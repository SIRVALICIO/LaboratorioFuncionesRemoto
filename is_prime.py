def is_prime(n):
    cont=0
    primo=0
    while cont<=n:
        cont+=1
        if n % cont == 0:
            primo += 1
    return primo
try:
    n=int(input("Valor a evaluar: "))
    is_prime(n)
    r=is_prime(n)

    if r>2:
        print("0")
    else:
     print("1")
except Exception:
    print("-1")