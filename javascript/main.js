const express = require("express");
const app = express();

app.get("/", (req, res) => res.json("This is simple JS application for Lab3"));

app.listen(8080, () => {
  console.log("server running on port 8080");
});
