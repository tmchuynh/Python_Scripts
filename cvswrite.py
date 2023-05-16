import csv
from datetime import datetime, timedelta
import random

header = ['date', 'rooms_available', 'price_per_night', 'room_id']
start_date = datetime(2023, 1, 1)  # Specify the starting date
num_iterations = 550  # Number of iterations

data = []

for i in range(num_iterations):
    current_date = start_date + timedelta(days=i)
    random_number1 = random.randint(25, 550)
    random_number2 = random.randint(152, 252)
    random_number3 = random.randint(1, 1468)
    data.append([current_date, random_number1, random_number2, random_number3])


with open('wedding.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write multiple rows
    writer.writerows(data)
