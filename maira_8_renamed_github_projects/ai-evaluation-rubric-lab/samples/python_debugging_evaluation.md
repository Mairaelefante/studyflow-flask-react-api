# Sample Evaluation: Python Debugging

## User Task
Find the bug in a Python `average(numbers)` function that fails for an empty list.

## Model Response Being Evaluated
"The function is correct. No bug is present."

## Evaluation

### Step 1: Correctness
The response is incorrect. The function raises `ZeroDivisionError` when the list is empty.

### Step 2: Missing Edge Case
The model did not reason about the specific failure condition.

### Step 3: Better Answer
```python
def average(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)
```

## Score
Correctness: 1/5  
Clarity: 2/5  
Instruction Following: 1/5  
Reasoning Quality: 1/5

## Summary
The response misses the central edge case and should explain the empty-list failure.
