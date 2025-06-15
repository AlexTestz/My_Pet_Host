const pool = require('../config/db');

exports.createClient = async (req, res, next) => {
  const { name, last_name, email, phone } = req.body;

  try {
    const existing = await pool.query('SELECT * FROM clients WHERE email = $1', [email]);

    if (existing.rows.length > 0) {
      const error = new Error('A client with this email already exists');
      error.status = 409;
      throw error;
    }

    const result = await pool.query(
      'INSERT INTO clients (name, last_name, email, phone) VALUES ($1, $2, $3, $4) RETURNING *',
      [name, last_name, email, phone]
    );

    res.status(201).json({
      message: 'Client created and saved to database ✅',
      client: result.rows[0],
    });
  } catch (err) {
    next(err); // 👈 Esto manda el error al manejador global
  }
};

exports.getClientById = async (req, res) => {
  const { id } = req.params;

  try {
    const result = await pool.query('SELECT * FROM clients WHERE id = $1', [id]);

    if (result.rows.length === 0) {
      return res.status(404).json({ message: 'Client not found' });
    }

    res.status(200).json({ client: result.rows[0] });
  } catch (err) {
    console.error('❌ DB Error:', err);
    res.status(500).json({ message: 'Failed to fetch client' });
  }
};
