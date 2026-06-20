# Sample Evaluation: Machine Learning Metrics

## User Task
A dataset has 95% negative cases and 5% positive cases. Is accuracy enough?

## Model Response Being Evaluated
"Yes. Accuracy is always the best metric."

## Evaluation

### Step 1: Correctness
The response is incorrect. Accuracy can be misleading for imbalanced datasets.

### Step 2: Reasoning
A model that predicts every case as negative would reach 95% accuracy but fail to identify positives.

### Step 3: Better Answer
Use precision, recall, F1-score, PR-AUC, ROC-AUC, and the confusion matrix depending on the business cost of false positives and false negatives.

## Score
Correctness: 1/5  
Clarity: 3/5  
Instruction Following: 2/5  
Reasoning Quality: 1/5

## Summary
The answer should explain class imbalance and recommend more useful metrics.
