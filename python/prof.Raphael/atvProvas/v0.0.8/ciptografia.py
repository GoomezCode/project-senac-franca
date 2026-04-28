# **Descrição da Task:**

# Desenvolver uma função chamada `criptografar_senha` que receba uma senha e retorne uma string criptografada.

# **Regras:**
# 1. Inverter a ordem dos caracteres da senha
# 2. Converter cada caractere para hexadecimal
# 3. Remover o prefixo '0x'
# 4. Concatenar todos os valores hexadecimais

# **Critérios de Aceite:**
# - Função deve se chamar `criptografar_senha`
# - Recebe 1 parâmetro: senha (string)
# - Retorna uma string com a senha criptografada
# - A ordem dos passos deve ser seguida estritamente

# **Exemplo de uso:**
# ```python
# Entrada: 'abc'
# Processo: 'abc' → 'cba' → '63' + '62' + '61'
# Saída: '636261'
# ```

# **Dica:** Use `ord()` para pegar o código ASCII e `hex()` para converter para hexadecimal

# **Prazo:** 2 dias
# **Prioridade:** Alta

def _converterHexadecial(pl):
    cover = hex(ord(pl)).replace("0", "")
    return cover.replace("x", "")

def criptografar_senha(senha):
    senha = senha[::-1]
    newSenha = ""
    for i in senha:
        newSenha += _converterHexadecial(i)
    return newSenha
    