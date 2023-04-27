# Коля и дата-центры

n, m, q = map(int, input().split())

data_centers = [(0, m)] * n  # создаем список с данными о дата-центрах

for i in range(q):
    event = input().split()
    if event[0] == 'RESET':
        data_centers[int(event[1]) - 1] = (data_centers[int(event[1]) - 1][0] + 1, m)
    elif event[0] == 'DISABLE':
        i, j = map(int, event[1:])
        data_centers[i - 1] = (data_centers[i - 1][0], data_centers[i - 1][1] - 1)
    elif event[0] == 'GETMAX':
        max_center = max(range(n), key=lambda x: data_centers[x][0] * data_centers[x][1])
        print(max_center + 1)
    elif event[0] == 'GETMIN':
        min_center = min(range(n), key=lambda x: data_centers[x][0] * data_centers[x][1])
        print(min_center + 1)
