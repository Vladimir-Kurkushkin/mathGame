import random, math

if __name__ == '__main__':

    def mathOperations(number1, number2, operation):
        if operation == "+":
            return number1 + number2

        elif operation == "-":
            return number1 - number2

        elif operation == "*":
            return number1 * number2

        elif operation == "/":
            if number1 == number2 or number1 == 1 or number2 == 1:
                return round(math.floor((number1 / number2) * 100) / 100)
            else:
                return math.floor((number1 / number2) * 100) / 100


    def scoreMaster(state: bool, var):
        if state:
            var += 10
            return var
        elif not state:
            var -= 10
            return var


    def gameMaster(var):
        if var < 0:
            print("У тебя закончились очки. Ты проиграл.")
            return False
        else:
            return True


    score = 0  # Общий счет игры
    operations = ["+", "-", "*", "/"]
    game = True  # Переменная контроля цикла

    while game:
        rand_num1 = random.randint(1, 10)
        rand_num2 = random.randint(1, 10)
        rand_operation = random.choice(operations)
        right_answer = str(mathOperations(rand_num1, rand_num2, rand_operation))
        print(f"{rand_num1} {rand_operation} {rand_num2} = ?")
        user_answer = input('Твой ответ (q - для выхода): ')
        if user_answer == 'q':
            break
        elif right_answer == user_answer:
            score = scoreMaster(True, score)
            print(f"Правильно! У тебя {score} очков")
        else:
            score = scoreMaster(False, score)
            print(f'Неправильно! {rand_num1} {rand_operation} {rand_num2} = {right_answer}. У тебя, {score} очков')
            game = gameMaster(score)