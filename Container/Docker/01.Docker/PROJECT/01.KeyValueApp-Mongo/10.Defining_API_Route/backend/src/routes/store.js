const express = require('express');

const storeRouter = express.Router();

storeRouter.get('/:key', (req, res) => {
  res.send('Get from store route')
});

storeRouter.post('/', (req, res) => {
  res.send('Post from store route')
});

storeRouter.put('/:key', (req, res) => {
  res.send('Put from store route')
});

storeRouter.delete('/:key', (req, res) => {
  res.send('Delete from store route')
});

module.exports = {storeRouter};
