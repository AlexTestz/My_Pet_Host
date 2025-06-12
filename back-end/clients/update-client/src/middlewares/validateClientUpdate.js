const { body, validationResult } = require('express-validator');

const validateClientUpdate = [
  body('name')
    .notEmpty().withMessage('Name is required')
    .isLength({ min: 2 }).withMessage('Name must be at least 2 characters'),

  body('last_name')
    .notEmpty().withMessage('Last name is required')
    .isLength({ min: 2 }).withMessage('Last name must be at least 2 characters'),

  body('email')
    .isEmail().withMessage('Email must be valid'),

  body('phone')
    .optional()
    .isNumeric().withMessage('Phone must contain only numbers'),

  // Manejo de errores
  (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      const messages = errors.array().map(err => err.msg);
      return res.status(400).json({ errors: messages });
    }
    next();
  }
];

module.exports = validateClientUpdate;
