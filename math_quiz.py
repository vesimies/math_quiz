import random # For getting random numbers for the excercises

# The opening display/text
def display_title():
    title="Matikka tehtäviä lapsille"
    print("*"*len(title))
    print(title)
    print("*"*len(title)) 

# Choose the age level
def get_level_input():
    while True:
        try:
            level = int(input("Valitse taso (1 = 7-9-vuotiaalle, 2 = 10-12-vuotiaalle): "))
            if level == 1 or level == 2:
                return level
            else:
                print("Väärä taso, yritä uudestaan!")
        except ValueError:
            print("Anna numero 1 tai 2.")

# The options for what excercises they want to practise on
def display_options():
    print("-"*18)
    print("Harjoitus vaihtoehdot:")
    list_options=[
        "1. Pluslaskuja", 
        "2. Miinuslaskuja", 
        "3. Kertolaskuja", 
        "4. Jakolaskuja", 
        "5. Sekalaista", 
        "6. Lopeta"
        ]
    for option in list_options:
        print(option)
    print("-"*18)

# Choosing the option
def get_user_input():
    while True: # Loop until valid input is provided
        try:
            choise=int(input("Syötä valintasi (numero 1-6): "))
            if 1 <= choise <= 6: # Check if valid input has been provided
                return choise
            else:
                print("Väärä vaihtoehto, yritä uudestaan!")
        except ValueError: # Message for non integral input
            print("Ei kirjaimia, anna numero (1-6)")

# Ask for the answer for a problem
def get_user_solution(problem):
    print("Kerro vastaus: ")
    print(problem, end="")
    result=int(input(" = "))
    return result

# Generate a math problem
def get_problem(operation,level):
    if level == 1: # For ages 7-9
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
    else:  # For ages 10-12
        num1 = random.randint(10, 100)
        num2 = random.randint(10, 100)

    if operation == 1:  # Addition
        problem = f"{num1} + {num2}"
        solution = num1 + num2
        
    elif operation == 2:  # Subtraction
        while num1 < num2:  # Ensure num1 is greater than num2
            num1 = random.randint(1, 20) if level == 1 else random.randint(10, 100)
            num2 = random.randint(1, 20) if level == 1 else random.randint(10, 100)
        problem = f"{num1} - {num2}"
        solution = num1 - num2
        
    elif operation == 3:  # Multiplication
        num1 = random.randint(1, 2) if level == 1 else random.randint(2, 10)
        num2 = random.randint(1, 10) if level == 1 else random.randint(2, 10)
        problem = f"{num1} * {num2}"
        solution = num1 * num2
        
    elif operation == 4:  # Division (ensuring whole number results)
        if level == 1:
            num2 = random.randint(1, 5)  # Divisor for simpler problems
            num1 = num2 * random.randint(1, 4)  # Ensure dividend ≤ 20
        else:  # Level 2
            num2 = random.randint(2, 10)  # Slightly larger divisors
            num1 = num2 * random.randint(1, 10)  # Ensure dividend ≤ 100
        problem = f"{num1} / {num2}"
        solution = num1 // num2  # Use integer division to ensure a whole number result
        
    elif operation == 5:  # Mixed operation
        operation = random.randint(1, 4)  # Randomly pick an operation
        return get_problem(operation, level)  # Recursively call with a random operation

    return problem, solution

        
def main():
    display_title()
    count = 0
    total = 0
    level = get_level_input()
    while True:
        display_options()
        option = get_user_input()
        if option == 6: # Exit the program
            break

        # Perform a set of five exercises
        for _ in range(5):
            prob, solution = get_problem(option, level)
            user_answer = get_user_solution(prob)
            if user_answer == solution:
                print("Oikein!")
                count+=1
                total+=1
            else:
                print(f"Väärin. Oikea vastaus on {solution}. ")
                total+=1

    # Summary
    print("-"*32)
    print("Moneen kysymykseen vastasin:", total)
    print("Monta oikeaa vastausta:", count)
    if total > 0:
        print(f"Oikeita vastauksia oli {round(count*100/total, 1)} %")
    print("Hienoa työtä!!")
    
main()
