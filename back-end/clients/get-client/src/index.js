require('dotenv').config();
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3002;

app.use(express.json());

// Routes
const clientRoutes = require('./routes/clients.routes');
app.use('/api', clientRoutes);

// Health check
app.get('/', (req, res) => {
  res.send('✅ Get Client Service is running!');
});

app.listen(PORT, () => {
  console.log(`🚀 Server is listening on port ${PORT}`);
});
