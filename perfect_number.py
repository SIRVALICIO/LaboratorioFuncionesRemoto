def perfect_number(n):
    a=0
    for i in range(1,n):
        if(n%i==0):
            a+=i
    if (a==n):
        print("El numero es perfecto")
    else:
        print("El numero no es perfecto")

n=int(input("Numero a evaluar_: "))
perfect_number(n)
