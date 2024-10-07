entrada = input('Digite um Número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Ímpar!'
    
    if par_impar:
        par_impar_texto = 'Par!'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro!')