const { Pool } = require('pg');

// ✅ Solo carga .env local si estás en desarrollo
if (process.env.NODE_ENV !== 'ci' && process.env.NODE_ENV !== 'test') {
  const path = require('path');
  const dotenv = require('dotenv');
  dotenv.config({ path: path.resolve(__dirname, '../../.env') });
}

// 🔐 Pool usando variables de entorno (ya sea desde .env o GitHub Actions)
const pool = new Pool({
  host: process.env.PG_HOST,
  port: process.env.PG_PORT,
  user: process.env.PG_USER,
  password: process.env.PG_PASSWORD,
  database: process.env.PG_DATABASE,
});

module.exports = pool;
