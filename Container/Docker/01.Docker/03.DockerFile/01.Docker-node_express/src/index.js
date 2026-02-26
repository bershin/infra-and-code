const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;
const users = [];

app.use(bodyParser.json());

// Hello world endpoint
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Get Registered Users
app.get('/users', (req, res) => {
  res.json({ users });
});

// Register a new User
app.post('/register', (req, res) => {
  const newUserId = req.body.userId;
  if (!newUserId) {
    return res.status(400).send('Username is required');
  }
  if (users.includes(newUserId)) {
    return res.status(409).json({ message: 'Username already exists' });
  }
  users.push(newUserId);
  res.status(201).json({ message: 'User registered successfully' });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
