import numpy as np

def analyze_criteria(matrix):
    criteria_means = np.mean(matrix, axis=0)
    return criteria_means

def determine_weights(criteria_means):
    weights = criteria_means / np.sum(criteria_means)
    return weights

def normalize_criteria(matrix):
    normalized_matrix = matrix / np.linalg.norm(matrix, axis=0)
    return normalized_matrix

def saw(matrix, weights):
    num_alternatives, num_criteria = matrix.shape
    scores = np.dot(matrix, weights)
    ranking = np.argsort(scores)[::-1]
    return ranking

decision_matrix = np.array([
    [0.9, 0.9, 0.6, 0.6, 0.6],
    [0.8, 0.9, 0.5, 0.4, 0.2],
    [0.5, 0.9, 0.55, 0.4, 0.6],
    [0.9, 0.9, 0.5, 0.6, 0.6]
])
criteria_weights = np.array([0.35, 0.2, 0.2, 0.15, 0.1])

normalized_matrix = normalize_criteria(decision_matrix)

result_ranking = saw(normalized_matrix, criteria_weights)
po = ["Premier Pro", "Final Cut Pro", "After Effects", "Vegas Pro"]
print("\nРанжирование ПО по методу SAW:")
for position, i in enumerate(result_ranking):
    print(f"{po[i]} - Позиция: {position + 1}")