import os
import time
import random


trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos_aleatorios = random.randint(300000,2500000)
trabajadores_sueldo = sueldos_aleatorios
salud = trabajadores_sueldo * 0.07
afp = trabajadores_sueldo * 0.12
trabajadores_sueldo = trabajadores_sueldo - (salud + afp)
def limpiezaPantalla():
    os.system("cls")

def menu ():
    print ("1. Asignar sueldos aleatorios")
    print ("2. Clasificar sueldos")
    print ("3. Ver estadísticas.")
    print ("4. Reporte de sueldos")
    print ("5. Salir del programa")
    print(input("Ingresa una opcion del 1 al 5 "))

    opcion = 0
    while True:
        if opcion == 1:
            print("Asignar sueldos aleatorios ")
        elif opcion == 2:
            print("Clasificar Sueldos ")
        elif opcion == 3:
            print("Ver estadisticas ")
        elif opcion == 4:
            print("Reporte de sueldos ")
        else:
            print("Salir del Programa")
            break
menu()     
def asignar():
    print("Asignacion de Sueldos")
for i in trabajadores:
    print(trabajadores)
asignar()
    
def reporte_sueldos():
    print(f"El sueldo sera para Juan Perez es: ",trabajadores_sueldo)
    print(f"El sueldo sera Maria Garcia es: ",trabajadores_sueldo)
    print(f"El sueldo sera Carlos Lopez es: ",trabajadores_sueldo)
    print(f"El sueldo sera Ana Martinez es: ",trabajadores_sueldo)
    print(f"El sueldo sera Pedro Rodriguez es: ",trabajadores_sueldo)
    print(f"El sueldo sera Laura Hernandez es: ",trabajadores_sueldo)
    print(f"El sueldo sera Miguel Sanchez es: ",trabajadores_sueldo)
    print(f"El sueldo sera Isabel Gomez es: ",trabajadores_sueldo)
    print(f"El sueldo sera Francisco Diaz es: ",trabajadores_sueldo)
    print(f"El sueldo sera Elena Hernadez es: ",trabajadores_sueldo)
reporte_sueldos()
    

    