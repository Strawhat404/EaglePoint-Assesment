#  Eagle Point AI - Technical Assessment

This repository contains my solutions for the Full-stack Developer Technical Assessment. It demonstrates proficiency in **Python** and **JavaScript**, focusing on algorithmic thinking, asynchronous programming, and system design concepts.

##  Project Structure

### 1. Smart Text Analyzer (Python)
*   **File:** `task1.py`
*   **Description:** A text processing tool that cleans input using Regex but later changed to manual text cleaning to enhance readablity , calculates word statistics (average length, longest words), and generates frequency maps using `collections.Counter`.

### 2. Async Data Fetcher (JavaScript)
*   **File:** `task2.js`
*   **Description:** A robust data fetching simulation that implements a **Retry Pattern** with exponential backoff (wait logic) to handle unstable network requests.

### 3. Rate Limiter (Python)
*   **File:** `task3.py`
*   **Description:** An implementation of the **Sliding Window Log** algorithm to strictly limit API requests (5 req/60s) per user, ensuring precise traffic control.

---

##  How to Run

**Prerequisites:** Python 3.x and Node.js installed.

```bash
# Run Task 1 (Text Analyzer)
python task1.py

# Run Task 2 (Async Fetcher)
node task2.js

# Run Task 3 (Rate Limiter)
python task3.py
