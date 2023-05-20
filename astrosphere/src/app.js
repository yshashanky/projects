const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const https = require("node:https");

const app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", function (req, res) {
    res.send("It's working");
});

app.listen(6969, function () {
    console.log("server is running on 6969...")
});