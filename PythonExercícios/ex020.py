from random import shuffle
nome1 = input('1° Digite um nome: ')
nome2 = input('2º Digite um nome: ')
nome3 = input('3° Digite um nome: ')
nome4 = input('4° Digite um nome: ')
nomes = [nome1, nome2, nome3, nome4]
shuffle(nomes)
nomes_aleatorios = ', '.join(nomes)
print(f'A ordem de apresentação será: {nomes_aleatorios}!')
