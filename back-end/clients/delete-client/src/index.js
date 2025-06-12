require('dotenv').config();
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3004;

app.use(express.json());

const clientRoutes = require('./routes/clients.routes');
app.use('/api', clientRoutes);

app.get('/', (req, res) => {
  res.send('✅ Delete Client Service is running!');
});

app.listen(PORT, () => {
  console.log(`🚀 Server is listening on port ${PORT}`);
});
// This code sets up an Express server for the Delete Client service.
// It listens on a specified port (default 3004) and uses a router for client-related routes.