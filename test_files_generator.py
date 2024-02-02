import random

for i in range(1, 51):
    file_name = f"simple{i}.avl"
    num_instructions = random.randint(5, 100) 
    instructions = []

    for i in range(num_instructions):
        operation_type = random.choice(['i', 'd'])
        number = random.randint(1, 1000) 
        instructions.append(f"{operation_type}{number}")
    instructions.append("p")

    with open(file_name, 'w') as file:
        file.write(' '.join(instructions))

