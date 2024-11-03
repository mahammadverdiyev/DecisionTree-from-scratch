data = []

with open('breast-cancer-wisconsin.data.txt', 'r') as file:
    l = []
    for line in file:
        line = line.strip()
        line = line.split(',')
        if '?' in line:
            continue
        curr_data = map(int, line)
        data.append(curr_data)
