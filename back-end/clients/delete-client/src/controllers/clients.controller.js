const pool = require('../config/db');

exports.deleteClient = async (req, res, next) => {
  const { id } = req.params;

  try {
    // Verifica si el cliente existe
    const existing = await pool.query('SELECT * FROM clients WHERE id = $1', [id]);
    if (existing.rows.length === 0) {
      return res.status(404).json({ message: 'Client not found' });
    }

    // Elimina el cliente
    await pool.query('DELETE FROM clients WHERE id = $1', [id]);

    res.status(200).json({ message: 'Client deleted successfully' });
  } catch (err) {
    console.error('❌ DB Error:', err);
    res.status(500).json({ message: 'Failed to delete client' });
  }
};
