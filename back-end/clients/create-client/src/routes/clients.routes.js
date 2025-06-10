// src/routes/clients.routes.js

const express = require('express');
const router = express.Router();

// Verifica que la ruta sea correcta (usa dos puntos ../)
const { createClient } = require('../controllers/clients.controller');
const validateClient = require('../middlewares/validateClient');


router.post('/clients',validateClient, createClient);

module.exports = router;
