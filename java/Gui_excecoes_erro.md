# ☕ Guia Completo de Exceções Java — Try/Catch

> **Referência completa** de todas as exceções e erros built-in do Java,  
> com significados, exemplos práticos e boas práticas de tratamento.

---

## 📋 Índice

1. [Como Funciona o Try/Catch](#1-como-funciona-o-trycatch)
2. [Checked vs Unchecked Exceptions](#2-checked-vs-unchecked-exceptions)
3. [Erros de Tipo e Casting](#3-erros-de-tipo-e-casting)
4. [Erros de Referência Nula e Objeto](#4-erros-de-referência-nula-e-objeto)
5. [Erros de Índice e Array](#5-erros-de-índice-e-array)
6. [Erros de Aritmética](#6-erros-de-aritmética)
7. [Erros de I/O e Arquivo](#7-erros-de-io-e-arquivo)
8. [Erros de Concorrência e Thread](#8-erros-de-concorrência-e-thread)
9. [Erros de Memória e JVM](#9-erros-de-memória-e-jvm)
10. [Erros de Coleções e Iteração](#10-erros-de-coleções-e-iteração)
11. [Erros de Número e Formato](#11-erros-de-número-e-formato)
12. [Erros de Reflexão e Classe](#12-erros-de-reflexão-e-classe)
13. [Hierarquia Completa](#13-hierarquia-completa)
14. [Boas Práticas](#14-boas-práticas)
15. [Criar Exceções Personalizadas](#15-criar-exceções-personalizadas)
16. [Cheatsheet Rápido](#16-cheatsheet-rápido)

---

## 1. Como Funciona o Try/Catch

> O bloco `try/catch` captura e trata erros sem deixar o programa quebrar abruptamente.

```java
try {
    // Código que pode lançar uma exceção
    int resultado = 10 / 0;

} catch (ArithmeticException e) {
    // Executado SE essa exceção específica ocorrer
    System.out.println("Divisão por zero: " + e.getMessage());

} catch (NullPointerException | IllegalArgumentException e) {
    // Captura múltiplos tipos de uma vez (Multi-catch — Java 7+)
    System.out.println("Erro: " + e.getMessage());

} catch (Exception e) {
    // Captura qualquer outra exceção genérica
    System.out.println("Erro inesperado: " + e.getMessage());

} finally {
    // Executado SEMPRE, com exceção ou sem
    System.out.println("Bloco finally sempre executa!");
}
```

### Estrutura dos blocos

| Bloco | Quando executa | Uso principal |
|-------|---------------|---------------|
| `try` | Sempre (primeiro) | Código que pode lançar exceção |
| `catch` | Se a exceção correspondente for lançada | Tratar o erro |
| `finally` | **Sempre**, com ou sem exceção | Fechar recursos, limpeza |

---

### Inspecionar o objeto da exceção

```java
try {
    int[] array = new int[3];
    array[10] = 5;

} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println(e.getMessage());        // Index 10 out of bounds for length 3
    System.out.println(e.getClass().getName()); // java.lang.ArrayIndexOutOfBoundsException
    e.printStackTrace();                        // Stack trace completo no console
}
```

---

### Try-with-resources (Java 7+)

> Fecha recursos automaticamente — substitui o `finally` para I/O.

```java
// ❌ Forma antiga (verbosa e propensa a erros)
BufferedReader reader = null;
try {
    reader = new BufferedReader(new FileReader("dados.txt"));
    String linha = reader.readLine();
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (reader != null) {
        try { reader.close(); } catch (IOException e) { e.printStackTrace(); }
    }
}

// ✅ Try-with-resources (fecha automaticamente ao sair do bloco)
try (BufferedReader reader = new BufferedReader(new FileReader("dados.txt"))) {
    String linha = reader.readLine();
    System.out.println(linha);
} catch (IOException e) {
    System.out.println("Erro ao ler arquivo: " + e.getMessage());
}
// reader.close() é chamado automaticamente aqui
```

---

### Relançar uma exceção

```java
public void processar() throws IOException {
    try {
        lerArquivo();
    } catch (IOException e) {
        System.out.println("Logando o erro...");
        throw e;                          // relança a mesma exceção
    }
}

// Encapsular em outra exceção (wrapping)
public void processar() throws RuntimeException {
    try {
        lerArquivo();
    } catch (IOException e) {
        throw new RuntimeException("Falha ao processar", e); // causa original preservada
    }
}
```

---

## 2. Checked vs Unchecked Exceptions

> Esta é a distinção mais importante do sistema de exceções Java.

### Checked Exceptions (Verificadas)
- O **compilador obriga** você a tratar ou declarar com `throws`
- Representam situações externas e recuperáveis (arquivo não encontrado, rede indisponível)
- Estendem `Exception` (mas não `RuntimeException`)

```java
// O compilador exige que você trate IOException
public void lerArquivo(String caminho) throws IOException {
    FileReader file = new FileReader(caminho); // checked!
}

// Ou trate com try/catch
public void lerArquivo(String caminho) {
    try {
        FileReader file = new FileReader(caminho);
    } catch (IOException e) {
        System.out.println("Arquivo não encontrado!");
    }
}
```

**Principais Checked Exceptions:**
- `IOException` e subclasses
- `SQLException`
- `ClassNotFoundException`
- `InterruptedException`
- `ParseException`
- `CloneNotSupportedException`

---

### Unchecked Exceptions (Não Verificadas)
- O **compilador NÃO obriga** o tratamento
- Representam bugs de programação (índice inválido, null inesperado)
- Estendem `RuntimeException`

```java
// Java não obriga try/catch para RuntimeException
public void dividir(int a, int b) {
    int resultado = a / b;  // pode lançar ArithmeticException sem aviso do compilador
}
```

**Principais Unchecked Exceptions:**
- `NullPointerException`
- `ArrayIndexOutOfBoundsException`
- `ClassCastException`
- `ArithmeticException`
- `IllegalArgumentException`
- `IllegalStateException`

---

### Tabela comparativa

| Característica | Checked | Unchecked |
|----------------|---------|-----------|
| Compilador exige tratamento | ✅ Sim | ❌ Não |
| Herda de | `Exception` | `RuntimeException` |
| Representa | Problema externo | Bug de programação |
| Deve ser tratada | Sempre | Prevenida no código |
| Exemplo | `IOException` | `NullPointerException` |

---

## 3. Erros de Tipo e Casting

### `ClassCastException`
**Quando ocorre:** Tentativa de converter um objeto para um tipo incompatível.

```java
// Exemplo que causa ClassCastException
Object obj = "Eu sou uma String";
Integer numero = (Integer) obj;  // String não pode ser convertida para Integer

// Tratando
try {
    Object obj = "texto";
    Integer num = (Integer) obj;
} catch (ClassCastException e) {
    System.out.println("Cast inválido: " + e.getMessage());
}

// ✅ Prevenindo com instanceof
if (obj instanceof Integer) {
    Integer num = (Integer) obj;
}

// ✅ Forma moderna com Pattern Matching (Java 16+)
if (obj instanceof Integer num) {
    System.out.println("É um Integer: " + num);
}
```

---

### `NumberFormatException`
**Quando ocorre:** String que não representa um número válido é convertida para tipo numérico.  
*(Subclasse de `IllegalArgumentException`)*

```java
// Exemplos que causam NumberFormatException
Integer.parseInt("abc");        // não é número
Integer.parseInt("12.5");       // int não aceita decimal
Double.parseDouble("12,5");     // vírgula ao invés de ponto
Long.parseLong("");             // string vazia

// Tratando
try {
    int numero = Integer.parseInt("abc");
} catch (NumberFormatException e) {
    System.out.println("Formato inválido: " + e.getMessage());
}

// Método utilitário seguro
public static Integer parseIntSafe(String valor) {
    try {
        return Integer.parseInt(valor);
    } catch (NumberFormatException e) {
        return null;
    }
}
```

---

## 4. Erros de Referência Nula e Objeto

### `NullPointerException` (NPE)
**Quando ocorre:** Tentativa de usar uma referência que aponta para `null`.  
*(A exceção mais comum em Java!)*

```java
// Situações que causam NullPointerException
String texto = null;
texto.length();             // chamar método em null
texto.toUpperCase();        // qualquer método em null

String[] array = null;
array[0] = "valor";         // acessar array null

int[] numeros = null;
int tamanho = numeros.length; // acessar .length de array null

// Tratando
try {
    String nome = null;
    System.out.println(nome.length());
} catch (NullPointerException e) {
    System.out.println("Referência nula encontrada!");
    // Java 14+ mostra exatamente qual variável era null no stack trace
}

// ✅ Prevenindo — verificação explícita
if (texto != null) {
    System.out.println(texto.length());
}

// ✅ Prevenindo — usando Optional (Java 8+)
Optional<String> opcional = Optional.ofNullable(texto);
int tamanho = opcional.map(String::length).orElse(0);

// ✅ Prevenindo — Objects.requireNonNull
public void processar(String nome) {
    Objects.requireNonNull(nome, "O nome não pode ser null");
    // ...
}
```

---

### `IllegalArgumentException`
**Quando ocorre:** Método recebe um argumento inválido ou fora do esperado.

```java
// Exemplo
public void definirIdade(int idade) {
    if (idade < 0 || idade > 150) {
        throw new IllegalArgumentException("Idade inválida: " + idade);
    }
    this.idade = idade;
}

// Tratando
try {
    definirIdade(-5);
} catch (IllegalArgumentException e) {
    System.out.println("Argumento inválido: " + e.getMessage());
}
```

---

### `IllegalStateException`
**Quando ocorre:** Método chamado no momento errado, quando o objeto está em estado inválido.

```java
// Exemplo com Iterator
Iterator<String> it = lista.iterator();
it.remove(); // remove() antes de chamar next() — estado inválido!

// Exemplo personalizado
public class ConexaoDB {
    private boolean conectado = false;

    public void consultar(String sql) {
        if (!conectado) {
            throw new IllegalStateException("Conexão não foi aberta ainda!");
        }
        // executar query...
    }
}

// Tratando
try {
    consultar("SELECT * FROM usuarios");
} catch (IllegalStateException e) {
    System.out.println("Estado inválido: " + e.getMessage());
}
```

---

### `UnsupportedOperationException`
**Quando ocorre:** Operação não suportada pelo objeto — muito comum em coleções imutáveis.

```java
// Lista imutável criada com List.of() não suporta add/remove
List<String> lista = List.of("a", "b", "c");

try {
    lista.add("d");     // UnsupportedOperationException!
    lista.remove("a");  // UnsupportedOperationException!
} catch (UnsupportedOperationException e) {
    System.out.println("Operação não suportada nesta coleção!");
}

// ✅ Solução: use ArrayList para coleções mutáveis
List<String> mutavel = new ArrayList<>(List.of("a", "b", "c"));
mutavel.add("d"); // funciona
```

---

## 5. Erros de Índice e Array

### `ArrayIndexOutOfBoundsException`
**Quando ocorre:** Acesso a um índice inválido de um array (negativo ou >= tamanho).

```java
// Exemplos que causam ArrayIndexOutOfBoundsException
int[] numeros = {10, 20, 30};
numeros[5];     // índice 5 não existe (tamanho é 3)
numeros[-1];    // índice negativo inválido
numeros[3];     // índice igual ao tamanho também é inválido

// Tratando
try {
    int[] arr = {1, 2, 3};
    System.out.println(arr[10]);
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Índice inválido: " + e.getMessage());
}

// ✅ Prevenindo
for (int i = 0; i < numeros.length; i++) {
    System.out.println(numeros[i]); // sempre dentro do limite
}
```

---

### `StringIndexOutOfBoundsException`
**Quando ocorre:** Acesso a um índice inválido de uma String.  
*(Subclasse de `IndexOutOfBoundsException`)*

```java
String texto = "Java";

try {
    char c = texto.charAt(10);  // String tem 4 chars (0-3)
    String sub = texto.substring(2, 10); // fim maior que o tamanho
} catch (StringIndexOutOfBoundsException e) {
    System.out.println("Índice inválido na String: " + e.getMessage());
}
```

---

### `NegativeArraySizeException`
**Quando ocorre:** Tentativa de criar um array com tamanho negativo.

```java
try {
    int[] array = new int[-5]; // tamanho negativo
} catch (NegativeArraySizeException e) {
    System.out.println("Tamanho de array inválido: " + e.getMessage());
}
```

---

## 6. Erros de Aritmética

### `ArithmeticException`
**Quando ocorre:** Operação aritmética inválida — mais comum: divisão inteira por zero.

```java
// int / 0 lança exceção
try {
    int resultado = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Erro aritmético: " + e.getMessage()); // / by zero
}

// ⚠️ ATENÇÃO: double / 0.0 NÃO lança exceção — retorna Infinity ou NaN!
double infinito = 10.0 / 0.0;   // retorna Infinity
double nan = 0.0 / 0.0;          // retorna NaN (Not a Number)

System.out.println(Double.isInfinite(infinito));  // true
System.out.println(Double.isNaN(nan));            // true

// ✅ Verificando NaN e Infinity antes de usar
if (Double.isNaN(resultado) || Double.isInfinite(resultado)) {
    System.out.println("Resultado inválido!");
}
```

---

## 7. Erros de I/O e Arquivo

### `IOException`
**Quando ocorre:** Erro genérico de entrada/saída — leitura, escrita, rede, etc.  
*(Checked Exception — o compilador exige tratamento)*

```java
// Tratando IOException
try {
    FileReader reader = new FileReader("dados.txt");
    BufferedReader br = new BufferedReader(reader);
    String linha = br.readLine();
    br.close();
} catch (IOException e) {
    System.out.println("Erro de I/O: " + e.getMessage());
}
```

---

### `FileNotFoundException`
**Quando ocorre:** Arquivo não existe no caminho especificado ou sem permissão de acesso.  
*(Subclasse de `IOException`)*

```java
try (FileInputStream fis = new FileInputStream("arquivo_inexistente.txt")) {
    // ler arquivo...
} catch (FileNotFoundException e) {
    System.out.println("Arquivo não encontrado: " + e.getMessage());
} catch (IOException e) {
    System.out.println("Erro ao ler arquivo: " + e.getMessage());
}

// ✅ Verificar antes de abrir
File arquivo = new File("dados.txt");
if (arquivo.exists() && arquivo.isFile()) {
    // abrir com segurança
}
```

---

### `EOFException`
**Quando ocorre:** Fim inesperado do arquivo/stream durante leitura.  
*(Subclasse de `IOException`)*

```java
try (DataInputStream dis = new DataInputStream(new FileInputStream("dados.bin"))) {
    while (true) {
        int valor = dis.readInt(); // lança EOFException ao chegar no fim
    }
} catch (EOFException e) {
    System.out.println("Fim do arquivo atingido.");
} catch (IOException e) {
    System.out.println("Erro de leitura: " + e.getMessage());
}
```

---

### `SocketException` / `ConnectException`
**Quando ocorre:** Erros de conexão de rede.

```java
import java.net.*;
import java.io.*;

try {
    Socket socket = new Socket("servidor.com", 8080);
} catch (ConnectException e) {
    System.out.println("Conexão recusada: " + e.getMessage());
} catch (SocketTimeoutException e) {
    System.out.println("Tempo limite de conexão excedido!");
} catch (IOException e) {
    System.out.println("Erro de rede: " + e.getMessage());
}
```

---

## 8. Erros de Concorrência e Thread

### `InterruptedException`
**Quando ocorre:** Thread é interrompida enquanto está esperando (sleep, wait, join).  
*(Checked Exception)*

```java
try {
    Thread.sleep(5000); // espera 5 segundos
} catch (InterruptedException e) {
    System.out.println("Thread foi interrompida!");
    Thread.currentThread().interrupt(); // boa prática: restaurar o status de interrupção
}
```

---

### `ConcurrentModificationException`
**Quando ocorre:** Coleção modificada enquanto está sendo iterada.

```java
List<String> lista = new ArrayList<>(Arrays.asList("a", "b", "c"));

// ❌ Causa ConcurrentModificationException
try {
    for (String item : lista) {
        if (item.equals("b")) {
            lista.remove(item); // modificar durante iteração!
        }
    }
} catch (ConcurrentModificationException e) {
    System.out.println("Não modifique a lista durante a iteração!");
}

// ✅ Solução 1: usar Iterator.remove()
Iterator<String> it = lista.iterator();
while (it.hasNext()) {
    if (it.next().equals("b")) {
        it.remove(); // seguro
    }
}

// ✅ Solução 2: usar removeIf() (Java 8+)
lista.removeIf(item -> item.equals("b"));
```

---

### `DeadlockError` / Deadlock
**Quando ocorre:** Duas threads se bloqueiam mutuamente esperando uma pela outra.  
*(Não é uma exceção — o programa trava silenciosamente)*

```java
// Exemplo de deadlock
Object recurso1 = new Object();
Object recurso2 = new Object();

Thread t1 = new Thread(() -> {
    synchronized (recurso1) {
        synchronized (recurso2) { /* usa recurso2 */ }
    }
});

Thread t2 = new Thread(() -> {
    synchronized (recurso2) {
        synchronized (recurso1) { /* usa recurso1 — DEADLOCK! */ }
    }
});

// ✅ Prevenção: sempre adquirir locks na mesma ordem
```

---

## 9. Erros de Memória e JVM

### `OutOfMemoryError`
**Quando ocorre:** JVM ficou sem memória heap para alocar novos objetos.  
*(É um Error, não Exception — normalmente não deve ser capturado)*

```java
// ⚠️ Raramente capture Errors — apenas em situações muito específicas
try {
    List<byte[]> lista = new ArrayList<>();
    while (true) {
        lista.add(new byte[1024 * 1024]); // aloca 1MB por vez até estourar
    }
} catch (OutOfMemoryError e) {
    System.out.println("Sem memória! Libere recursos.");
}

// Aumentar memória heap via JVM:
// java -Xmx2g -Xms512m MinhaAplicacao
// -Xmx = máximo de heap    -Xms = heap inicial
```

---

### `StackOverflowError`
**Quando ocorre:** Pilha de chamadas estourou, geralmente por recursão infinita.  
*(É um Error — subclasse de VirtualMachineError)*

```java
// Recursão sem caso base causa StackOverflowError
public static void infinita() {
    infinita(); // chama a si mesma infinitamente
}

try {
    infinita();
} catch (StackOverflowError e) {
    System.out.println("Recursão muito profunda! Verifique o caso base.");
}

// ✅ Sempre defina um caso base na recursão
public static int fatorial(int n) {
    if (n <= 1) return 1;          // caso base
    return n * fatorial(n - 1);    // chamada recursiva
}
```

---

### `ClassNotFoundException`
**Quando ocorre:** Classe não encontrada em tempo de execução ao usar reflexão ou carregamento dinâmico.  
*(Checked Exception)*

```java
try {
    Class<?> clazz = Class.forName("com.exemplo.ClasseInexistente");
} catch (ClassNotFoundException e) {
    System.out.println("Classe não encontrada: " + e.getMessage());
}

// Comum ao carregar drivers JDBC
try {
    Class.forName("com.mysql.cj.jdbc.Driver");
} catch (ClassNotFoundException e) {
    System.out.println("Driver MySQL não está no classpath!");
}
```

---

## 10. Erros de Coleções e Iteração

### `NoSuchElementException`
**Quando ocorre:** `next()` chamado em iterador vazio, ou `Scanner` sem mais tokens.

```java
import java.util.*;

// Com Iterator
List<String> lista = new ArrayList<>();
Iterator<String> it = lista.iterator();

try {
    it.next(); // lista vazia!
} catch (NoSuchElementException e) {
    System.out.println("Iterador está vazio!");
}

// ✅ Verificar antes
if (it.hasNext()) {
    String item = it.next();
}

// Com Optional (Java 8+)
Optional<String> vazio = Optional.empty();
try {
    vazio.get(); // NoSuchElementException se vazio!
} catch (NoSuchElementException e) {
    System.out.println("Optional está vazio!");
}
// ✅ Use orElse ou orElseThrow
String valor = vazio.orElse("padrão");
```

---

### `EmptyStackException`
**Quando ocorre:** Operação `pop()` ou `peek()` em uma `Stack` vazia.

```java
Stack<Integer> pilha = new Stack<>();

try {
    pilha.pop();  // pilha vazia!
} catch (EmptyStackException e) {
    System.out.println("A pilha está vazia!");
}

// ✅ Verificar antes
if (!pilha.isEmpty()) {
    int topo = pilha.pop();
}
```

---

## 11. Erros de Número e Formato

### `ParseException`
**Quando ocorre:** String não pode ser convertida para o tipo esperado pelo `parse()`.  
*(Checked Exception — muito comum com datas)*

```java
import java.text.*;
import java.util.*;

SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

try {
    Date data = sdf.parse("32/13/2024"); // data inválida
} catch (ParseException e) {
    System.out.println("Data inválida! Posição do erro: " + e.getErrorOffset());
}

// ✅ Usando DateTimeFormatter (Java 8+) — mais moderno
import java.time.*;
import java.time.format.*;

try {
    LocalDate data = LocalDate.parse("32/13/2024",
        DateTimeFormatter.ofPattern("dd/MM/yyyy"));
} catch (DateTimeParseException e) {
    System.out.println("Formato de data inválido: " + e.getMessage());
}
```

---

### `InputMismatchException`
**Quando ocorre:** `Scanner` lê um token que não corresponde ao tipo esperado.

```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);

try {
    System.out.print("Digite um número: ");
    int numero = scanner.nextInt(); // usuário digita "abc"
} catch (InputMismatchException e) {
    System.out.println("Entrada inválida! Digite apenas números.");
    scanner.nextLine(); // limpar o buffer do scanner
}
```

---

## 12. Erros de Reflexão e Classe

### `InstantiationException`
**Quando ocorre:** Tentativa de instanciar uma classe abstrata ou interface via reflexão.

```java
try {
    Object obj = Runnable.class.newInstance(); // interface não pode ser instanciada
} catch (InstantiationException e) {
    System.out.println("Não é possível instanciar: " + e.getMessage());
} catch (IllegalAccessException e) {
    System.out.println("Acesso negado ao construtor!");
}
```

---

### `IllegalAccessException`
**Quando ocorre:** Reflexão tenta acessar um membro privado sem permissão.  
*(Checked Exception)*

```java
try {
    Class<?> clazz = MinhaClasse.class;
    java.lang.reflect.Method metodo = clazz.getDeclaredMethod("metodoPri vado");
    metodo.invoke(new MinhaClasse()); // acesso negado!
} catch (IllegalAccessException e) {
    System.out.println("Acesso ao método negado!");
    // ✅ Solução: metodo.setAccessible(true) antes de invoke
}
```

---

## 13. Hierarquia Completa

```
Throwable
 ├── Error                              ← Problemas graves da JVM — NÃO capture
 │    ├── OutOfMemoryError              ← Heap esgotado
 │    ├── StackOverflowError            ← Recursão infinita
 │    ├── VirtualMachineError           ← Erro interno da JVM
 │    ├── AssertionError                ← assert falhou
 │    └── LinkageError
 │         └── NoClassDefFoundError    ← Classe encontrada em compile mas não em runtime
 │
 └── Exception                         ← Base de todas as exceções tratáveis
      │
      ├── ── CHECKED (compilador exige tratamento) ──────────────
      ├── IOException
      │    ├── FileNotFoundException
      │    ├── EOFException
      │    ├── SocketException
      │    └── ConnectException
      ├── SQLException
      ├── ClassNotFoundException
      ├── InterruptedException
      ├── ParseException
      ├── CloneNotSupportedException
      │
      └── ── UNCHECKED (RuntimeException) ──────────────────────
           └── RuntimeException
                ├── NullPointerException
                ├── ClassCastException
                ├── ArithmeticException
                ├── IllegalArgumentException
                │    └── NumberFormatException
                ├── IllegalStateException
                ├── UnsupportedOperationException
                ├── IndexOutOfBoundsException
                │    ├── ArrayIndexOutOfBoundsException
                │    └── StringIndexOutOfBoundsException
                ├── NegativeArraySizeException
                ├── ConcurrentModificationException
                ├── NoSuchElementException
                │    └── EmptyStackException
                ├── InputMismatchException
                └── DateTimeException
                     └── DateTimeParseException
```

---

## 14. Boas Práticas

### ✅ Capture exceções específicas, não genéricas

```java
// ❌ Ruim — captura tudo sem distinção
try {
    int num = Integer.parseInt(entrada);
    int resultado = num / divisor;
} catch (Exception e) {
    System.out.println("Deu erro");
}

// ✅ Bom — cada exceção tratada adequadamente
try {
    int num = Integer.parseInt(entrada);
    int resultado = num / divisor;
} catch (NumberFormatException e) {
    System.out.println("Entrada não é um número válido!");
} catch (ArithmeticException e) {
    System.out.println("Divisão por zero!");
}
```

---

### ✅ Nunca engula exceções silenciosamente

```java
// ❌ Péssimo — o erro desaparece sem deixar rastro
try {
    processarArquivo();
} catch (IOException e) {
    // não faz nada — NUNCA faça isso!
}

// ✅ No mínimo, logue o erro
try {
    processarArquivo();
} catch (IOException e) {
    logger.error("Falha ao processar arquivo", e); // log com stack trace
    throw new RuntimeException("Erro no processamento", e); // ou relance
}
```

---

### ✅ Use try-with-resources para fechar recursos

```java
// ❌ Propenso a vazamento de recursos
Connection conn = null;
try {
    conn = dataSource.getConnection();
    // usar conn...
} finally {
    if (conn != null) conn.close(); // e se close() lançar exceção?
}

// ✅ Try-with-resources fecha tudo automaticamente
try (Connection conn = dataSource.getConnection();
     PreparedStatement stmt = conn.prepareStatement(sql)) {
    // usar conn e stmt...
} catch (SQLException e) {
    System.out.println("Erro no banco: " + e.getMessage());
}
```

---

### ✅ Prefira exceções unchecked em APIs modernas

```java
// Checked exception força o chamador a tratar (muitas vezes desnecessário)
public Usuario buscarUsuario(int id) throws UsuarioNotFoundException { ... }

// ✅ Unchecked é mais limpa para o chamador
public Usuario buscarUsuario(int id) {
    Usuario usuario = repositorio.findById(id);
    if (usuario == null) {
        throw new UsuarioNotFoundException("Usuário " + id + " não encontrado");
    }
    return usuario;
}
```

---

### ✅ Preserve a causa original ao encapsular

```java
// ❌ Perde a causa original — dificulta o debug
try {
    conexao.conectar();
} catch (IOException e) {
    throw new ServicoException("Falha na conexão"); // causa perdida!
}

// ✅ Preserva a causa original no construtor
try {
    conexao.conectar();
} catch (IOException e) {
    throw new ServicoException("Falha na conexão", e); // causa preservada
}
```

---

### ✅ Use a ordem correta no multi-catch

```java
// ❌ Erro de compilação: FileNotFoundException nunca será alcançado
// (é subclasse de IOException que vem antes)
try {
    // ...
} catch (IOException e) {
    // ...
} catch (FileNotFoundException e) { // UNREACHABLE — erro de compilação!
    // ...
}

// ✅ Correto: mais específico primeiro, mais genérico por último
try {
    // ...
} catch (FileNotFoundException e) { // mais específico
    System.out.println("Arquivo não encontrado");
} catch (IOException e) {           // mais genérico
    System.out.println("Erro de I/O");
}
```

---

## 15. Criar Exceções Personalizadas

> Crie suas próprias exceções para representar erros específicos do seu domínio.

```java
// ── Exceção Unchecked (recomendado para a maioria dos casos) ─────────

public class SaldoInsuficienteException extends RuntimeException {

    private final double saldoAtual;
    private final double valorSolicitado;

    public SaldoInsuficienteException(double saldoAtual, double valorSolicitado) {
        super(String.format(
            "Saldo insuficiente! Disponível: R$%.2f, Solicitado: R$%.2f",
            saldoAtual, valorSolicitado
        ));
        this.saldoAtual = saldoAtual;
        this.valorSolicitado = valorSolicitado;
    }

    // Construtor para encapsular causa original
    public SaldoInsuficienteException(double saldo, double valor, Throwable causa) {
        super("Saldo insuficiente", causa);
        this.saldoAtual = saldo;
        this.valorSolicitado = valor;
    }

    public double getSaldoAtual() { return saldoAtual; }
    public double getValorSolicitado() { return valorSolicitado; }
}


// ── Hierarquia de exceções personalizadas ────────────────────────────

// Base do domínio bancário
public class BancoException extends RuntimeException {
    public BancoException(String mensagem) { super(mensagem); }
    public BancoException(String mensagem, Throwable causa) { super(mensagem, causa); }
}

public class SaldoInsuficienteException extends BancoException {
    public SaldoInsuficienteException(double saldo, double valor) {
        super(String.format("Saldo R$%.2f insuficiente para saque de R$%.2f", saldo, valor));
    }
}

public class ContaInativaException extends BancoException {
    public ContaInativaException(String numeroConta) {
        super("Conta " + numeroConta + " está inativa!");
    }
}

public class LimiteDiarioExcedidoException extends BancoException {
    public LimiteDiarioExcedidoException(double limite) {
        super(String.format("Limite diário de R$%.2f excedido!", limite));
    }
}


// ── Usando as exceções personalizadas ────────────────────────────────

public class ContaBancaria {
    private double saldo;
    private boolean ativa;
    private String numero;

    public void sacar(double valor) {
        if (!ativa) {
            throw new ContaInativaException(numero);
        }
        if (valor < 0) {
            throw new IllegalArgumentException("Valor de saque não pode ser negativo!");
        }
        if (valor > saldo) {
            throw new SaldoInsuficienteException(saldo, valor);
        }
        this.saldo -= valor;
    }
}

// Capturando exceções personalizadas
ContaBancaria conta = new ContaBancaria();

try {
    conta.sacar(500.0);

} catch (SaldoInsuficienteException e) {
    System.out.println(e.getMessage());
    System.out.printf("Você pode sacar no máximo R$%.2f%n", e.getSaldoAtual());

} catch (ContaInativaException e) {
    System.out.println(e.getMessage());

} catch (BancoException e) {
    // captura qualquer outro erro bancário
    System.out.println("Erro bancário: " + e.getMessage());
}
```

---

## 16. Cheatsheet Rápido

```
── TIPO E CASTING ─────────────────────────────────────────────
ClassCastException          Cast inválido              (Integer) "texto"
NumberFormatException       String não é número        Integer.parseInt("abc")

── REFERÊNCIA E OBJETO ────────────────────────────────────────
NullPointerException        Usar referência null       null.length()
IllegalArgumentException    Argumento inválido         idade = -1
IllegalStateException       Estado inválido            uso antes de inicializar
UnsupportedOperationException  Operação não suportada  List.of().add("x")

── ÍNDICE E ARRAY ─────────────────────────────────────────────
ArrayIndexOutOfBoundsException   Índice fora do array  array[99]
StringIndexOutOfBoundsException  Índice fora da String texto.charAt(99)
NegativeArraySizeException       Tamanho negativo      new int[-1]

── ARITMÉTICA ─────────────────────────────────────────────────
ArithmeticException         Divisão inteira por zero   10 / 0

── ARQUIVO E I/O (Checked) ────────────────────────────────────
IOException                 Erro genérico de I/O
FileNotFoundException       Arquivo não existe
EOFException                Fim inesperado do arquivo

── CONCORRÊNCIA ───────────────────────────────────────────────
InterruptedException        Thread interrompida (Checked)
ConcurrentModificationException  Coleção modificada durante iteração

── MEMÓRIA E JVM (Errors) ─────────────────────────────────────
OutOfMemoryError            Heap esgotado
StackOverflowError          Recursão infinita
ClassNotFoundException      Classe não encontrada (Checked)

── COLEÇÕES ───────────────────────────────────────────────────
NoSuchElementException      Iterator ou Optional vazio
EmptyStackException         Stack vazia no pop/peek

── NÚMERO E FORMATO ───────────────────────────────────────────
ParseException              Falha no parse de data (Checked)
InputMismatchException      Scanner recebe tipo errado
DateTimeParseException      Falha no parse de LocalDate

── REGRAS DE OURO ─────────────────────────────────────────────
1. Capture exceções específicas, não Exception genérica
2. NUNCA engula exceções com catch vazio
3. Use try-with-resources para fechar recursos (I/O, DB)
4. Checked → problemas externos  |  Unchecked → bugs de código
5. Catch mais específico SEMPRE antes do mais genérico
6. Preserve a causa original ao encapsular: new MinhaEx("msg", e)
7. Não use exceções para controle de fluxo normal
8. Errors (OutOfMemory, StackOverflow) raramente devem ser capturados
```

---

*Guia elaborado para Java 11+. Recursos como try-with-resources requerem Java 7+, pattern matching requer Java 16+.*
