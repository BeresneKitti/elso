def negyszog(x, y):
    ker = 2 * x + 2 * y
    ter = x * y
    if x==y:
        alakzat = "négyzet"
    else:
        alakzat = "téglalap"
    return ker, ter, alakzat

if __name__ == '__main__':
    a = 4
    b = 4
    eredmeny = negyszog(a, b)
    print (f"A {eredmeny[2]} kerület =", eredmeny[0])
    print (f"A {eredmeny[2]} terület =", eredmeny[1])
    print("Saját hívás!")
