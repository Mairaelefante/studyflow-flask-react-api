# Sample Evaluation: JavaScript Async Reasoning

## User Task
Explain why JavaScript logs `Start`, `End`, then `Data` when using `fetch().then(...)`.

## Model Response Being Evaluated
"JavaScript runs all lines at the same time, so the order is random."

## Evaluation

### Step 1: Correctness
The response is incorrect. The order is not random.

### Step 2: Conceptual Issue
The model confuses asynchronous behavior with randomness.

### Step 3: Better Answer
`Start` logs first because it is synchronous. `fetch` starts and returns a promise. JavaScript continues and logs `End`. When the promise resolves, the callback logs `Data`.

## Score
Correctness: 2/5  
Clarity: 2/5  
Instruction Following: 3/5  
Reasoning Quality: 2/5

## Summary
The answer should explain promises and callback timing more accurately.
