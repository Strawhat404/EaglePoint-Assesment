# EaglePoint AI - Technical Assessment Submission

## Overview
This repository contains solutions for the Full-stack Developer Technical Assessment.The searched url links and more detailed documentation is shared on Google Docs https://docs.google.com/document/d/1DVtA7zH2mRna-WS9-puwgg2A2nd_xat4xOJ-HdlsMR4/edit?usp=sharing
- **Task 1:** Smart Text Analyzer (Python)
- **Task 2:** Async Data Fetcher with Retry (JavaScript)
- **Task 3:** Rate Limiter (Python)

---

##  Task 1: Smart Text Analyzer
**File:** `task1.py`
**Language:** Python

### Searches made
*   "python remove punctuation from string manual loop"
*   "python format float 2 decimal places"
*   "how to calculate average word length python"
*   "python find max value in list of strings"

### Aproach
I initially considered using Python's `re` (Regex) module and `collections.Counter` for efficiency. However, I decided to implement the logic **manually** using loops and basic string manipulation.
*   **Because** Relying on libraries hides the underlying logic. It avoids external dependencies.

### 🛠️ Step-by-Step Solution
1.  **Cleaning Text:** I faced an issue where punctuation (like `word!`) was counted as part of the word.
    *   *then* I implemented a loop that iterates through every character. If the character is alphanumeric or a space, I kept it otherwise I replaced it with a space.
2.  **Calculating Stats:**
    *   *Average:* Summed the lengths of all words and divided by the count. Used `float(format(val, ".2f"))` to ensure strict 2-decimal formatting.
    *   *Longest Word:* I trid Found the maximum length integer first  then filtered the list to find all words matching that length.
3.  **Frequency:** Instead of `Counter`, I used a standard dictionary to increment counts manually.

###Why this solution is best
It is **dependency-free** and highly readable. By avoiding complex Regex patterns the code is easier to debug and modify for specific edge cases  in the future.

---

## Task 2: Async Data Fetcher with Retry
**File:** `task2.js`
**Language:** JavaScript (Node.js)

### Search 
*   "javascript wait 1 second async await"
*   "how to implement javascript sleep promise function"
*   "javascript try catch retry loop pattern"
*   "how to mock api calls in javascript random failure"

### Approach
JavaScript does not have a native `sleep()` function like Python. My main challenge was creating a pause between retries without blocking the main thread.
*   **Then** I created a `wait(ms)` helper function that wraps `setTimeout` in a Promise.
### Step-by-Step Solution
1.  **Mocking the API:** I needed to simulate a network that fails randomly. I used `Math.random()` to generate a 70% failure rate.
2.  **The Retry Loop:** I implemented a `for` loop that runs up to `maxRetries`.
3.  **Problem Faced:** I initially included `require('node-fetch')` thinking I needed it, but realized it would cause the code to crash on machines without `node_modules`.
    *   *so* I removed the import and relied entirely on the internal `mock` function to ensure the code is portable.
4.  **also** Used a `try/catch` block. If a request fails, it catches the error, waits 1 second and the loop continues. If the loop finishes it throws a final error.

### Why this solution is best
It demonstrates a solid understanding of **Asynchronous JavaScript** and the Event Loop. The solution is **self-contained** (no `npm install` required) and handles network jitter simulation realistically.

---

## Task 3: Rate Limiter
**File:** `task3.py`
**Language:** Python

###  Search 
*   "rate limiter algorithms sliding window vs token bucket"
*   "python time.time() current timestamp"
*   "python list filtering list comprehension"

###  Approach
I chose the **Sliding Window Log** algorithm.
*   **Why:** For a requirement of "5 requests per 60 seconds", exact precision is needed. Simpler algorithms (like Fixed Window) can allow bursts of traffic at the edges of the window e.g., 5 requests at 00:59 and 5 more at 01:01. Storing exact timestamps prevents this.

### Step by Step Solution
1.  **Data Structure:** I used a dictionary `user_requests` where the Key is the `user_id` and the Value is a `list` of timestamps.
2.  **The Logic:**
    *   When a request comes in, I verify if the user exists in the dictionary.
    *   **Cleanup:** I filter the list to keep *only* timestamps from the last 60 seconds (`current_time - t < 60`).
    *   **Decision:** If the length of the filtered list is less than 5, I add the new time and return `True`. Otherwise, I return `False`.
3.  **Problem Faced:** I needed to ensure one user's traffic didn't block another.
    *   *then* The dictionary approach isolates every user's history perfectly.

###  Why this solution is best
The Sliding Window Log is the most accurate algorithm for strict rate limiting. Implementation in Python is concise due to List Comprehensions

---

## How to Run
1.  **Task 1:** `python task1.py`
2.  **Task 2:** `node task2.js`
3.  **Task 3:** `python task3.py`