def multiplo():
    numero = int(input('Digite um numero para obter seus multiplos: '))
    print(f'Os 10 primeiros multiplos de {numero} sao:')
    for i in range(1,11):
        produto = i * numero
        print(f'{produto}',end=' ')


multiplo()
print()
from aritmetica.menu_aritmetica import aritmetica
aritmetica()