import math
def main():
    #escribe tu código abajo de esta línea
    altc=float(input(""))
    angl=float(input(""))
    from math import sin, ceil
    lare=ceil((altc/(sin(angl))))
    print(lare)

if __name__ == '__main__':
    main()
