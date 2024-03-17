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
            mayor_menor()
        elif opcion == 6:
            datos()
        elif opcion == 7:
            igual_delictes()
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
                sum += int(line[1])
                print(num_nil,line[1])
    print('\nTotal:',sum)



def coaccions():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        num_coaccions = 0
        total_coaccions = 0

        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            num_coaccions += 1
            total_coaccions += int(line[7])

        mitjana_coaccions = total_coaccions / num_coaccions
        print("La media de coaccions es :", int(mitjana_coaccions))

def lesions():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f, delimiter=',')
        ano_inicio = int(input('Introduce el año inicio: '))
        ano_final = int(input('Introduce el año final del rango: '))
        calcular = 0
        line_count = 0
        lesiones_rango = []
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            ano = int(line[0])
            if ano_inicio <= ano <= ano_final:
                calcular += 1
                lesiones_rango.append(int(line[4]))

    print('\t\nLesiones entre', ano_inicio, 'y', ano_final, ':', str(calcular), ', Rango de lesiones:', lesiones_rango)

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
        print("L'any amb més delictes (TOTAL DELICTES):", max_year)


def mayor_menor():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        datos_moral = []
        calcular = 0
        ano_inicio = int(input('Introduce el año inicio: '))
        ano_final = int(input('Introduce el año final del rango: '))
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            ano = int(line[0])
            if ano_inicio <= ano <= ano_final:
                calcular += 1
                datos_moral.append(int(line[8]))
            line_count += 1

    datos_moral.sort(reverse=True)

    print('\t\nLesiones entre', ano_inicio, 'y', ano_final, ':', str(calcular), ', Lesiones de mayor a menor:', datos_moral)

def igual_delictes():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        igual = []
        for line in reader:
            if line_count ==0:
                line_count += 1
                continue
            if line_count == 1:
                total_penals = int(line[1])
                total_delictes = int(line[2])
                if total_penals == total_delictes:
                    igual.append(int(line[0]))

    print('Años de igual de total infracciones penales y delictos: ',igual)




def datos():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f,delimiter=',')
        num_linea = 0
        for line in reader:
            num_linea += 1
            print(str(num_linea),line)

def prueba():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f,delimiter=',')
        line_count = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line[1]:
                toso = int(line[1])
                print(toso)



menu()