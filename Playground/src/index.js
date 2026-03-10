const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 6000;
const user_record = [];

app.use(bodyParser.json())

app.get('/', (req, res) => {
  return res.status(200).send('Hello world');
});

app.get('/users', (req, res) => {
  return res.status(200).json(user_record);
});

app.post('/register', (req, res) => {
  const userId = req.body.userid;
  if (!userId) {
    return res.status(400).send('Body should contain userid');
  }
  if (user_record.includes(userId)) {
    return res.status(400).send('Userid already exists');
  }
  user_record.push(userId);
  return res.status(400).send('Userid added');
});

app.listen(port, (req, res) => {
  console.log('Listening on port {port}');
});
