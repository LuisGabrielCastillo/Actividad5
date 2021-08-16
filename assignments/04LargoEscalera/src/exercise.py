import math
def main():
    #escribe tu código abajo de esta línea
    alto=int(input())
    ang=int(input())
    largo= alto/math.sin(ang)
    print(math.ceil(largo))



if __name__ == '__main__':
    main()
