const express = require('express')

const app = express();
const port = process.env.PORT

app.get('/', (req, res)=>{
    res.status(200).send(`Welcome to ${process.env.APP_NAME}`)
})

app.listen(port, ()=> {
    console.log(`Listening on port ${port}`)
})