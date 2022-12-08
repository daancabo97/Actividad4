# 6.

# Mistura S.A. es una empresa dedicada a la comercialización de dulces a nivel nacional. Después de una minuciosa evaluación,
# la empresa ha decidido asignarle la tarea de desarrollar un programa que permita gestionar las ventas de dulces. Se le pide 
# ingresar la siguiente información: cantidad de dulces a comprar, el tipo de dulce (1, 2 o 3) y muestre como salida, el tipo 
# de dulce, el precio unitario, la cantidad y el monto de la venta, teniendo en cuenta la siguiente política de descuento.


tipo = int(input(f'ingrese el tipo de dulce ( 1  2  3 ) : '))
cant = int(input(f'Ingrese la cantidad de dulces a comprar : '))
print(f'Usted adquirio {cant} dulces')


if tipo == 1:
    precio = 3
    montoDinero = precio * cant
    if cant <= 5:
       montoDinero = montoDinero - 0.5
       print(montoDinero)
    elif cant <= 10:
       montoDinero = montoDinero * .93
       print(montoDinero)
elif tipo == 2:
     precio = 4
     montoDinero = precio * cant
     print(montoDinero)
     if cant > 7:
        montoDinero = montoDinero
        print(montoDinero)
     else:
         montoDinero = montoDinero * .95    
         print(montoDinero)
elif tipo == 3:
     precio = 5
     montoDinero = precio * cant
     print(montoDinero)
     if cant > 4:
       montoDinero = montoDinero * .85
       print(montoDinero)

print(tipo)
print("")    
    
print("Tipo de dulce:", tipo)
print("Precio Unitario:", precio)
print("Cantidad de dulces:", cant)
print(f"dinero de la venta:, $ {montoDinero} pesos")
