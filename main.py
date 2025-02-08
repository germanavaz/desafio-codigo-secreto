# Missão 1: Restaurando as Regras Escolares 📝
# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 5) ou reprovado (nota menor ou igual à 5).

print('Digite sua nota:')
nota = input()
nota = float(nota)

if nota >= 5:
    print('Parabéns, você foi aprovado!')
else:
    print('Você foi reprovado ):')


# Missão 2: O Sistema Eleitoral Secreto 📝
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

print('Quantos anos você tem?')
idade = int(input())

if idade > 16:
    print('Você pode votar!')
else:
    print('Você ainda não tem idade para votar.')

# Missão 3: Recuperando o Sistema de Notas 📊
# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

print('Digite sua nota (0-100):')
nota = int(input())

if nota >= 90:
    print("Parabéns, você tirou A!")
elif nota >= 80 and nota < 90:
    print("Muito bem, você tirou B.")
elif nota >= 70 and nota < 80:
    print("Muito bem, você tirou C.")
elif nota >= 60 and nota < 70:
    print("Muito bem, você tirou D.")
else:
    print('Estude um pouco mais, você tirou F.')


# Missão 4: Restaurando a Identificação de Números ⚖️
# Os robôs da escola precisam identificar padrões numéricos para resolver cálculos e otimizar os sistemas. No entanto, o vírus bagunçou os algoritmos e agora eles não conseguem mais somar corretamente!
# Crie um programa que peça dois números ao usuário e exiba a soma deles.

print('Digite o primeiro número:')
num1 = int(input())
print('Digite o segundo número:')
num2 = int(input())


def soma_dois_num(numero1, numero2):
    return numero1 + numero2


soma = soma_dois_num(num1, num2)
print(f"A soma dos dois números é {soma}")

# Missão 5: Recuperando o Cofre de Segurança 🔒
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.
# Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

print('Digite a senha:')
senha = str(input())

if senha == 'Python123':
    print('A senha está correta!')
else:
    print('A senha está errada.')

# Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
# O vírus está comprometendo o sistema de segurança e a contagem de registros! Para restaurar o funcionamento correto, você precisa reforçar as verificações e garantir que os dados sejam processados corretamente.
#   Exiba os números de 1 a 10 usando um loop while.

contagem = 1

while contagem < 11:
    print(contagem)
    contagem += 1

# Missão 7: Organizando a Lista📋
# Os números estão misturados e precisam ser organizados!
# Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente. Isso ajudará a colocar tudo em ordem corretamente!

lista_de_numeros = [8, 3, 10, 1, 5]
lista_de_numeros.sort()
print(lista_de_numeros)

# Missão 8: Acessando os Registros de Alunos 🏷️
# O sistema de alunos está desordenado! Para acessar as informações corretamente, você precisa organizar os dados.
# Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.
# Missão 9: Calculando Dobro de um Número 🛠️
# Os alunos precisam de um programa que ajude em cálculos rápidos.
# Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
# ➡️ Exemplo: dobro(5)
# ➡️ Saída: "O dobro de 5 é 10"
# Missão 10: Contando Letras 🔄
# O sistema precisa contar quantas letras há em um nome.
# ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
# ➡️ Exemplo: contar_letras("Ana")
# ➡️ Saída:" O nome Ana tem 3 letras"
