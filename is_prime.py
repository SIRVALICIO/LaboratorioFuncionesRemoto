def is_prime(n):
    cont=0
    primo=0
    while cont<=n:
        cont+=1
        if n % cont == 0:
            primo += 1

    return primo
contP=0
try:
    n=int(input("Valor a evaluar: "))
    is_prime(n)
    r=is_prime(n)

    if r>2:
        print("0")
    else:
     print("1")
     contP+=1
except Exception:
    print("-1")

c=input("quiere voler a intentarlo? y/n: ")
if c=="y":
       try:
        while c!="n":

            d = int(input("nueva base a: "))
            if d<=0:
                raise Exception("-1")

            if d <=0:

                break
            is_prime(d)
            s=is_prime(d)
            if s > 2:
                print("0")
            else:
                print("1")
                contP+=1


       except Exception:
           print("-1")

else:
    if c=="n":

        print("muchas gracias")

print("la cantida de primos fueron: ",contP)