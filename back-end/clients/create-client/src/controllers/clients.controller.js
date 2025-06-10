// src/controllers/clients.controller.js

exports.createClient = (req, res) => {
  const { name, email, phone } = req.body;

  if (!name || !email || !phone) {
    return res.status(400).json({ message: "Missing required fields" });
  }

  console.log("📥 New client received:", { name, email, phone });

  res.status(201).json({
    message: "Client created successfully",
    client: { name, email, phone },
  });
};
