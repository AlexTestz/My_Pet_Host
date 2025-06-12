require('dotenv').config();
const express = require('express');
const cors = require('cors'); 
const app = express();


// Middleware
app.use(cors());            
app.use(express.json());

// Routes
const clientRoutes = require('./routes/clients.routes');
app.use('/api', clientRoutes);

// Root route (simple health check)
app.get('/', (req, res) => {
  res.send('✅ Create Client Service is running!');
});

// Manejo global de errores
const errorHandler = require('./middlewares/errorHandler');
app.use(errorHandler);

// Solo escuchar si este archivo es el principal
if (require.main === module) {
  const PORT = process.env.PORT || 3001;
  app.listen(PORT, () => {
    console.log(`🚀 Server is listening on port ${PORT}`);
  });
}

// Exportar para pruebas
module.exports = app;
