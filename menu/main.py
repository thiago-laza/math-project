def menu():
    titulo = '\033[92mMATH - PROJECT - Thiago Cavalcanti Azevedo\033[0m'
    largura = 160
    titulo_centralizado = titulo.center(largura)
    print('-=' * 80)
    print(titulo_centralizado)
    print('-=' * 80)

    while True:
        area_matematica = input('ESCOLHA A AREA:\n\033[92mAritmetica\033[0m\033[93m[1]\033[0m\n\033'
          '[92mGeometria\033[0m\033[93m[2]\033[0m\n\033[92mGrandezas e Medidas\033'
          '[0m\033[93m[3]\033[0m''\n\033[92mAlgebra\033[0m\033[93m[4]\033[0m\n\033'
          '[92mEstatistica e Probabilidade\033[0m\033[93m[5]\033[0m\n\033[93mOpcao:\033[0m ')
        if area_matematica not in '12345':
            print('\033[38;5;208mOPCAO INVALIDA!\033[0m')
            area_matematica = input('ESCOLHA A AREA:\n\033[92mAritmetica\033[0m\033[93m[1]\033[0m\n\033'
          '[92mGeometria\033[0m\033[93m[2]\033[0m\n\033[92mGrandezas e Medidas\033'
          '[0m\033[93m[3]\033[0m''\n\033[92mAlgebra\033[0m\033[93m[4]\033[0m\n\033'
          '[92mEstatistica e Probabilidade\033[0m\033[93m[5]\033[0m\n\033[93mOpcao:\033[0m ')
        else:
            if area_matematica == '1':
                from aritmetica import menu_aritmetica
                menu_aritmetica.aritmetica()
menu()


