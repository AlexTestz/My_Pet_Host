const express = require('express');
const router = express.Router();
const { deleteClient } = require('../controllers/clients.controller');

// Ruta DELETE
router.delete('/clients/:id', deleteClient);

module.exports = router;
