preco = float (input('Qual o valor do produto? R$ '))
novo = preco - (preco * 5 / 100)
d = 5  #Aqui eu informo a % do desconto
print(f' O valor do produto R$ {preco :.2f}, Com desconto de {d} % passou a custar: R$ {novo :.2f} ')