import csv

def menu():
    while True:
        print('\n1 Cuál fue el comprador que más esclavos compró ')
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
            max_vendas()
        elif opcion == 3:
            ano_promedio()
        elif opcion == 4:
            calcular_por_genero()
        elif opcion == 5:
            promedio_venta()
        elif opcion == 6:
            encontrar_comprador()
        elif opcion == 7:
            media_genero()
        elif opcion == 8:
            dos_ano_venta()
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
                    comprador = line[1]

    print('\nEl señor',comprador,'con',str(max_exclavo),'de exclavo ha comprado' )


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

def ano_promedio():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        num_esclavo = 0
        total_esclavo = 0

        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                sexo = line[9]
                ano = float(line[8])
                if sexo == 'F':
                    if ano < 18 and ano > 1:
                        num_esclavo += 1
                        total_esclavo += float(line[8])

        promedio = total_esclavo / num_esclavo
        print('El promedieo',promedio)

def calcular_por_genero():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        hombre = 0
        mujer = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                sexo = line[9]
                if sexo == 'M':
                    hombre += 1
                if sexo == 'F':
                    mujer += 1

        print('Hay',str(hombre),'hombres y',mujer,'mujeres')

def promedio_venta():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        num_compra = 0
        total_compra = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                num_compra += 1
                total_compra += float(line[19])

            media = total_compra / num_compra
        print('Media del venta',media)

def encontrar_comprador():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        encontrar_comprador2()
        buscar_comprador = input('Ingrese el nombre:')
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                line_nom_comprador = line[1]
            if line_nom_comprador == buscar_comprador:
                nombre = line_nom_comprador
                num_exclavo = int(line[15])

        print('El señor',nombre,'ha comprado',str(num_exclavo),'exclavos')

def encontrar_comprador2():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue

            if line_count == 1:
                nom_comprador = line[1]
                print(nom_comprador)


def media_genero():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        cantidad_hombre = 0
        cantidad_mujer = 0
        hombre = 0
        mujer = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue

            sexo = line[9]
            cantidad = float(line[8])

            if sexo == 'M':
                hombre += 1
                cantidad_hombre += cantidad
            elif sexo == 'F':
                mujer += 1
                cantidad_mujer += cantidad

        medias_hombres = cantidad_hombre/hombre
        medias_mujer = cantidad_mujer/mujer
        print('Media de hombres:',medias_hombres,'media de mujeres:',medias_mujer)


def dos_ano_venta():
    with open('slavery.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        ano_primero = int(input('Introduce primer año:'))
        ano_final = int(input('Introduce final año:'))
        calcular = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count ==1:
                cojer_ano = line[12].split('/')[2]
                if ano_primero <= cojer_ano <= ano_final:
                    calcular += 1

        print(calcular)




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