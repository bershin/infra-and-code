const express = require('express');

const healthRouter = express.Router();

healthRouter.get('/', (req, res) => {
  res.status(200).json({ status: 'UP!' });
});

module.exports = { healthRouter };
