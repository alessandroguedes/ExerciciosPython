import math

angulo = float(input("Digite o angulo que você deseja: "))
#converter o ângulo de graus para radianos (math.radianus) 
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tag = math.tan(math.radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}'.format(angulo, sen))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tag))