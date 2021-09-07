
def main():
    #escribe tu código abajo de esta línea
    height = int(input("Enter triangle height: "))
    if height > 0:
        for i in range(1, height+1):
            print(' '*(height-i)+ '*'*i)

if __name__=='__main__':
    main()
