const express = require('express');
const router = express.Router();
const { updateClient } = require('../controllers/clients.controller');
const validateClientUpdate = require('../middlewares/validateClientUpdate');

// Validación + Controlador
router.put('/clients/:id', validateClientUpdate, updateClient);

module.exports = router;
// Este archivo define las rutas para actualizar clientes.
// Utiliza el middleware de validación y el controlador para manejar las solicitudes PUT a /clients/:id.