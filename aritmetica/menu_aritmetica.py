def aritmetica():
    titulo = '\033[92mMATH - PROJECT - Thiago Cavalcanti Azevedo\033[0m'
    largura = 160
    titulo_centralizado = titulo.center(largura)
    sub_titulo = '\033[92mARITMETICA\033[0m'
    largura = 160
    sub_titulo_centralizado = sub_titulo.center(largura)
    print('-=' * 80)
    print(titulo_centralizado)
    print(sub_titulo_centralizado)
    print('-=' * 80)

    while True:
        area_matematica = input('ESCOLHA O TEMA:\n\033[92mMultiplos\033[0m\033[93m[1]\033[0m\n\033'
                                '[92mDivisores\033[0m\033[93m[2]\033[0m\n\033[92mTabuada\033'
                                '[0m\033[93m[3]\033[0m''\n\033[92mNumeros Primos\033[0m\033[93m[4]\033[0m\n\033'
                                '[92mPorcentagem\033[0m\033[93m[5]\033[0m'
                                '\n\033[92mMenu\033[0m\033[93m[6]\033[0m\n\033[93mOpcao:\033[0m')
        if area_matematica not in '123456':
            print('\033[38;5;208mOPCAO INVALIDA!\033[0m')
            area_matematica = input('ESCOLHA O TEMA:\n\033[92mMultiplos\033[0m\033[93m[1]\033[0m\n\033'
                                '[92mDivisores\033[0m\033[93m[2]\033[0m\n\033[92mTabuada\033'
                                '[0m\033[93m[3]\033[0m''\n\033[92mNumeros Primos\033[0m\033[93m[4]\033[0m\n\033'
                                '[92mPorcentagem\033[0m\033[93m[5]\033[0m\n\033[93mOpcao: \033[0m')
        elif area_matematica == '6':
            from menu.main import menu
            menu()
        elif area_matematica == '1':
            from aritmetica import multiplos
            multiplos()






