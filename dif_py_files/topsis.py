import numpy as np
def topsis_electre(matrix, weights, thresholds):
    num_alternatives, num_criteria = matrix.shape
    normalized_matrix = matrix / np.linalg.norm(matrix, axis=0)
    weighted_normalized_matrix = normalized_matrix * weights
    ideal_solution = np.max(weighted_normalized_matrix, axis=0)
    anti_ideal_solution = np.min(weighted_normalized_matrix, axis=0)
    concordance_matrix = np.zeros((num_alternatives, num_alternatives), dtype=int)
    discordance_matrix = np.zeros((num_alternatives, num_alternatives), dtype=int)
    for i in range(num_alternatives):
        for j in range(num_alternatives):
            if i != j:
                if all(weighted_normalized_matrix[i] >= weighted_normalized_matrix[j] - thresholds):
                    concordance_matrix[i, j] = 1
                if any(weighted_normalized_matrix[j] > weighted_normalized_matrix[i] + thresholds):
                    discordance_matrix[i, j] = 1
    ideal_distances = np.linalg.norm(weighted_normalized_matrix - ideal_solution, axis=1)
    anti_ideal_distances = np.linalg.norm(weighted_normalized_matrix - anti_ideal_solution, axis=1)
    relative_closeness = anti_ideal_distances / (ideal_distances + anti_ideal_distances)
    best_alternative_index = np.argmax(relative_closeness)
    alternative_positions = np.argsort(relative_closeness)[::-1]
    return best_alternative_index, alternative_positions
decision_matrix = np.array([
    [0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
    [0.5, 0.5, 0.6, 0.6, 0.6, 0.5],
    [1, 0.6, 0.5, 0.6, 0.5, 0.6],
    [0.7, 0.5, 0.3, 0.6, 0.6, 0.4]
])
criteria_weights = np.array([0.2, 0.2, 0.1, 0.1, 0.2, 0.2])
criteria_thresholds = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
best_po_index, all_positions = topsis_electre(decision_matrix, criteria_weights, criteria_thresholds)
po = ["Spotify", "Yandex Music", "Apple Music", "YouTube Music"]
print("Лучший музыкальный сервис:", po[best_po_index])
print("Позиции всех музыкальных сервисов:", {po[i]: position + 1 for position, i in enumerate(all_positions)})
