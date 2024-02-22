# ------------ EJERCICIOS CORRESPONDIENTES A LA SECCION 1

#1 Verificar si un numero es par o impar (Usar un input).
''' Esto es un bloque comentado
msg = input("ingresa un numero\n")

print(msg)

if int(msg) % 2 == 0:
    print(f"{msg} es un numero par")
else:
    print( f"{msg}  Es un numero impar")
    
'''

#2 Clasificar una persona en una categoria de edad. Por ejemplo: Si es un nino, si es un adolescente o si es una persona adulta

'''
msg2 = input("Ingrese su edad\n")

if int(msg2) < 10:
    print("Eres un niño")
elif int(msg2) < 18:
    print("Eres un Adolescente")
else:
    print("Eres un adulto")

''' 

#3 Evaluar la nota e imprimir el resultado: Por ejemplo: Se recibe una nota con un input (20), y le decimos que letra fue su calificacion (A,B,C,D,E,F)

'''
msg3 = input ("Ingrese nota para saber su calificacion en letra\n")

nota = int(msg3)

if nota <= 3:
     print("Tu nota en letra es F")
elif nota <= 7:
    print("Tu nota en letra es E")
elif nota <= 10 :
    print("Tu nota en letra es D")
elif nota <= 14:
    print("Tu nota en letra es C")
elif nota <= 17:
    print("Tu nota en letra es B")
else:
    print("Tu nota en letra es A")
    
'''

#4 Calcular el descuento en una tienda si el monto supera los 100$ aplicar un 10% de descuento. Por ejemplo: se recibe un numero (el monto de la compra) Usar input.
'''
msg4 = input("Monto de la compra\n")

valor = int(msg4)

if valor <= 100:
    print(f'{msg4} Gracias por su compra')
elif valor > 100: 
    subtotal = valor*0.1
    total = valor - subtotal
    print(f'Por ser la comprar mayor a 100$ tiene un descuento 10% para un monto total de {total}')
'''

#5 Determinar el tipo de triangulo en base a sus lados (EQuilatero, Isosceles o Escaleno) Usar 3 input.
'''
lado1 = input("Ingrese medida Lado 1\n")
lado2 = input("Ingrese medida Lado 2\n")
lado3 = input("Ingrese medida Lado 3\n")

if lado1 == lado2 and lado2 == lado3:
    print("Es un triangulo equilatero")
elif lado1 == lado2 and lado2 != lado3:
    print("Es un triangulo isosceles")
else:
    print("Es un triangulo escaleno")
 '''
#6 Convertir una cantidad de dolares a bolivares o viceversa (usar input)

monto = input("introduzca monto. (tasa BCV = 3.62)\n")

moneda = input("Especifique que moneda es $ o Bs \n")

monedaT = moneda.lower()

if moneda == "$":
    total1 = int(monto)* 36.23
    redon = round(total1,2)
    print(f' Su monto en Bs es {redon}')
elif moneda == "bs":
    Total = int(monto)/36.23
    redon1 =round(Total,2)
    print(f'Su monto en $ es {redon1}')
    
    
    
  






