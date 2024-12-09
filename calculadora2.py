def calculator():
    while True:
        print("Selecione a operação desejada:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        choice = input("Entre sua escolha (1/2/3/4/5): ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Entre o primeiro número: "))
            num2 = float(input("Entre o segundo número: "))
            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)
            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)
            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)
            else:
                print(num1, "/", num2, "=", num1 / num2)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")