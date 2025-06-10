// src/index.js

require('dotenv').config();
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(express.json());

// Routes
const clientRoutes = require('./routes/clients.routes');
app.use('/api', clientRoutes);

// Root route (simple health check)
app.get('/', (req, res) => {
  res.send('✅ Create Client Service is running!');
});

app.listen(PORT, () => {
  console.log(`🚀 Server is listening on port ${PORT}`);
});
