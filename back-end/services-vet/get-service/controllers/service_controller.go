package controllers

import (
	"context"
	"time"

	"github.com/AlexTestz/get-service/database"
	"github.com/AlexTestz/get-service/models"
	"github.com/gofiber/fiber/v2"
	"go.mongodb.org/mongo-driver/bson"
)

func GetServices(c *fiber.Ctx) error {
    collection := database.Client.Database("pet_care_services_db").Collection("services")
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()

    // ✅ Leer query param
    name := c.Query("name")

    // 📄 Condición de búsqueda
    filter := bson.M{}
    if name != "" {
        filter = bson.M{"name": bson.M{"$regex": name, "$options": "i"}} // búsqueda insensible a mayúsculas
    }

    cursor, err := collection.Find(ctx, filter)
    if err != nil {
        return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": "Error fetching services"})
    }

    var services []models.Service
    if err := cursor.All(ctx, &services); err != nil {
        return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": "Error parsing results"})
    }

    return c.JSON(services)
}
