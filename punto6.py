#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
#coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = int(input("ingrese las horas trabajadas"))
costo = int(input("ingrese el costo por las horas trabajadas"))
paga = horas * costo
print(f"su pago del trabajo es: ${paga} dolares")