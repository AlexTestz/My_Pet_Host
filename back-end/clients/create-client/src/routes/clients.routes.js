// src/routes/clients.routes.js

const express = require('express');
const router = express.Router();

// Verifica que la ruta sea correcta (usa dos puntos ../)
const { createClient } = require('../controllers/clients.controller');

router.post('/clients', createClient);

module.exports = router;
