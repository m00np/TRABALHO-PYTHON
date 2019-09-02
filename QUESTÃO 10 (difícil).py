n1= float(input('Digite sua primeira nota: '))
n2= float(input('Digite sua segunda nota: '))
media= (n1 + n2)/2
if media >=7:
    print('APROVADO')
if media <=7:
    print('RECUPERAÇÃO')
recuperação= float(input('Digite a nota da recuperação: '))
if (media + recuperação)/2 >=5:
    print('APROVADO APÓS RECUPERAÇÃO')
if recuperação <=5:
    print('REPROVADO')
