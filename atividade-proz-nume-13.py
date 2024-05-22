#Para cada trecho de código ao  executar  comente o restante para verificar o resultado de cada implementação
#VS Code: Comentar: Selecione as linhas e pressione Ctrl + /

print("Imprimindo números dos andares (exceto 13) usando 'for':")
for andar in range(1, 21):
    if andar == 13:
        continue
    print(andar)


print("Imprimindo números dos andares (exceto 13) usando 'while':")
andar = 1
while andar <= 20:
    if andar != 13:
        print(andar)
    andar += 1


print("Imprimindo números dos andares em ordem decrescente (exceto 13) usando 'for':")
for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)


print("Imprimindo números dos andares em ordem decrescente (exceto 13) usando 'while':")
andar = 20
while andar > 0:
    if andar != 13:
        print(andar)
    andar -= 1

