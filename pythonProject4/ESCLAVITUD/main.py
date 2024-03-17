import csv

def menu():
    while True:
        print('\nCuál fue el comprador que más esclavos compró ')
        print('2 Mitjana de coacions total ')
        print('3 Lesiones se han cometido entre años incluidos ')
        print('4 El año con mas delitos')
        print('5 : ')
        print('6 :')
        print('7 :')
        print('0 Salir')
        opcion = -1
        while opcion not in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            opcion = int(input('Opción: '))
        if opcion == 1:
            max_exclavo()
        elif opcion == 2:
            prueba()
        elif opcion == 3:
            max_vendas()
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        else:
            break

def max_exclavo():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        max_exclavo = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                datos_compra = int(line[15])
                if datos_compra > max_exclavo:
                    max_exclavo = datos_compra
                    nom_cli = line[10]

    print('\nEl señor',nom_cli,'con mas de exclavo es', str(max_exclavo))


def max_vendas():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        max_exclavo = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                datos_compra = float(line[19])
                if datos_compra > max_exclavo:
                    max_exclavo = datos_compra
                    estado_origen = line[7]

    print('\nEl estado del origen ',estado_origen,'con mas de vendas es', str(max_exclavo))

def prueba():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        max_exclavo = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                datos_compra = line[2]
                print(datos_compra)
menu()