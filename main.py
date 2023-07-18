import csv

def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            data.append(row)
    return data

def calculate_percentage_above_age_with_high_cholesterol(data, age_threshold):
    total_above_age = 0
    total_above_age_with_high_cholesterol = 0

    for person in data:
        age = float(person[0])
        cholesterol = float(person[4])
        if age > age_threshold:
            total_above_age += 1
            if cholesterol > 240:
                total_above_age_with_high_cholesterol += 1

    percentage = (total_above_age_with_high_cholesterol / total_above_age) * 100
    return percentage

def calculate_percentage_above_age_with_high_cholesterol_and_sugar(data, age_threshold):
    total_above_age = 0
    total_above_age_with_high_cholesterol_and_sugar = 0

    for person in data:
        age = float(person[0])
        cholesterol = float(person[4])
        sugar = float(person[5])
        if age > age_threshold:
            total_above_age += 1
            if cholesterol > 240 and sugar > 120:
                total_above_age_with_high_cholesterol_and_sugar += 1

    percentage = (total_above_age_with_high_cholesterol_and_sugar / total_above_age) * 100
    return percentage

def is_related_to_left_ventricular_hypertrophy(data):
    total_samples = len(data)
    total_related = 0

    for person in data:
        cholesterol = float(person[4])
        sugar = float(person[5])
        heart_hypertrophy = float(person[6])
        if cholesterol > 240 and sugar > 120 and heart_hypertrophy == 2:
            total_related += 1

    percentage = (total_related / total_samples) * 100
    return percentage

data = load_data('data.csv')
age_threshold = 40

cholesterol_percentage = calculate_percentage_above_age_with_high_cholesterol(data, age_threshold)
print(f"A porcentagem de pessoas acima de {age_threshold} anos com colesterol alto é: {cholesterol_percentage:.2f}%")

cholesterol_sugar_percentage = calculate_percentage_above_age_with_high_cholesterol_and_sugar(data, age_threshold)
print(f"A porcentagem de pessoas acima de {age_threshold} anos com colesterol alto e alto teor de açúcar é: {cholesterol_sugar_percentage:.2f}%")

heart_hypertrophy_percentage = is_related_to_left_ventricular_hypertrophy(data)
print(f"A porcentagem de pessoas com colesterol alto, alto teor de açúcar e hipertrofia ventricular esquerda é: {heart_hypertrophy_percentage:.2f}%")
