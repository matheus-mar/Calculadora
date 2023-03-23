print("Bem vindo(a) a calculadora!")


operacao = input("Insira a sua operação: ")

operacao = [*operacao]
i = 0

while(i != len(operacao)):
    if operacao[i] == "+":
        num1 = float(''.join(operacao[:i]))
        num2 = float(''.join(operacao[i+1:]))

        realizarOperacao = num1 + num2
        print("{} + {} = {}" .format(num1, num2, realizarOperacao))
        break

    elif operacao[i] == "-":
        num1 = float(''.join(operacao[:i]))
        num2 = float(''.join(operacao[i+1:]))

        realizarOperacao = num1 - num2
        print("{} - {} = {}" .format(num1, num2, realizarOperacao))
        break

    elif operacao[i] == "/":
        num1 = float(''.join(operacao[:i]))
        num2 = float(''.join(operacao[i+1:]))

        realizarOperacao = num1 / num2
        print("{} / {} = {}" .format(num1, num2, realizarOperacao))
        break

    elif operacao[i] == "*":
        num1 = float(''.join(operacao[:i]))
        num2 = float(''.join(operacao[i+1:]))

        realizarOperacao = num1 * num2
        print("{} * {} = {}" .format(num1, num2, realizarOperacao))
        break

    else:
        i += 1