const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();

const port = process.env.PORT || 3000;
const mongoHost = process.env.MONGO_HOST || 'mongodb';

// Middleware
app.use(bodyParser.json());

app.get('/health', (req, res) => {
    res.status(200).json({ status: 'UP!' });
});

// MongoDB connection
mongoose.connect(`mongodb://${mongoHost}/${process.env.KV_DATABASE || 'key-value-app'}`, {
    auth: {
        username: process.env.KV_USER || 'key-value-app',
        password: process.env.KV_PASSWORD || 'key-value-app'
    },
    connectTimeoutMS: 500
}).then(() => {
    app.listen(port, () => {
        console.log(`Server is running on port ${port}`);
    });
    console.log('Connected to MongoDB');
}).catch((err) => {
    console.error('Error connecting to MongoDB:', err);
});

