def a_power_b(a,b):
    prod=1
    for i in range(0,b):
        prod=prod*a
        if i==b-1:
            print(prod)

    return  prod

a=int(input("Ingresar valor de la base: "))
b=int(input("valor de la potencia: "))

a_power_b(a,b)