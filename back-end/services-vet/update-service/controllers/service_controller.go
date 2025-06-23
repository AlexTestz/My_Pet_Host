package controllers

import (
	"context"
	"time"

	"github.com/AlexTestz/update-service/database"
	"github.com/AlexTestz/update-service/models"
	"github.com/gofiber/fiber/v2"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
)

func UpdateService(c *fiber.Ctx) error {
	id := c.Params("id")
	objID, err := primitive.ObjectIDFromHex(id)
	if err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Invalid ID"})
	}

	var updated models.Service
	if err := c.BodyParser(&updated); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Cannot parse JSON"})
	}

	// ⛔ Validaciones manuales

	// Tipo y presencia
	if updated.Name == "" || updated.Description == "" {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Name and Description are required"})
	}

	// Longitud mínima
	if len(updated.Name) < 3 {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Name must be at least 3 characters"})
	}
	if len(updated.Description) < 10 {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Description must be at least 10 characters"})
	}

	// Rangos válidos
	if updated.Price <= 0 || updated.Price > 1000 {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Price must be between 1 and 1000"})
	}
	if updated.Duration <= 0 || updated.Duration > 240 {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Duration must be between 1 and 240 minutes"})
	}

	// Validación de unicidad del nombre
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	collection := database.Client.Database("pet_care_services_db").Collection("services")

	var existing models.Service
	err = collection.FindOne(ctx, bson.M{"name": updated.Name, "_id": bson.M{"$ne": objID}}).Decode(&existing)
	if err == nil {
		return c.Status(fiber.StatusConflict).JSON(fiber.Map{"error": "A service with this name already exists"})
	}

	// Actualizar el documento
	update := bson.M{
		"$set": bson.M{
			"name":        updated.Name,
			"description": updated.Description,
			"price":       updated.Price,
			"duration":    updated.Duration,
		},
	}

	_, err = collection.UpdateOne(ctx, bson.M{"_id": objID}, update)
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": "Failed to update service"})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{"message": "Service updated ✅"})
}