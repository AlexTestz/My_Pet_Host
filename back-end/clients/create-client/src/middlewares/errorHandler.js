function errorHandler(err, req, res, next) {
  console.error('❌ Global Error:', err);

  // 🔎 Inspección
  console.log('🔍 err.code:', err.code);
  console.log('🔍 err.message:', err.message);

  if (err.code === '23505') {
    return res.status(409).json({
      message: 'A record with this value already exists'
    });
  }

  if (err.status) {
    return res.status(err.status).json({ message: err.message });
  }

  res.status(500).json({ message: 'Internal Server Error' });
}

module.exports = errorHandler;
