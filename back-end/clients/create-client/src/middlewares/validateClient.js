const { body, validationResult } = require('express-validator');

const validateClient = [
  body('name')
    .notEmpty().withMessage('Name is required')
    .isLength({ min: 2 }).withMessage('Name must be at least 2 characters'),

  body('last_name')
    .notEmpty().withMessage('Last name is required'),

  body('email')
    .notEmpty().withMessage('Email is required')
    .isEmail().withMessage('Email must be valid'),

  body('phone')
    .optional()
    .isNumeric().withMessage('Phone must contain only numbers'),

(req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    const formattedErrors = errors.array().map(err => err.msg);
    return res.status(422).json({ errors: formattedErrors });
  }
  next();
}

];

module.exports = validateClient;
