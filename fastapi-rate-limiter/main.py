from fastapi import FastAPI, HTTPException, Request
from collections import deque
from time import time
from typing import Dict

# Create the FastAPI app
app = FastAPI()

# We use Rate Limiter using sliding window log algorithim  
MAX_REQUESTS = 5   # Maximum requests allowed per user
WINDOW_SIZE = 60   # Time window in seconds

# Data Structure
# ===========================
# We'll store a mapping of user_id -> deque of request timestamps
# Using deque is efficient because popping from left is O(1)
user_requests: Dict[str, deque] = {}

# Helper function: Check if a request is allowed
def is_allowed(user_id: str) -> bool:
    
    # Returns True if the user can make a request, False if rate limit exceeded.
    
    now = time()

    if user_id not in user_requests:
        # First request from this user -> create a deque
        user_requests[user_id] = deque()

    timestamps = user_requests[user_id]

    # Remove timestamps older than WINDOW_SIZE seconds
    # This automatically resets old requests
    while timestamps and timestamps[0] <= now - WINDOW_SIZE:
        timestamps.popleft()

    if len(timestamps) < MAX_REQUESTS:
        # User is within rate limit -> allow request
        timestamps.append(now)
        return True
    else:
        # User exceeded rate limit -> block request
        return False

# API Endpoint
# Example endpoint that is rate-limited per user.
# Users exceeding the limit receive HTTP 429.
# ===========================
@app.get("/api/data")
async def get_data(request: Request, user_id: str):
    if not is_allowed(user_id):
        # Block the request with a 429 Too Many Requests
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")

    # Example response
    return {"message": f"Hello {user_id}, your request is allowed!"}


# Notes / Explanation
# 1. Sliding Window Log: We track each request timestamp individually.
#    This allows precise control over the "last 60 seconds" window.
# 2. Using deque ensures fast removal of old timestamps (O(1)).
# 3. Each user has their own queue, so tracking is per user_id.
# 4. Auto-reset happens naturally because old timestamps are removed.
# 5. HTTP 429 is returned when the user exceeds the allowed number of requests.

