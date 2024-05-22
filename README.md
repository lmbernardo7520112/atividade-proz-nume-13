# 🏨 Hotel Andares - Código Python

Este documento contém códigos Python que imprimem os números dos andares de um hotel de 20 andares, exceto o 13º andar, utilizando diferentes laços de repetição. O desafio adicional é imprimir os andares em ordem decrescente.

## 📋 Requisitos

- Python 3.x

---

## 🔢 Código usando `for`(Exemplo)

Imprime os números dos andares, exceto o 13º, usando um laço `for`.

```python
print("Imprimindo números dos andares (exceto 13) usando 'for':")
for andar in range(1, 21):
    if andar == 13:
        continue
    print(andar)
## ✍️ Notas

- Utilizamos `continue` no laço `for` para pular o 13º andar.
- Utilizamos `if andar != 13` no laço `while` para evitar a impressão do 13º andar.
- Ambos os desafios adicionais imprimem os números em ordem decrescente, começando do 20º andar até o 1º, excluindo o 13º.
