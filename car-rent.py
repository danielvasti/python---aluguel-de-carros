cars = [
    "Toyota Corolla - R$ 100 por dia",
    "Honda Civic - R$ 120 por dia",
    "Ford Focus - R$ 110 por dia",
    "Chevrolet Malibu - R$ 130 por dia",
    "Nissan Altima - R$ 115 por dia",
    "Hyundai Elantra - R$ 105 por dia",
    "Volkswagen Jetta - R$ 125 por dia",
    "BMW 3 Series - R$ 200 por dia",
    "Audi A4 - R$ 220 por dia",
    "Mercedes-Benz C-Class - R$ 250 por dia"
]

prices = {
    "Toyota Corolla": 100,
    "Honda Civic": 120,
    "Ford Focus": 110,
    "Chevrolet Malibu": 130,
    "Nissan Altima": 115,
    "Hyundai Elantra": 105,
    "Volkswagen Jetta": 125,
    "BMW 3 Series": 200,
    "Audi A4": 220,
    "Mercedes-Benz C-Class": 250
}

rented_cars = []

while True:
    print('---------------\nBem vindo à locadora de carros! \nO que você deseja fazer?')
    print('1 - Alugar um carro')
    print('2 - Devolver um carro')
    print('3 - Verificar carros disponíveis')
    print('4 - Sair')	

    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        while True:
            print("Lista de carros disponíveis para aluguel:")
            for index, car in enumerate(cars, start=1):
                print(f"{index}. {car}")
            carro_escolhido = input('Digite o número do carro que deseja alugar: ')
            if not carro_escolhido.isdigit() or int(carro_escolhido) < 1 or int(carro_escolhido) > len(cars):
                print("Opção inválida! Tente novamente.")
                continue
            dias = int(input('Por quantos dias você deseja alugar o carro? '))
            car_name = cars[int(carro_escolhido)-1].split(" - ")[0]
            total_price = prices[car_name] * dias
            print(f"Você alugou o carro {car_name} por {dias} dias. O preço total é R$ {total_price}.")
            rented_cars.append(cars.pop(int(carro_escolhido)-1))
            if not cars:
                print("Todos os carros foram alugados.")
                break
            continuar = input('Deseja alugar outro carro? (s/n): ')
            if continuar.lower() != 's':    
                print('Obrigado por usar nossos serviços!')
                break

    elif opcao == '2':
        if not rented_cars:
            print("Nenhum carro para devolver no momento.")
        else:
            print("Lista de carros alugados:")
            for index, car in enumerate(rented_cars, start=1):
                print(f"{index}. {car}")
            carro_devolvido = input('Digite o número do carro que deseja devolver: ')
            if not carro_devolvido.isdigit() or int(carro_devolvido) < 1 or int(carro_devolvido) > len(rented_cars):
                print("Opção inválida! Tente novamente.")
                continue
            devolvido = rented_cars.pop(int(carro_devolvido)-1)
            cars.append(devolvido)
            print(f"Você devolveu o carro: {devolvido}.")

    elif opcao == '3':
        if not cars:
            print("Nenhum carro disponível para aluguel no momento.")
        else:
            print("Carros disponíveis para aluguel:")
            for car in cars:
                print(car)

    elif opcao == '4':
        print('Obrigado por usar nossos serviços! Até a próxima.')
        break

    else:
        print("Opção inválida! Tente novamente.")
