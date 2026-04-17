# 🐍 Guia Completo de Exceções Python — Try/Except

> **Referência completa** de todos os erros e exceções built-in do Python,  
> com significados, exemplos práticos e boas práticas de tratamento.

---

## 📋 Índice

1. [Como Funciona o Try/Except](#1-como-funciona-o-tryexcept)
2. [Erros de Tipo e Valor](#2-erros-de-tipo-e-valor)
3. [Erros de Índice e Chave](#3-erros-de-índice-e-chave)
4. [Erros de Importação e Módulo](#4-erros-de-importação-e-módulo)
5. [Erros de I/O e Sistema](#5-erros-de-io-e-sistema)
6. [Erros de Aritmética](#6-erros-de-aritmética)
7. [Erros de Memória e Recursão](#7-erros-de-memória-e-recursão)
8. [Erros de Iteração](#8-erros-de-iteração)
9. [Erros de Sintaxe e Runtime](#9-erros-de-sintaxe-e-runtime)
10. [Erros de Encoding](#10-erros-de-encoding)
11. [Avisos (Warnings)](#11-avisos-warnings)
12. [Hierarquia Completa](#12-hierarquia-completa)
13. [Boas Práticas](#13-boas-práticas)
14. [Criar Exceções Personalizadas](#14-criar-exceções-personalizadas)
15. [Cheatsheet Rápido](#15-cheatsheet-rápido)

---

## 1. Como Funciona o Try/Except

> O bloco `try/except` permite capturar e tratar erros sem que o programa quebre.

```python
try:
    # Código que pode gerar um erro
    resultado = 10 / 0

except ZeroDivisionError:
    # Executado SE o erro ocorrer
    print("Não pode dividir por zero!")

except (TypeError, ValueError) as e:
    # Captura múltiplos tipos de erro de uma vez
    print(f"Erro de tipo ou valor: {e}")

except Exception as e:
    # Captura qualquer outro erro genérico
    print(f"Erro inesperado: {e}")

else:
    # Executado SOMENTE se NÃO houve erro
    print(f"Resultado: {resultado}")

finally:
    # Executado SEMPRE, com erro ou sem
    print("Bloco finally sempre roda!")
```

### Estrutura dos blocos

| Bloco | Quando executa | Uso principal |
|-------|---------------|---------------|
| `try` | Sempre (primeiro) | Código que pode falhar |
| `except` | Se ocorrer o erro especificado | Tratar o erro |
| `else` | Se **não** ocorreu nenhum erro | Código que depende do sucesso |
| `finally` | **Sempre**, com ou sem erro | Fechar arquivos, conexões, limpeza |

### Capturar o objeto do erro

```python
try:
    int("abc")
except ValueError as e:
    print(type(e))    # <class 'ValueError'>
    print(str(e))     # invalid literal for int() with base 10: 'abc'
    print(e.args)     # ("invalid literal for int() with base 10: 'abc'",)
```

### Relançar um erro

```python
try:
    int("abc")
except ValueError:
    print("Logando o erro...")
    raise  # Relança o mesmo erro para cima
```

---

## 2. Erros de Tipo e Valor

### `TypeError`
**Quando ocorre:** Operação ou função aplicada a um objeto de tipo incompatível.

```python
# Exemplos que causam TypeError
"texto" + 5             # não pode somar str com int
len(42)                 # len() não aceita int
None + 1                # operação com None
[1, 2] * "3"            # multiplicação de lista com string

# Tratando
try:
    resultado = "texto" + 5
except TypeError as e:
    print(f"Tipo incompatível: {e}")
```

---

### `ValueError`
**Quando ocorre:** Tipo correto, mas o **valor** em si é inválido para a operação.

```python
# Exemplos que causam ValueError
int("abc")              # string não é um número
float("xyz")            # string não é um float
int("12.5")             # int() não aceita casas decimais em string
[1, 2, 3].index(99)     # valor não existe na lista
int("10", 1)            # base inválida

# Tratando
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Isso não é um número válido!")
```

---

### `AttributeError`
**Quando ocorre:** Tentativa de acessar um atributo ou método que não existe no objeto.

```python
# Exemplos que causam AttributeError
[1, 2, 3].upper()       # listas não têm método upper()
"texto".append("!")     # strings não têm append()
None.split()            # None não tem métodos

# Tratando
try:
    [1, 2].upper()
except AttributeError as e:
    print(f"Método não existe: {e}")
```

---

### `NameError`
**Quando ocorre:** Variável, função ou nome referenciado antes de ser definido.

```python
# Exemplo que causa NameError
print(variavel_inexistente)

# Tratando
try:
    print(x)
except NameError:
    print("Variável não foi definida!")
```

---

### `UnboundLocalError`
**Quando ocorre:** Variável local usada antes de ser atribuída dentro de uma função.  
*(Subclasse de `NameError`)*

```python
# Exemplo que causa UnboundLocalError
def funcao():
    print(x)   # x ainda não foi atribuído aqui
    x = 10

# Tratando
try:
    funcao()
except UnboundLocalError as e:
    print(f"Variável local sem valor: {e}")
```

---

## 3. Erros de Índice e Chave

### `IndexError`
**Quando ocorre:** Índice fora do intervalo válido de uma lista, tupla ou string.

```python
# Exemplos que causam IndexError
lista = [1, 2, 3]
lista[10]               # índice 10 não existe
lista[-99]              # índice negativo inválido
"abc"[5]                # índice fora da string

# Tratando
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("Índice fora do intervalo da lista!")
```

---

### `KeyError`
**Quando ocorre:** Chave não existe em um dicionário.

```python
# Exemplos que causam KeyError
dicionario = {"nome": "Ana"}
dicionario["idade"]     # chave "idade" não existe

# Tratando
try:
    usuario = {"nome": "Ana"}
    print(usuario["email"])
except KeyError as e:
    print(f"Chave não encontrada: {e}")

# Alternativa segura com .get()
email = usuario.get("email", "não informado")  # retorna None ou valor padrão
```

---

## 4. Erros de Importação e Módulo

### `ImportError`
**Quando ocorre:** Falha ao importar um módulo ou ao importar um nome específico de um módulo.

```python
# Exemplos que causam ImportError
from os import funcao_inexistente

# Tratando
try:
    from os import funcao_que_nao_existe
except ImportError as e:
    print(f"Falha na importação: {e}")
```

---

### `ModuleNotFoundError`
**Quando ocorre:** O módulo que está tentando importar não existe ou não está instalado.  
*(Subclasse de `ImportError`)*

```python
# Exemplo que causa ModuleNotFoundError
import biblioteca_que_nao_existe

# Tratando
try:
    import numpy
except ModuleNotFoundError:
    print("NumPy não está instalado! Execute: pip install numpy")
```

---

## 5. Erros de I/O e Sistema

### `FileNotFoundError`
**Quando ocorre:** Arquivo ou diretório especificado não existe.

```python
# Exemplo que causa FileNotFoundError
open("arquivo_inexistente.txt", "r")

# Tratando
try:
    with open("dados.txt", "r") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
```

---

### `PermissionError`
**Quando ocorre:** Sem permissão do sistema operacional para acessar o arquivo ou diretório.

```python
# Tratando
try:
    with open("/etc/shadow", "r") as f:
        conteudo = f.read()
except PermissionError:
    print("Sem permissão para acessar este arquivo!")
```

---

### `IsADirectoryError`
**Quando ocorre:** Operação esperava um arquivo, mas recebeu um diretório.

```python
try:
    open("/home/usuario", "r")
except IsADirectoryError:
    print("Isso é um diretório, não um arquivo!")
```

---

### `OSError` / `IOError`
**Quando ocorre:** Erro genérico de sistema operacional ou entrada/saída.  
`IOError` é um alias de `OSError` no Python 3.

```python
# FileNotFoundError, PermissionError e outros são subclasses de OSError
try:
    open("arquivo.txt", "r")
except OSError as e:
    print(f"Erro do sistema: {e.strerror} — código: {e.errno}")
```

---

### `TimeoutError`
**Quando ocorre:** Uma operação (geralmente de rede ou I/O) demorou mais que o tempo limite.

```python
import socket

try:
    socket.setdefaulttimeout(1)
    s = socket.socket()
    s.connect(("192.168.0.1", 9999))
except TimeoutError:
    print("Conexão excedeu o tempo limite!")
```

---

## 6. Erros de Aritmética

### `ZeroDivisionError`
**Quando ocorre:** Divisão ou módulo por zero.

```python
# Exemplos que causam ZeroDivisionError
10 / 0
10 // 0
10 % 0

# Tratando
try:
    resultado = 100 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
    resultado = None
```

---

### `OverflowError`
**Quando ocorre:** Resultado numérico grande demais para ser representado.  
*(Mais comum com `float`; `int` em Python cresce automaticamente)*

```python
import math

try:
    resultado = math.exp(1000)  # e^1000 é enorme demais
except OverflowError:
    print("Número grande demais para representar!")
```

---

### `FloatingPointError`
**Quando ocorre:** Erro em operação de ponto flutuante (raramente ocorre no Python padrão).

```python
import fpectl  # módulo necessário para ativar esse comportamento
# Na prática, Python silencia a maioria dos erros de float
```

---

## 7. Erros de Memória e Recursão

### `MemoryError`
**Quando ocorre:** Python não consegue alocar memória suficiente para continuar.

```python
try:
    lista_gigante = [0] * (10**12)  # tentar alocar terabytes
except MemoryError:
    print("Memória insuficiente!")
```

---

### `RecursionError`
**Quando ocorre:** Profundidade máxima de recursão atingida (padrão: 1000 chamadas).

```python
# Função que causa RecursionError
def infinita():
    return infinita()

# Tratando
try:
    infinita()
except RecursionError:
    print("Recursão muito profunda! Verifique o caso base.")

# Ver e alterar o limite de recursão
import sys
print(sys.getrecursionlimit())   # 1000 por padrão
sys.setrecursionlimit(2000)      # aumentar o limite (use com cuidado)
```

---

## 8. Erros de Iteração

### `StopIteration`
**Quando ocorre:** Um iterador não tem mais itens para retornar.  
*(Normalmente tratado internamente pelo `for`; raramente você precisa capturá-lo)*

```python
# Usando next() manualmente
numeros = iter([1, 2, 3])

try:
    while True:
        print(next(numeros))
except StopIteration:
    print("Iterador esgotado!")

# Forma segura com valor padrão
valor = next(numeros, None)  # retorna None em vez de lançar erro
```

---

### `GeneratorExit`
**Quando ocorre:** Um generator é fechado com `.close()`.

```python
def meu_generator():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("Generator foi fechado!")

g = meu_generator()
next(g)
g.close()  # dispara GeneratorExit dentro do generator
```

---

## 9. Erros de Sintaxe e Runtime

### `SyntaxError`
**Quando ocorre:** Código com sintaxe inválida. Python não consegue nem iniciar a execução.

```python
# Exemplo de SyntaxError (não pode ser capturado em try/except normal)
# if True           <- falta o ':'
# print("olá"       <- parêntese não fechado

# Capturar SyntaxError ao compilar código dinâmico
try:
    codigo = "if True print('oi')"  # sintaxe errada
    compile(codigo, "<string>", "exec")
except SyntaxError as e:
    print(f"Erro de sintaxe na linha {e.lineno}: {e.msg}")
```

---

### `IndentationError`
**Quando ocorre:** Indentação incorreta no código.  
*(Subclasse de `SyntaxError`)*

```python
# Exemplo que causa IndentationError:
# def funcao():
# print("sem indentação")  <- erro aqui
```

---

### `TabError`
**Quando ocorre:** Mistura inconsistente de tabs e espaços na indentação.  
*(Subclasse de `IndentationError`)*

```
Solução: configure seu editor para usar sempre espaços (PEP 8 recomenda 4 espaços).
```

---

### `RuntimeError`
**Quando ocorre:** Erro genérico em tempo de execução que não se encaixa em outra categoria.

```python
try:
    raise RuntimeError("Algo inesperado aconteceu")
except RuntimeError as e:
    print(f"Erro de runtime: {e}")
```

---

### `NotImplementedError`
**Quando ocorre:** Método abstrato chamado sem ter sido implementado na subclasse.

```python
class Animal:
    def falar(self):
        raise NotImplementedError("Subclasse deve implementar o método falar()")

class Cachorro(Animal):
    def falar(self):
        return "Au!"

class Peixe(Animal):
    pass  # não implementou falar()

try:
    peixe = Peixe()
    peixe.falar()
except NotImplementedError as e:
    print(e)
```

---

## 10. Erros de Encoding

### `UnicodeDecodeError`
**Quando ocorre:** Falha ao decodificar bytes em string com o encoding especificado.

```python
try:
    b"\xff\xfe".decode("utf-8")  # bytes inválidos para UTF-8
except UnicodeDecodeError as e:
    print(f"Erro de decodificação: {e}")

# Solução: especificar o encoding correto ou usar errors='ignore'/'replace'
texto = b"\xff\xfe".decode("utf-16", errors="replace")
```

---

### `UnicodeEncodeError`
**Quando ocorre:** Falha ao codificar uma string em bytes com o encoding especificado.

```python
try:
    "café ☕".encode("ascii")  # ASCII não suporta acentos e emojis
except UnicodeEncodeError as e:
    print(f"Erro de codificação: {e}")

# Solução
"café ☕".encode("utf-8")             # UTF-8 suporta tudo
"café".encode("ascii", errors="ignore")  # ignora caracteres inválidos
```

---

## 11. Avisos (Warnings)

> Warnings **não param o programa** — apenas alertam sobre situações problemáticas.

```python
import warnings

# Tipos de Warning
# DeprecationWarning   — funcionalidade está obsoleta
# UserWarning          — aviso genérico do desenvolvedor
# RuntimeWarning       — algo suspeito em tempo de execução
# FutureWarning        — comportamento mudará em versões futuras
# ResourceWarning      — recurso não foi fechado corretamente

# Emitir um warning personalizado
warnings.warn("Este método está obsoleto, use novo_metodo()", DeprecationWarning)

# Capturar warnings como exceções
warnings.filterwarnings("error", category=DeprecationWarning)

try:
    warnings.warn("Obsoleto!", DeprecationWarning)
except DeprecationWarning:
    print("Capturei o warning como erro!")

# Ignorar um tipo de warning
warnings.filterwarnings("ignore", category=ResourceWarning)
```

---

## 12. Hierarquia Completa

```
BaseException
 ├── SystemExit                  ← sys.exit() — encerra o programa
 ├── KeyboardInterrupt           ← Ctrl+C no terminal
 ├── GeneratorExit               ← generator.close()
 └── Exception                  ← base de quase todos os erros
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         └── UnicodeEncodeError
      ├── AttributeError
      ├── NameError
      │    └── UnboundLocalError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── OSError  (= IOError)
      │    ├── FileNotFoundError
      │    ├── FileExistsError
      │    ├── PermissionError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── TimeoutError
      │    └── ConnectionError
      │         ├── ConnectionRefusedError
      │         ├── ConnectionResetError
      │         └── BrokenPipeError
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    ├── OverflowError
      │    └── FloatingPointError
      ├── MemoryError
      ├── RecursionError
      ├── RuntimeError
      │    └── NotImplementedError
      ├── StopIteration
      ├── StopAsyncIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── ReferenceError
      ├── AssertionError          ← quando assert falha
      ├── EOFError                ← input() chegou ao fim do arquivo
      ├── SystemError             ← erro interno do interpretador Python
      └── Warning
           ├── DeprecationWarning
           ├── UserWarning
           ├── RuntimeWarning
           ├── FutureWarning
           └── ResourceWarning
```

**Dica importante:** Ao usar `except Exception`, você captura quase tudo. Mas `KeyboardInterrupt` e `SystemExit` **não** são subclasses de `Exception` — eles sobem direto de `BaseException`. Por isso, um `except Exception` não impede o `Ctrl+C` de funcionar.

---

## 13. Boas Práticas

### ✅ Seja específico nos excepts

```python
# ❌ Ruim — captura tudo sem distinção
try:
    resultado = int(entrada) / divisor
except:
    pass

# ✅ Bom — captura apenas o que é esperado
try:
    resultado = int(entrada) / divisor
except ValueError:
    print("Entrada não é um número válido!")
except ZeroDivisionError:
    print("Divisor não pode ser zero!")
```

---

### ✅ Nunca use `except` sem especificar o tipo

```python
# ❌ Péssimo — silencia até KeyboardInterrupt e erros graves
try:
    codigo_perigoso()
except:
    pass

# ✅ Se precisar pegar tudo, use Exception explicitamente
try:
    codigo_perigoso()
except Exception as e:
    print(f"Erro inesperado: {e}")
    raise  # sempre relance se não souber tratar
```

---

### ✅ Use `finally` para limpeza de recursos

```python
# ❌ Arquivo pode ficar aberto se der erro
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
arquivo.close()

# ✅ Com finally
arquivo = open("dados.txt", "r")
try:
    conteudo = arquivo.read()
finally:
    arquivo.close()  # sempre fecha, com erro ou sem

# ✅✅ Melhor ainda: usar with statement
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
# Fecha automaticamente ao sair do bloco
```

---

### ✅ Use `else` para código que depende do sucesso

```python
# ❌ Ambíguo — qual linha causou o ValueError?
try:
    numero = int(entrada)
    resultado = calcular(numero)
    salvar(resultado)
except ValueError:
    print("Erro!")

# ✅ Claro — só o int() está no try
try:
    numero = int(entrada)
except ValueError:
    print("Entrada inválida!")
else:
    # Só executa se int() funcionou
    resultado = calcular(numero)
    salvar(resultado)
```

---

### ✅ Prefira EAFP ao LBYL

```python
# LBYL — Look Before You Leap (verificar antes)
# Funciona, mas menos "pythônico"
if "chave" in dicionario:
    valor = dicionario["chave"]

# EAFP — Easier to Ask Forgiveness than Permission (estilo Python)
# Mais idiomático e frequentemente mais rápido
try:
    valor = dicionario["chave"]
except KeyError:
    valor = None
```

---

## 14. Criar Exceções Personalizadas

> Crie suas próprias exceções para erros específicos do seu domínio.

```python
# Exceção simples
class SaldoInsuficienteError(Exception):
    pass

# Exceção com informações extras
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_solicitado):
        self.saldo_atual = saldo_atual
        self.valor_solicitado = valor_solicitado
        super().__init__(
            f"Saldo insuficiente! Disponível: R${saldo_atual:.2f}, "
            f"Solicitado: R${valor_solicitado:.2f}"
        )

# Hierarquia de exceções personalizadas
class BancoError(Exception):
    """Base para todos os erros do sistema bancário"""
    pass

class SaldoInsuficienteError(BancoError):
    pass

class ContaInativaError(BancoError):
    pass

class LimiteDiarioExcedidoError(BancoError):
    pass


# Usando as exceções personalizadas
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        self.ativa = True

    def sacar(self, valor):
        if not self.ativa:
            raise ContaInativaError("Conta está inativa!")
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        return valor


# Capturando exceções personalizadas
conta = ContaBancaria(saldo=100.0)

try:
    conta.sacar(500.0)
except SaldoInsuficienteError as e:
    print(e)
    print(f"Você pode sacar no máximo R${e.saldo_atual:.2f}")
except BancoError as e:
    print(f"Erro bancário genérico: {e}")
```

---

## 15. Cheatsheet Rápido

```
── TIPO E VALOR ───────────────────────────────────────────────
TypeError           Tipo errado na operação       "a" + 1
ValueError          Valor inválido                int("abc")
AttributeError      Atributo não existe           [].upper()
NameError           Variável não definida         print(x)
UnboundLocalError   Var local sem valor           uso antes de atribuir

── ÍNDICE E CHAVE ─────────────────────────────────────────────
IndexError          Índice fora do range          lista[99]
KeyError            Chave não existe              dic["x"]

── IMPORTAÇÃO ─────────────────────────────────────────────────
ImportError         Falha na importação           from os import xyz
ModuleNotFoundError Módulo não instalado          import numpy

── ARQUIVO E SISTEMA ──────────────────────────────────────────
FileNotFoundError   Arquivo não existe            open("x.txt")
PermissionError     Sem permissão de acesso       open("/etc/shadow")
IsADirectoryError   Era arquivo, veio diretório
OSError / IOError   Erro genérico do sistema

── ARITMÉTICA ─────────────────────────────────────────────────
ZeroDivisionError   Divisão por zero              10 / 0
OverflowError       Número grande demais          math.exp(1000)

── MEMÓRIA E RECURSÃO ─────────────────────────────────────────
MemoryError         Sem memória suficiente
RecursionError      Recursão muito profunda

── ITERAÇÃO ───────────────────────────────────────────────────
StopIteration       Iterador esgotado             next() sem itens
GeneratorExit       Generator foi fechado

── SINTAXE E RUNTIME ──────────────────────────────────────────
SyntaxError         Código inválido               if True print()
IndentationError    Indentação errada
RuntimeError        Erro genérico de runtime
NotImplementedError Método abstrato não impl.

── ENCODING ───────────────────────────────────────────────────
UnicodeDecodeError  Bytes → string falhou
UnicodeEncodeError  String → bytes falhou

── ESPECIAIS ──────────────────────────────────────────────────
AssertionError      assert False disparou
EOFError            input() sem mais dados
KeyboardInterrupt   Usuário pressionou Ctrl+C
SystemExit          sys.exit() chamado
```

### 🛡️ Regras de Ouro do Try/Except

1. **Seja específico** — capture apenas as exceções que você sabe tratar.
2. **Nunca use `except: pass`** — silenciar erros esconde bugs sérios.
3. **Use `finally`** para fechar recursos (arquivos, conexões, etc.).
4. **Prefira `with`** ao `try/finally` para gerenciar recursos.
5. **Use `else`** para separar o código que depende do sucesso.
6. **Crie exceções personalizadas** para erros do seu domínio de negócio.
7. **Sempre relance (`raise`)** se capturou mas não sabe como tratar.
8. **Nunca capture `BaseException`** diretamente — deixe `Ctrl+C` funcionar.

---

*Guia elaborado para Python 3.6+. Alguns comportamentos podem variar em versões anteriores.*
