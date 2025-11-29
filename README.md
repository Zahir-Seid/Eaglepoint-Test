# Eaglepoint-Test

This repository contains my submissions for the **Full-Stack Developer Technical Assessment**.

## Overview

This repository shows solutions for multiple coding tasks, implemented in **Python**, **JavaScript**, and **FastAPI**. Each task includes:

- Step-by-step explanation of the solution process.
- Thought process and approaches considered.
- Clear reasoning for why the chosen solution is optimal for the task.


## Coding Tasks

1. **Smart Text Analyzer (Python)**  
   - Analyzes text for word count, average word length, longest words, and word frequency.  
   - Implemented manually without external libraries for full control and understanding.

2. **Async Data Fetcher with Retry (JavaScript)**  
   - Fetches data from an API with retry logic and delays.  
   - Includes a mock API that simulates failures to test the retry mechanism.

3. **FastAPI Sliding Window Log Rate Limiter (Python)**  
   - Implements a per-user rate limiter with a sliding window log algorithm.  
   - Limits requests to prevent abuse and automatically resets after the time window.

## Repository Structure

``` bash
├── async-fetcher
│   ├── fetchWithRetry.js
│   ├── mockApi.js
│   └── README.md
├── fastapi-rate-limiter
│   ├── main.py
│   └── README.md
├── README.md
└── smart-text-analyzer
    ├── README.md
    └── Smart_Text_Analyzer.py

```

### Each folder contains:

- The code for the task.
- A dedicated README with usage instructions and detailed documentation.

## How to Use

1. Navigate into the folder of the task you want to explore.  
2. Follow the instructions in that folder's README for setup and usage.  
3. Review the documentation to understand the implementation decisions and thought process.

