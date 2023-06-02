const express = require('express')
const axios = require('axios')

const app = express()

app.get("/api", (req, res) => {
    res.json({"users": ["userone", "usertwo", "userthree", "userfour"]})
});

app.get("/pictureOfDay", async(req, res) =>{
    
    try{

        const response = await axios.get('https://api.nasa.gov/planetary/apod?api_key=SqDvmlkP2nm7fYyiJ1wSxIhWCicRU3dEod6qM7H3');
        const responseData = response.data;
        res.json(responseData);

    } catch (error) {
        console.error('Error making API call:', error.message);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.listen(5000, () => {
    console.log("Server started on port 5000")
});