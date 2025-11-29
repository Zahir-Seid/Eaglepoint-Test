// This script fetches data from a URL with retries on failure.
// It waits 1 second between retries and throws an error if all attempts fail.

async function fetchWithRetry(url, maxRetries = 3, delayMs = 1000) {
  let attempt = 0;       // Track which attempt we're on
  let lastError = null;  // Store the last error in case all retries fail

  while (attempt <= maxRetries) {
    try {
      // Attempt to fetch the URL
      const resp = await fetch(url); 
      if (!resp.ok) {
        // If HTTP status is not 200-299, treat as failure
        throw new Error(`HTTP error! status: ${resp.status}`);
      }

      // Parse JSON response
      const data = await resp.json();
      return data; // on success we return the data

    } catch (err) {
      lastError = err; // Save error for later
      if (attempt === maxRetries) break; // Stop retrying after max attempts

      // Log and wait before retrying
      console.warn(`Attempt ${attempt + 1} failed: ${err.message}. Retrying in ${delayMs}ms...`);
      await new Promise((res) => setTimeout(res, delayMs));
    }
    attempt++;
  }

  // If we get here, all retries failed
  throw new Error(`Failed to fetch ${url} after ${maxRetries + 1} attempts. Last error: ${lastError}`);
}

(async () => {
  try {
    // Call our local mock API
    const data = await fetchWithRetry("http://localhost:3000/data", 5, 1000);
    console.log("Successfully fetched:", data);
  } catch (err) {
    console.error("All retries failed:", err.message);
  }
})();

