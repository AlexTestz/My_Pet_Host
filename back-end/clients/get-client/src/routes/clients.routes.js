const express = require('express');
const router = express.Router();

const {
  getAllClients,
  getClientById
} = require('../controllers/clients.controller');

router.get('/clients', getAllClients);
router.get('/clients/:id', getClientById); 

module.exports = router;
