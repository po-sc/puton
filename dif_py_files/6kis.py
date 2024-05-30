# def main(P):
#     L = {abs(p) for p in P if 97 > p > -94}
#     N = {7 * p for p in P if p > float("-inf") and p <= 15}
#     H = N | L
#     lower_bound_sum = sum(n ** 3 for n in H)
#     result = len(L.intersection(H))
#     u = result + lower_bound_sum
#     return u
#
# print(main({-91, 11, 44, 77, 45, -49, 83, -74, 27, -98}))
# print(main({40, -54, 78, -18, 82, 54, 88, -71, -99, 30}))
#


def main(P):
    L = {abs(p) for p in P if -94 < p < 97}
    N = {7 * p for p in P if p <= 15}
    H = N | L
    lower_bound_sum = sum(n ** 3 for n in H)
    result = len(L) * len(H)
    u = result + lower_bound_sum
    return u

print(main({-91, 11, 44, 77, 45, -49, 83, -74, 27, -98}))
print(main({40, -54, 78, -18, 82, 54, 88, -71, -99, 30}))
