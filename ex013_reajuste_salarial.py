salario = float(input('Qual é o salario do Funcionário? R$ '))
novo_salario = salario + salario*15/100
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento'. format(salario))
print('passa a receber R$ {:.2f} '.format(novo_salario))