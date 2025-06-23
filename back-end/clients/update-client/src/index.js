//
require('dotenv').config();
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3003;

app.use(express.json());

const clientRoutes = require('./routes/clients.routes');
app.use('/api', clientRoutes);

app.get('/', (req, res) => {
  res.send('✅ Update Client Service is running!');
});

app.listen(PORT, () => {
  console.log(`🚀 Server is listening on port ${PORT}`);
});
