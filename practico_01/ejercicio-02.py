# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.




def mayor(a,b,c):
    
    if a > b and a > c:
        return a

    if b > c and b > a:
        return b

    if c > b and c > a:
        return c

assert mayor(2, 5, 7) == 7


