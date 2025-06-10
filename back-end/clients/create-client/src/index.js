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

//test de error
//app.get('/error-test', (req, res, next) => {
  //const error = new Error('💥 This is a test error');
  //error.status = 418; // Código divertido: “I’m a teapot” (opcional)
  //next(error);
//});


// 🛑 Manejo global de errores (debe ir después de TODAS las rutas)
const errorHandler = require('./middlewares/errorHandler');
app.use(errorHandler);

app.listen(PORT, () => {
  console.log(`🚀 Server is listening on port ${PORT}`);
});
