import random


def number_choice(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def operation_choice():
    return random.choice(['+', '-', '*'])


def selecting_operation(number1, number2, operation):
    p = f"{number1} {operation} {number2}"
    if operation == '+': a = number1 +number2
    elif operation == '-': a = number1 - number2
    else: a = number1 * number2
    return p, a

def math_quiz():
    s = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = number_choice(1, 10); number2 = number_choice(1, 5); o = operation_choice()

        PROBLEM, ANSWER = selecting_operation(number1, number2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
