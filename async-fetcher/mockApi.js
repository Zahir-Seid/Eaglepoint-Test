// This is a simple API server that sometimes fails randomly to simulate network/API errors.
// When successful, it returns a "real" message and API key.

import express from "express";  // Fast and simple web framework
const app = express();
const PORT = 3000;

// Our “real” data that the fetcher will get
const realData = {
  message: "Thank you for subscribing to Free APIMap!",
  apiKey: "28383001833883390202",
};

app.get("/data", (req, res) => {
  // Randomly fail half the time
  if (Math.random() < 0.5) {
    // Simulate server error
    res.status(500).json({ error: "Random server error, please retry!" });
  } else {
    // Success response
    res.status(200).json(realData);
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Mock API server running on http://localhost:${PORT}`);
});

