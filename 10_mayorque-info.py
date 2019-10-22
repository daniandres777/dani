'''definir un script, que tome tre
numeros ingresados por teclado como argumentos
y devuelva el mayor de ellos'''

x=int(input("ingreso primer numero"))
y=int(input("ingreso segundo numero"))
z=int(input("ingreso tercer numero"))
if x>y and x>z:
    print(x,"es maypor que",y,"y",z)
elif y>x and y>z:
    print(y,"es mayor que",x,"y",z)
else:
    print(z,"es mayor que",x,"y",y)
    
'''escribir un programa que pida al usuario su peso en kg y
la estatura en metros y calcule el imc y lo almacene en una variable
redondeado a dos decimales'''

q=float(input("Su peso es: "))
e=float(input("Su estatura es: "))
IMC=q/(e*e)
print("{:.2f}".format(IMC))

'''
crear un script que pida el ingreso al usuario por teclado el valor de la compra,
agregar el 12% de IVA, si la compra es a 200 USD asignar un 2% de descuento
mostrar el precio del IVA, el precio final del producto, el valor del ahorro y
total a pagar'''

x=float(input("valor compra"))
y=x*0.12
totals=x+y
if totals>=200:'''cuando hay descuento'''
    descuento=totals*0.02
    total=totals-descuento
    print("el total sin descuento:",totals,"\n total del IVA(12%)",y,"\n descuento aplicado:",descuento,"\n Total a pagar", total)
else:'''cuando no hay descuento'''
    print("el total a pagar:",totals,"\n total del IVA(12%)",y)
