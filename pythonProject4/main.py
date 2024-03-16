import csv

def menu():
    while True:
        print('\n1 TOTAL INFRACCIONS PENALS: ')
        print('2 Mitjana de coacions total: ')
        print('3 Promedio de : ')
        print('4 : ')
        print('5 : ')
        print('6 :')
        print('7 :')
        print('0 Salir')
        opcion = -1
        while opcion not in [1, 2, 3, 4, 5, 6, 7, 0]:
            opcion = int(input('Opción: '))
        if opcion == 1:
            Anys()
        elif opcion == 2:
            coaccions()
        elif opcion == 3:
            lesions()
        elif opcion == 4:
            delictes()
        elif opcion == 5:
            pass
        elif opcion == 6:
            datos()
        elif opcion == 7:
            pass
        else:
            break


def Anys():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f,delimiter=',')
        line_count = 0
        sum = 0
        num_nil = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                num_nil += 1
                sum += float(line[1])
                print(num_nil,line[1])
    print('\nTotal:',sum)

def coaccions2():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)
        values = [int(float(line[7])) for line in reader]
        media = sum(values) / len(values)
        print('Media:', media)

def coaccions():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f, delimiter=',')
        valor = []
        line_count = 0
        num_lie = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line[7] == 1:
                num_lie += 1
                valor = [int(float(line[7]))]
                valor.append(valor)
            media = sum(valor) / len(valor)
    print('Media:',media)

def lesions():
    with open('violencia genere.csv') as f:
        reader = csv.DictReader(f)
        ano_inicio = int(input('Introduce el año inicio: '))
        ano_final = int(input('Introduce el año final del rango: '))
        calcular = 0
        for line in reader:
            ano = int(line['Anys'])
            if ano_inicio <= ano <= ano_final:
                calcular += 1

    print('\t\nLesiones entre', ano_inicio, 'y', ano_final, ':', str(calcular))


def delictes():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        max_delictes = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line[2]:
                print(str(line_count),line[0],line[2])
                total_delictes = int(line[2])
                if total_delictes > max_delictes:
                    max_delictes = total_delictes
                    max_year = line[0]
            line_count += 1
        print("L'any amb més delictes (TOTAL DELICTES):", max_year)



def datos():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f,delimiter=',')
        num_linea = 0
        for line in reader:
            num_linea += 1
            print(str(num_linea),line)

menu()