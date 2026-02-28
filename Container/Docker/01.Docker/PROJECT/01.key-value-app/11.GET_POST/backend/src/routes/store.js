const express = require('express');
const {KeyValue} = require('../models/keyValue');

const storeRouter = express.Router();

storeRouter.get('/:key', async (req, res) => {
  const {key} = req.params;
  try {
    const keyValue = await KeyValue.findOne({ key });
    if (!keyValue) {
      return res.status(404).json({error: 'Key not found'});
    }
    return res.status(200).json({key: keyValue.key, value: keyValue.value});
  } catch (err) {
    return res.status(500).json({error: err.message});
  }
  
});

storeRouter.post('/', async (req, res) => {
  const {key, value} = req.body;
  if (!key || !value) {
    return res.status(400).json({error: 'Key and value are required'});
  }
  try{
    const existing = await KeyValue.findOne({ key });
    if (existing) {
      return res.status(400).json({error: 'Key already exists'});
    }
    const keyValue = new KeyValue({key, value});
    await keyValue.save();
  } catch (err) {
    return res.status(500).json({error: err.message});
  }
  res.send('Post from store route')
});

storeRouter.put('/:key', (req, res) => {
  res.send('Put from store route')
});

storeRouter.delete('/:key', (req, res) => {
  res.send('Delete from store route')
});

module.exports = {storeRouter};
