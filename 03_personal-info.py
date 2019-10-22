x= input("¿cual es tu primer nombre?: ")
y= input("¿cual es tu apellido?: ")
z= input("¿cual es tu edad?: ")
w= input("¿donde vive?: ")
print(f"hola su primer nombre es: {x}, su apellido es: {y}, su edad: {z} años, vive en: {w}.gracias por su atencion")
if x > str(18):
    print("mayor edad")
else:
    print("menor edad")
