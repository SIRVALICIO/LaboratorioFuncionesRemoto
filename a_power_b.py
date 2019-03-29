
def a_power_b(a,b):

        prod=1

        for i in range(0,b):
            prod=prod*a
            if i>1000:
                raise Exception("El rango no es admitido  para la potencia")
        return  prod





try:
    a=int(input("Ingresar valor de la base a: "))
    b=int(input("valor de la potencia b: "))
    a_power_b(a, b)
    r= a_power_b(a, b)
    print(r)

except Exception:
    print("error al digitar")



c=input("quiere voler a intentarlo? y/n: ")
if c=="y":
       try:
        while c!="n":

            d = int(input("nueva base a: "))
            e = int(input("nueva potencia b: "))
            if d == 0:
                break



            a_power_b(d,e)
            d=a_power_b(d,e)
            print(d)
            if d==0 :
                print("muchas gracias")
       except Exception:
           print("Error al digitar")
else:
    if c=="n":

        print("muchas gracias")



