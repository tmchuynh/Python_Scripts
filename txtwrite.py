data = []
num_iterations = 1468  # Number of iterations

for i in range(num_iterations):
    query = "UPDATE guest_rooms SET name = 'room" + str(i) + "' WHERE id = " + str(i) + ";"
    data.append(query)


with open('wedding.txt', 'w') as f:
    for query in data:
        f.write(query + '\n')