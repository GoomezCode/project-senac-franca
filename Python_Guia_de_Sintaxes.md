# 🐍 Guia de Python — Sintaxes Essenciais

> Guia prático com as principais sintaxes do Python explicadas de forma simples, com dicas de como escrever código mais limpo e produtivo.

---

## Sumário

1. [Variáveis e Tipos de Dados](#1-variáveis-e-tipos-de-dados)
2. [Operadores](#2-operadores)
3. [Strings](#3-strings)
4. [Listas](#4-listas)
5. [Dicionários](#5-dicionários)
6. [Condicionais](#6-condicionais)
7. [Laços de Repetição](#7-laços-de-repetição)
8. [Funções](#8-funções)
9. [Classes e Objetos](#9-classes-e-objetos)
10. [Tratamento de Erros](#10-tratamento-de-erros)
11. [Arquivos](#11-arquivos)
12. [Dicas de Produtividade](#12-dicas-de-produtividade)

---

## 1. Variáveis e Tipos de Dados

Em Python, você não precisa declarar o tipo da variável — ele é definido automaticamente.

```python
# Texto (str)
nome = "StockEasy"

# Número inteiro (int)
quantidade = 10

# Número decimal (float)
preco = 29.90

# Verdadeiro ou Falso (bool)
em_estoque = True

# Nenhum valor (None) — equivalente ao null de outras linguagens
descricao = None

# Verificando o tipo de uma variável
print(type(preco))  # <class 'float'>
```

---

## 2. Operadores

```python
# Aritméticos
10 + 3   # 13  → soma
10 - 3   # 7   → subtração
10 * 3   # 30  → multiplicação
10 / 3   # 3.33 → divisão
10 // 3  # 3   → divisão inteira (sem decimal)
10 % 3   # 1   → resto da divisão
10 ** 2  # 100 → potência

# Comparação (retornam True ou False)
10 == 10  # True  → igual
10 != 5   # True  → diferente
10 > 5    # True  → maior que
10 < 5    # False → menor que
10 >= 10  # True  → maior ou igual
10 <= 9   # False → menor ou igual

# Lógicos
True and False  # False → os dois precisam ser True
True or False   # True  → basta um ser True
not True        # False → inverte o valor
```

---

## 3. Strings

```python
nome = "Maria"
sobrenome = "Silva"

# Juntar strings (concatenação)
nome_completo = nome + " " + sobrenome
print(nome_completo)  # Maria Silva

# F-string — forma mais moderna e limpa de montar textos
produto = "Arroz"
preco = 12.50
print(f"O produto {produto} custa R$ {preco:.2f}")
# O produto Arroz custa R$ 12.50

# Métodos úteis de string
texto = "  hello world  "
texto.upper()       # "  HELLO WORLD  " → tudo maiúsculo
texto.lower()       # "  hello world  " → tudo minúsculo
texto.strip()       # "hello world"     → remove espaços das bordas
texto.replace("hello", "oi")  # "  oi world  "
texto.split(" ")    # ['', '', 'hello', 'world', '', '']

# Verificações
"hello".startswith("he")  # True
"hello".endswith("lo")    # True
"llo" in "hello"          # True → contém?

# Tamanho
len("hello")  # 5
```

---

## 4. Listas

Uma lista guarda vários valores em ordem, como uma fila.

```python
produtos = ["Arroz", "Feijão", "Óleo", "Sal"]

# Acessando itens pelo índice (começa do 0)
produtos[0]   # "Arroz"
produtos[-1]  # "Sal" → último item

# Fatiamento (slicing)
produtos[1:3]  # ["Feijão", "Óleo"] → do índice 1 até antes do 3

# Adicionando e removendo
produtos.append("Açúcar")       # adiciona no final
produtos.insert(1, "Macarrão")  # adiciona na posição 1
produtos.remove("Sal")          # remove pelo valor
produtos.pop()                  # remove e retorna o último
produtos.pop(0)                 # remove pelo índice

# Verificando
len(produtos)          # quantidade de itens
"Arroz" in produtos    # True → está na lista?

# Ordenando
produtos.sort()         # ordena em ordem alfabética (modifica a lista)
sorted(produtos)        # ordena sem modificar a original

# Percorrendo
for produto in produtos:
    print(produto)
```

---

## 5. Dicionários

Um dicionário guarda pares de **chave: valor**, como uma ficha de cadastro.

```python
produto = {
    "nome": "Arroz",
    "preco": 12.50,
    "quantidade": 50,
    "em_estoque": True
}

# Acessando valores
produto["nome"]           # "Arroz"
produto.get("preco")      # 12.50
produto.get("cor", "N/A") # "N/A" → valor padrão se não existir

# Adicionando e editando
produto["categoria"] = "Alimentos"  # adiciona nova chave
produto["preco"] = 13.00            # atualiza valor existente

# Removendo
del produto["em_estoque"]
produto.pop("categoria")

# Percorrendo
for chave, valor in produto.items():
    print(f"{chave}: {valor}")

# Verificando chaves
"nome" in produto  # True
```

---

## 6. Condicionais

```python
estoque = 3

if estoque == 0:
    print("Sem estoque — repor urgente!")
elif estoque <= 5:
    print("Estoque baixo — atenção!")
else:
    print("Estoque ok")

# Condicional em uma linha (ternário)
status = "Disponível" if estoque > 0 else "Indisponível"
print(status)  # Disponível
```

---

## 7. Laços de Repetição

### For

```python
# Percorrendo uma lista
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)

# Percorrendo com índice
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
# 0: maçã
# 1: banana
# 2: uva

# Range — repetir N vezes
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8 → de 2 em 2
```

### While

```python
tentativas = 0

while tentativas < 3:
    print(f"Tentativa {tentativas + 1}")
    tentativas += 1

# Controlando o loop
for i in range(10):
    if i == 5:
        break     # para o loop completamente
    if i % 2 == 0:
        continue  # pula para a próxima iteração
    print(i)  # imprime só os ímpares antes do 5: 1, 3
```

---

## 8. Funções

```python
# Função simples
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))  # Olá, Maria!

# Parâmetro com valor padrão
def calcular_desconto(preco, desconto=10):
    return preco - (preco * desconto / 100)

calcular_desconto(100)      # 90.0  → usa desconto=10
calcular_desconto(100, 20)  # 80.0  → usa desconto=20

# Retornando múltiplos valores
def resumo_produto(nome, preco, quantidade):
    total = preco * quantidade
    return nome, total

produto, valor = resumo_produto("Arroz", 12.50, 10)
print(f"{produto}: R$ {valor}")  # Arroz: R$ 125.0

# Função com número variável de argumentos
def soma(*numeros):
    return sum(numeros)

soma(1, 2, 3)      # 6
soma(10, 20, 30)   # 60
```

---

## 9. Classes e Objetos

```python
class Produto:
    # Construtor — roda ao criar um objeto
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # Método — função dentro da classe
    def esta_em_estoque(self):
        return self.quantidade > 0

    def vender(self, qtd):
        if qtd > self.quantidade:
            return "Estoque insuficiente"
        self.quantidade -= qtd
        return f"{qtd} unidade(s) vendida(s)"

    # Representação em texto do objeto
    def __str__(self):
        return f"{self.nome} — R$ {self.preco:.2f} ({self.quantidade} un.)"


# Criando objetos
arroz = Produto("Arroz 5kg", 24.90, 30)
oleo = Produto("Óleo de soja", 8.50, 0)

print(arroz)                    # Arroz 5kg — R$ 24.90 (30 un.)
print(arroz.esta_em_estoque())  # True
print(oleo.esta_em_estoque())   # False
print(arroz.vender(5))          # 5 unidade(s) vendida(s)
print(arroz.quantidade)         # 25
```

---

## 10. Tratamento de Erros

```python
# Sem tratamento — o programa crasha
numero = int("abc")  # ValueError: invalid literal

# Com tratamento — o programa continua
try:
    numero = int("abc")
    print(f"Número: {numero}")
except ValueError:
    print("Erro: valor informado não é um número")
except ZeroDivisionError:
    print("Erro: divisão por zero")
finally:
    print("Isso sempre executa, com ou sem erro")

# Lançando um erro manualmente
def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente para o saque")
    return saldo - valor
```

---

## 11. Arquivos

```python
# Escrevendo em um arquivo
with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Relatório de vendas\n")
    arquivo.write("Total: R$ 1.240,00\n")

# Lendo um arquivo
with open("relatorio.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Lendo linha por linha
with open("relatorio.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Modos de abertura
# "r"  → leitura (padrão)
# "w"  → escrita (apaga o conteúdo anterior)
# "a"  → adiciona ao final sem apagar
# "rb" → leitura em binário (para imagens, PDFs etc.)
```

---

## 12. Dicas de Produtividade

### List Comprehension — for em uma linha

```python
# Jeito longo
numeros = [1, 2, 3, 4, 5]
dobrados = []
for n in numeros:
    dobrados.append(n * 2)

# Jeito produtivo ✅
dobrados = [n * 2 for n in numeros]
# [2, 4, 6, 8, 10]

# Com filtro — só os pares
pares = [n for n in numeros if n % 2 == 0]
# [2, 4]

# Aplicado ao StockEasy — nomes dos produtos com estoque baixo
produtos = [
    {"nome": "Arroz", "qtd": 3},
    {"nome": "Feijão", "qtd": 50},
    {"nome": "Óleo", "qtd": 2},
]
alertas = [p["nome"] for p in produtos if p["qtd"] < 5]
# ["Arroz", "Óleo"]
```

### Dictionary Comprehension

```python
# Criar dicionário a partir de uma lista
nomes = ["Arroz", "Feijão", "Óleo"]
precos = [12.50, 8.90, 6.70]

catalogo = {nome: preco for nome, preco in zip(nomes, precos)}
# {"Arroz": 12.5, "Feijão": 8.9, "Óleo": 6.7}
```

### Unpacking — desempacotamento

```python
# Atribuição múltipla
a, b, c = 1, 2, 3

# Trocar valores sem variável auxiliar
a, b = b, a

# Ignorar valores com _
primeiro, _, ultimo = [10, 20, 30]
```

### Walrus Operator `:=` — atribuir e testar ao mesmo tempo

```python
# Sem walrus
dados = input("Digite o nome: ")
if dados:
    print(f"Nome: {dados}")

# Com walrus ✅
if nome := input("Digite o nome: "):
    print(f"Nome: {nome}")
```

### Enumerate e Zip

```python
# enumerate → índice + valor juntos
for i, item in enumerate(["a", "b", "c"], start=1):
    print(f"{i}. {item}")
# 1. a  2. b  3. c

# zip → percorre duas listas ao mesmo tempo
nomes = ["Ana", "João", "Maria"]
notas = [9.5, 7.0, 8.5]

for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")
```

### F-string com formatação

```python
preco = 1240.5
quantidade = 7

# Duas casas decimais
f"R$ {preco:.2f}"         # "R$ 1240.50"

# Separador de milhar
f"R$ {preco:,.2f}"        # "R$ 1,240.50"

# Alinhar texto (útil em relatórios)
f"{'Produto':<20} {'Preço':>10}"   # alinha à esquerda e direita
```

### any() e all() — verificações rápidas em listas

```python
estoques = [50, 3, 0, 12, 1]

any(e == 0 for e in estoques)   # True → algum está zerado?
all(e > 0 for e in estoques)    # False → todos têm estoque?
```

---

> **Dica final:** A melhor forma de aprender Python é praticando dentro do próprio projeto. Tente usar list comprehension nas consultas do banco de dados do StockEasy e f-strings em todos os textos dinâmicos do sistema!
