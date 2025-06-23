const pool = require('../config/db');
//
exports.updateClient = async (req, res, next) => {
  const { id } = req.params;
  const { name, last_name, email, phone } = req.body;

  try {
    // Verificar si el cliente existe
    const existing = await pool.query('SELECT * FROM clients WHERE id = $1', [id]);
    if (existing.rows.length === 0) {
      return res.status(404).json({ message: 'Client not found' });
    }

    // Verificar si el email ya está en uso por OTRO cliente
    const duplicateEmail = await pool.query(
      'SELECT * FROM clients WHERE email = $1 AND id != $2',
      [email, id]
    );
    if (duplicateEmail.rows.length > 0) {
      return res.status(409).json({ message: 'Email already in use by another client' });
    }

    // Actualizar cliente
    const result = await pool.query(
      `UPDATE clients 
       SET name = $1, last_name = $2, email = $3, phone = $4 
       WHERE id = $5 
       RETURNING *`,
      [name, last_name, email, phone, id]
    );

    res.status(200).json({
      message: 'Client updated successfully',
      client: result.rows[0],
    });

  } catch (err) {
    console.error('❌ DB Error:', err);
    res.status(500).json({ message: err.message || 'Failed to update client' });
  }
};
