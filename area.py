mensaje = input('Si quiere calcular el área de un triángulo ingrese T o t. Para la de un círculo C o c: ').upper()

if mensaje == 'T':
    base = float(input('ingrese la medida de la base del triángulo: '))
    altura = float(input('ingrese la medida de la altura del triángulo: '))

    area_t = (base * altura)/2

    print(f'El área del triángulo es: {area_t}')
elif mensaje == 'C':
    radio = float(input('ingrese el radio del cículo: '))

    area_c = 3.1416 * (radio ** 2)
    print(f'El área del círculo es: {area_c}')
else:
    print('Opción no valida')
