#Question2 factorise prime numbers

Numfact=2
Primefact=[]
Testvar=10

while Testvar > 1:
    if Testvar % numfact == 0:
    primefact.append(numfact)
    testvar=tesvar//numfact
else:
    numfact+=1
    print("Divisor:",numfact)
    print(primefact)