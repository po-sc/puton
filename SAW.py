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
    [1, 0.7, 0.7, 1, 0.8, 0.8],
    [0.5, 0.5, 0.6, 0.6, 0.6, 0.5],
    [1, 0.6, 0.5, 0.6, 0.5, 0.6],
    [0.7, 0.5, 0.3, 0.6, 0.6, 0.4]
])
criteria_weights = np.array([0.2, 0.2, 0.1, 0.1, 0.2, 0.2])

normalized_matrix = normalize_criteria(decision_matrix)

result_ranking = saw(normalized_matrix, criteria_weights)
po = ["Spotify", "Yandex Music", "Apple Music", "YouTube Music"]
print("\nМетод SAW:")
for position, i in enumerate(result_ranking):
    print(f"{po[i]} - Позиция: {position + 1}")