"""
Sistema Acadêmico - Desafio
Arquivo: sistema_academico.py
Descrição: Sistema para cadastro de estudante, disciplinas, notas e resultado final.
Atende aos requisitos exigidos pelo desafio.
"""

# -------------------------------
# CADASTRO DO ESTUDANTE
# -------------------------------

print("=== Sistema Acadêmico TIPI ===")

# 5 dados principais do estudante
nome = input("Digite o nome do estudante: ")
id_estudante = input("Digite o ID do estudante: ")
curso = input("Digite o nome do curso: ")
idade = int(input("Digite a idade: "))
periodo = input("Digite o período atual: ")

# -------------------------------
# CADASTRO DAS DISCIPLINAS
# -------------------------------

disciplinas = []
print("\nCadastre 5 disciplinas:")

contador = 0
while contador < 5:  # Comando de repetição WHILE
    disciplina = input(f"Digite o nome da disciplina {contador + 1}: ")
    disciplinas.append(disciplina)
    contador += 1

# -------------------------------
# CADASTRO DAS NOTAS
# -------------------------------

notas = []
print("\nDigite a nota final de cada disciplina (0 a 10):")

for materia in disciplinas:
    nota = float(input(f"Nota em {materia}: "))
    notas.append(nota)

# -------------------------------
# SITUAÇÃO DE CADA DISCIPLINA
# -------------------------------

situacoes = []
reprovacoes = 0

for n in notas:
    # Verificando aprovação
    if n == 10:
        situacoes.append("Aprovado com distinção")
    elif n >= 6:
        situacoes.append("Aprovado")
    else:
        situacoes.append("Reprovado")
        reprovacoes += 1

# -------------------------------
# SITUAÇÃO FINAL DO ESTUDANTE
# -------------------------------

if reprovacoes == 0:
    status_final = "Passou de ano direto"
elif reprovacoes <= 2:
    status_final = "Passou de ano com dependência"
    status_final = "Retido"

# -------------------------------
# RESULTADO FINAL
# -------------------------------

print("\n=========== FICHA DO ESTUDANTE ===========")
print("Nome: %s" % nome)
print("ID: %s" % id_estudante)
print("Curso: %s" % curso)
print("Idade: %d" % idade)
print("Período: %s" % periodo)

print("\n------ Situação das Disciplinas ------")
for i in range(5):
    print("Disciplina: %s | Nota: %.1f | Situação: %s" % (disciplinas[i], notas[i], situacoes[i]))

print("\n------ Situação Final do Estudante ------")
print(status_final)

print("\n=== FIM DO SISTEMA ===")
