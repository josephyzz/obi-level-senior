"""
Musica para todos
"""
# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/musica/
# # Points 50/100
# t = 1,696s / 1,6s -> perdir aqui
# memory 4.16 MB/ 64 MB

# Record = 27min

# By josephyzz

amigos, musica, compartilhada = map(int, input().split())

musicas_amadas = []
musicas_odiadas = []
ocorrencia = 0

for amigo in range(amigos):
    a, d = map(int, input().split())
    musicas_amadas.append(a)
    musicas_odiadas.append(d)

while compartilhada in musicas_odiadas:
    for i, valor in enumerate(musicas_odiadas):
        if compartilhada == valor:
            compartilhada = musicas_amadas[i]
            ocorrencia += 1

    if ocorrencia > amigos:
        ocorrencia = -1
        break
print(ocorrencia)
