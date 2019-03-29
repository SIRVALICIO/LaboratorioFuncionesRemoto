def a_power_b(a,b):
    prod=1
    for i in range(0,b):
        prod=prod*a
        if i==b-1:
            print(prod)

    return  prod

a=int(input("Ingresar valor de la base a: "))
b=int(input("valor de la potencia b: "))

a_power_b(a,b)


c=input("quiere voler a intentarlo? y/n: ")
if c=="y":
    while c!="n":
        d = int(input("nueva base a: "))
        e = int(input("nueva potencia b: "))
        if d == 0:
            break
        


        a_power_b(d,e)

        if d==0 :
            print("muchas gracias")

else:
    if c=="n":

        print("muchas gracias")



