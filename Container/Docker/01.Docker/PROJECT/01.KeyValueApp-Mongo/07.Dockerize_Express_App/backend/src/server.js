const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());

app.get('/health', (req, res) => {
    res.status(200).json({ status: 'UP' });
});

// MongoDB connection
mongoose.connect('mongodb://mongodb/key-value-app', {
    auth: {
        username: 'key-value-app',
        password: 'key-value-app'
    },
    connectTimeoutMS: 500
}).then(() => {
    app.listen(PORT, () => {
        console.log(`Server is running on port ${PORT}`);
    });
    console.log('Connected to MongoDB');
}).catch((err) => {
    console.error('Error connecting to MongoDB:', err);
});

