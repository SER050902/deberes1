import csv

def menu():
    while True:
        print('\n1 TOTAL INFRACCIONS PENALS ')
        print('2 Mitjana de coacions total ')
        print('3 Lesiones se han cometido entre años incluidos ')
        print('4 El año con mas delitos')
        print('5 Orderna de forma mayor a menor de tortura e integridad moral en 3 años')
        print('6 El año con los datos iguales de igual delitos')
        print('7 Total faltas')
        print('0 Salir')
        opcion = -1
        while opcion not in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
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
            igual_delictes()
        elif opcion == 7:
            total_faltas()
        else:
            break


def Anys():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f,delimiter=',')
        line_count = 0
        total = 0
        num_nil = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                num_nil += 1
                total += int(line[1])
                print(num_nil,line[1])
    print('\nTotal:',total)



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
            if line_count == 1:
                num_coaccions += 1
                total_coaccions += int(line[7])

        mitjana_coaccions = total_coaccions / num_coaccions
        print("La media de coaccions es :", int(mitjana_coaccions))

def lesions():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f, delimiter=',')
        ano_inicio = int(input('Introduce el año inicio: '))
        ano_final = int(input('Introduce el año final del rango: '))
        if ano_final < ano_inicio:
            print('El año final tiene que ser mayor que año inicio')
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

    print('\t\nLesiones entre', ano_inicio, 'y', ano_final, ':', str(calcular), ', Rango de lesiones:',
          lesiones_rango)

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
        ano_1 = int(input('Intruduce el año primero'))
        ano_2 = int(input('Intruduce el año segundo'))
        ano_3 = int(input('Intruduce el año tercero'))

        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            ano = int(line[0])
            datos_Tortura_moral = int(line[8])
            if ano_1 == ano:
                ano_del_1 = datos_Tortura_moral
                datos_moral.append(datos_Tortura_moral)
                continue
            if ano_2 == ano:
                datos_moral.append(datos_Tortura_moral)
                ano_del_2 = datos_Tortura_moral
                continue
            if ano_3 == ano:
                ano_del_3 = datos_Tortura_moral
                datos_moral.append(datos_Tortura_moral)
            line_count += 1
    datos_moral.sort(reverse=True)

    print('\t\nTortura e integridad moral 3 años: ',ano_1,'=',ano_del_1,',',ano_2,'=',ano_del_2,',',ano_3,'=',ano_del_3)
    print('\nForma ordenado en mayor a menor:',str(datos_moral))
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


def total_faltas():
    with open('violencia genere.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        calcular_valor = []
        for line in reader:
            if line_count ==0:
                line_count += 1
                continue
            if line_count == 1:
                total_falta = int(line[16])
                if total_falta == 0:
                    calcular_valor.append(int(line[0]))

    print('Años de que no tienes valores: ',calcular_valor)

menu()