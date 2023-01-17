import random

if __name__ == '__main__':
    def mathOperations(number1, number2, operation):
        if operation == "+":
            result = number1 + number2

        elif operation == "-":
            result = number1 - number2

        elif operation == "*":
            result = number1 * number2

        elif operation == "/":
            result = number1 / number2

        return result


    def rounded(number):
        return '{0:.2f}'.format(number)


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
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        operation = random.choice(operations)
        right_answer = mathOperations(number1, number2, operation)
        print(f"{number1} {operation} {number2} = ?")
        user_answer = input('Твой ответ (q - для выхода): ')
        if user_answer == 'q':
            break
        elif rounded(right_answer) == rounded(float(user_answer)):
            score = scoreMaster(True, score)
            print(f"Правильно! У тебя {score} очков")
        else:
            score = scoreMaster(False, score)
            print(f'Неправильно! {number1} {operation} {number2} = {rounded(right_answer)}. У тебя, {score} очков')
            game = gameMaster(score)
