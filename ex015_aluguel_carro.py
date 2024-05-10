dias = int(input('Qual a quantidade de dias foi alugado? '))
km = float(input('Quantos km foi rodado? '))
preco = 60*dias + 0.15*km
print('O preço total a pagar é R$ {:2f}'.format(preco))