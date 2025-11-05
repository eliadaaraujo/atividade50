# Leia o nome do aluno e três notas (0–10). Calcule a média aritmética e mostre:
# “Aprovado” (média ≥ 7.0), “Recuperação” (5.0–6.9) ou “Reprovado” (< 5.0).
# Exiba: Nome: <nome> | Média: X.Y | Situação: <...>.


aluno = (input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3)/3

if media >= 7.0:
    situacao = "Aprovado"

elif media >= 5.0:
    situacao = "Recuperação"

else:
    situacao = "Reprovado"

print(f"Nome: {aluno} | Média: {media:.1f} | Situação: {situacao}")
