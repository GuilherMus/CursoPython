soma = 0
qtd = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    soma += idade
    qtd += 1
if qtd > 0:
    media = soma / qtd
    print(f'{media:.2f}')