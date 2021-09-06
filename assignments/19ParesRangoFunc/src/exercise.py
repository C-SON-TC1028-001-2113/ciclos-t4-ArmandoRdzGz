
def main():
    n1 = int(input('Valor 1: ')) 
    n2 = int(input('Valor 2: '))

    if n1>0 and n2>0 :
        if n1!=n2:
            if n1>n2:
                for numero in range(n2, n1+1):
                    if numero%2==0 :
                        print(numero)
            elif n2>n1 :
                for numero in range(n1, n2+1):
                    if numero%2==0 :
                        print(numero)
        else:
            print('No hay pares')

if __name__=='__main__':
    main()
