def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

if __name__ == "__main__":
    arr = list(map(int, input("Введите числа через пробел: ").strip().split()))
    k = int(input("Введите максимальное значение в массиве: ").strip())
    sorted_arr = bucketsort(arr, k)
    print("Отсортированный массив:", sorted_arr)
