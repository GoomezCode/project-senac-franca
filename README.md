 --- 
 <h3 align="center">Project Senac franca</h3>
 <h4 align="center">GoomezCode</h3>
 
 ---

 # ⌨️ Guia Completo de Shortcuts — IDEs para Java
 
 > **Cobertura:** Eclipse IDE · IntelliJ IDEA · Visual Studio Code  
 > **Sistema:** Os atalhos utilizam `Ctrl` para Windows/Linux. No macOS, substitua `Ctrl` por `Cmd` e `Alt` por `Option`.
 
 ---
 
 ## 📋 Índice
 
 1. [Navegação e Busca](#1-navegação-e-busca)
 2. [Edição de Código](#2-edição-de-código)
 3. [Refatoração](#3-refatoração)
 4. [Geração de Código](#4-geração-de-código)
 5. [Compilação e Execução](#5-compilação-e-execução)
 6. [Debug](#6-debug)
 7. [Git e Controle de Versão](#7-git-e-controle-de-versão)
 8. [Gerenciamento de Janelas e Abas](#8-gerenciamento-de-janelas-e-abas)
 9. [Comentários e Formatação](#9-comentários-e-formatação)
 10. [Dicas Finais](#10-dicas-finais)
 
 ---
 
 ## 1. Navegação e Busca
 
 > Encontrar arquivos, classes, métodos e símbolos rapidamente é essencial para produtividade.
 
 ### 🔍 Buscar Arquivo / Classe
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Abrir arquivo pelo nome | `Ctrl + Shift + R` | `Ctrl + Shift + N` | `Ctrl + P` |
 | Buscar qualquer símbolo (classe, método, variável) | `Ctrl + Shift + T` (só classes) | `Ctrl + N` (classes) / `Ctrl + Alt + Shift + N` (símbolos) | `Ctrl + T` |
 | Busca global em todos os arquivos | `Ctrl + H` | `Ctrl + Shift + F` | `Ctrl + Shift + F` |
 | Ir para linha específica | `Ctrl + L` | `Ctrl + G` | `Ctrl + G` |
 | Buscar texto no arquivo atual | `Ctrl + F` | `Ctrl + F` | `Ctrl + F` |
 | Substituir texto no arquivo atual | `Ctrl + F` → "Replace" | `Ctrl + R` | `Ctrl + H` |
 | Substituir em todos os arquivos | `Ctrl + H` | `Ctrl + Shift + R` | `Ctrl + Shift + H` |
 
 **Explicação detalhada:**
 
 - **Eclipse `Ctrl + Shift + R`** — Abre o "Open Resource" para buscar qualquer arquivo do workspace pelo nome (suporta wildcards como `*.java`).
 - **IntelliJ `Shift + Shift` (dois Shifts seguidos)** — O famoso "Search Everywhere" que busca tudo: arquivos, classes, métodos, ações, configurações. Um dos atalhos mais poderosos do IntelliJ.
 - **VS Code `Ctrl + P`** — Abre o Quick Open. Digite o nome do arquivo. Use `@` para buscar símbolos no arquivo atual ou `#` para buscar em todo o projeto.
 
 ---
 
 ### 🔗 Navegação no Código
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Ir para a definição / declaração | `F3` | `Ctrl + B` ou `Ctrl + Clique` | `F12` ou `Ctrl + Clique` |
 | Ir para implementação de interface | `Ctrl + T` | `Ctrl + Alt + B` | `Ctrl + F12` |
 | Voltar para posição anterior | `Alt + ←` | `Ctrl + Alt + ←` | `Alt + ←` |
 | Avançar para posição seguinte | `Alt + →` | `Ctrl + Alt + →` | `Alt + →` |
 | Ir para o próximo erro/warning | `Ctrl + .` | `F2` | `F8` |
 | Ver todos os usos de um símbolo | `Ctrl + Shift + G` | `Alt + F7` | `Shift + F12` |
 | Ir para a linha acima/abaixo do método | `Ctrl + Shift + ↑/↓` | `Alt + ↑/↓` | `Ctrl + ↑/↓` |
 | Navegar entre métodos | `Ctrl + ↑/↓` | `Alt + ↑/↓` | — |
 | Abrir estrutura do arquivo (outline) | `Ctrl + O` | `Ctrl + F12` | `Ctrl + Shift + O` |
 | Mostrar hierarquia de herança | `F4` | `Ctrl + H` | Extensão necessária |
 
 **Explicação detalhada:**
 
 - **`F3` (Eclipse) / `Ctrl + B` (IntelliJ) / `F12` (VS Code)** — Navega diretamente para onde a classe, método ou variável foi declarada. Indispensável ao ler código desconhecido.
 - **IntelliJ `Alt + F7`** — "Find Usages" mostra todos os lugares onde aquela classe, método ou variável é utilizada no projeto, exibindo resultados em uma janela dedicada.
 - **VS Code `Shift + F12`** — "Find All References" semelhante ao "Find Usages" do IntelliJ, lista todas as referências ao símbolo selecionado.
 - **IntelliJ `Ctrl + Alt + ←/→`** — Navega entre locais visitados recentemente, como o botão "voltar/avançar" de um browser, mas para o código.
 
 ---
 
 ## 2. Edição de Código
 
 > Atalhos para escrever, mover, duplicar e deletar código com eficiência.
 
 ### ✏️ Seleção de Texto
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Selecionar linha inteira | `Ctrl + L` (posiciona), depois `Home` e `Shift + End` | `Ctrl + W` (expande seleção) | `Ctrl + L` |
 | Expandir seleção progressivamente | — | `Ctrl + W` | `Shift + Alt + →` |
 | Selecionar todas as ocorrências | — | `Ctrl + Shift + Alt + J` | `Ctrl + Shift + L` |
 | Selecionar próxima ocorrência | `Ctrl + K` | `Alt + J` | `Ctrl + D` |
 | Seleção em múltiplos cursores | — | `Alt + Clique` | `Alt + Clique` |
 | Adicionar cursor acima/abaixo | — | `Ctrl + Shift + Alt + ↑/↓` | `Ctrl + Alt + ↑/↓` |
 
 **Explicação detalhada:**
 
 - **IntelliJ `Ctrl + W`** — Expande a seleção progressivamente: primeiro seleciona a palavra, depois a expressão, depois a linha, depois o bloco, etc. Um dos atalhos mais úteis para selecionar código estruturalmente.
 - **VS Code `Ctrl + D`** — Seleciona a próxima ocorrência da palavra selecionada. Pressionando repetidamente, vai selecionando as próximas, permitindo editar todas ao mesmo tempo com múltiplos cursores.
 - **VS Code `Ctrl + L`** — Seleciona a linha inteira onde o cursor está posicionado.
 
 ---
 
 ### 📝 Mover e Duplicar Linhas
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Mover linha para cima | `Alt + ↑` | `Shift + Alt + ↑` | `Alt + ↑` |
 | Mover linha para baixo | `Alt + ↓` | `Shift + Alt + ↓` | `Alt + ↓` |
 | Duplicar linha abaixo | `Ctrl + Alt + ↓` | `Ctrl + D` | `Shift + Alt + ↓` |
 | Duplicar linha acima | `Ctrl + Alt + ↑` | — | `Shift + Alt + ↑` |
 | Deletar linha | `Ctrl + D` | `Ctrl + Y` | `Ctrl + Shift + K` |
 | Juntar linhas | — | `Ctrl + Shift + J` | — |
 
 **Explicação detalhada:**
 
 - **`Alt + ↑/↓`** — Move a linha (ou bloco selecionado) para cima ou para baixo sem precisar cortar e colar manualmente. Funciona de forma similar nas três IDEs.
 - **IntelliJ `Ctrl + D`** — Duplica a linha atual (ou seleção) imediatamente abaixo. Atenção: no Eclipse, `Ctrl + D` **deleta** a linha, comportamento oposto!
 - **VS Code `Ctrl + Shift + K`** — Deleta a linha inteira onde o cursor está, sem deixar linha em branco.
 
 ---
 
 ### 🧹 Operações de Texto
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Desfazer | `Ctrl + Z` | `Ctrl + Z` | `Ctrl + Z` |
 | Refazer | `Ctrl + Y` | `Ctrl + Shift + Z` | `Ctrl + Shift + Z` |
 | Copiar linha (sem selecionar) | `Ctrl + C` (cursor na linha) | `Ctrl + C` (cursor na linha) | `Ctrl + C` (cursor na linha) |
 | Recortar linha inteira | `Ctrl + X` (cursor na linha) | `Ctrl + X` (cursor na linha) | `Ctrl + X` (cursor na linha) |
 | Converter para maiúsculas | `Ctrl + Shift + X` | `Ctrl + Shift + U` | Extensão necessária |
 | Converter para minúsculas | `Ctrl + Shift + Y` | `Ctrl + Shift + U` (toggle) | Extensão necessária |
 | Completar código (IntelliSense) | `Ctrl + Space` | `Ctrl + Space` | `Ctrl + Space` |
 | Completar código avançado | — | `Ctrl + Shift + Space` | — |
 
 **Explicação detalhada:**
 
 - **`Ctrl + Space`** — Ativa o autocomplete em todas as IDEs. Mostra sugestões de código contextual: métodos disponíveis, variáveis no escopo, imports possíveis, etc.
 - **IntelliJ `Ctrl + Shift + Space`** — "Smart Completion" filtra as sugestões pelo tipo esperado. Por exemplo, em `String s = `, só mostra métodos que retornam `String`.
 - Ao pressionar `Ctrl + C` ou `Ctrl + X` sem selecionar nada, as três IDEs copiam/recortam a **linha inteira** automaticamente.
 
 ---
 
 ## 3. Refatoração
 
 > Reestruturar código com segurança, renomeando, extraindo e movendo elementos.
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Renomear (refactor rename) | `Alt + Shift + R` | `Shift + F6` | `F2` |
 | Extrair método | `Alt + Shift + M` | `Ctrl + Alt + M` | `Ctrl + Shift + R` → Extract Method |
 | Extrair variável local | `Alt + Shift + L` | `Ctrl + Alt + V` | `Ctrl + Shift + R` → Extract Variable |
 | Extrair constante | `Alt + Shift + C` | `Ctrl + Alt + C` | — |
 | Mover classe/arquivo | `Alt + Shift + V` | `F6` | `F2` (no explorer) |
 | Encapsular campo (gerar getter/setter) | `Alt + Shift + S` → Encapsulate | `Ctrl + Alt + F` | Extensão necessária |
 | Inline (substituir variável pela expressão) | `Alt + Shift + I` | `Ctrl + Alt + N` | — |
 | Alterar assinatura do método | `Alt + Shift + C` | `Ctrl + F6` | — |
 | Abrir menu de refatorações | `Alt + Shift + T` | `Ctrl + Alt + Shift + T` | `Ctrl + Shift + R` |
 
 **Explicação detalhada:**
 
 - **Rename (`Shift + F6` no IntelliJ / `F2` no VS Code)** — Renomeia o símbolo (classe, método, variável) em **todos** os lugares do projeto simultaneamente, com segurança. Muito superior a um simples "buscar e substituir".
 - **Extract Method (`Ctrl + Alt + M` no IntelliJ)** — Selecione um trecho de código e pressione o atalho: a IDE cria um novo método com aquele código e substitui o local pela chamada ao método. Parâmetros são identificados automaticamente.
 - **Extract Variable (`Ctrl + Alt + V` no IntelliJ)** — Selecione uma expressão e a IDE cria uma variável local com ela, substituindo todas as ocorrências na mesma visão.
 - **IntelliJ `Ctrl + Alt + Shift + T`** — Abre o menu completo de refatorações disponíveis para o contexto atual. Ótimo para descobrir opções.
 
 ---
 
 ## 4. Geração de Código
 
 > Gere código boilerplate automaticamente: construtores, getters, setters, overrides, etc.
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Gerar código (menu principal) | `Alt + Shift + S` | `Alt + Insert` | `Ctrl + .` (Quick Fix) |
 | Gerar construtor | `Alt + Shift + S` → Constructor | `Alt + Insert` → Constructor | `Ctrl + .` |
 | Gerar getter e setter | `Alt + Shift + S` → Getters/Setters | `Alt + Insert` → Getter/Setter | `Ctrl + .` |
 | Gerar `equals()` e `hashCode()` | `Alt + Shift + S` → equals/hashCode | `Alt + Insert` → equals/hashCode | Extensão necessária |
 | Gerar `toString()` | `Alt + Shift + S` → toString | `Alt + Insert` → toString | Extensão necessária |
 | Override de métodos da superclasse | `Alt + Shift + S` → Override | `Ctrl + O` | `Ctrl + .` |
 | Corrigir automaticamente erros/warnings | `Ctrl + 1` | `Alt + Enter` | `Ctrl + .` |
 | Importar classe automaticamente | `Ctrl + Shift + O` | `Alt + Enter` | `Ctrl + .` (ou automático) |
 | Organizar e remover imports não usados | `Ctrl + Shift + O` | `Ctrl + Alt + O` | `Shift + Alt + O` |
 
 **Explicação detalhada:**
 
 - **Eclipse `Alt + Shift + S`** — Abre o menu "Source" com todas as opções de geração de código para a classe atual. Centraliza em um único lugar a geração de construtores, getters, setters, equals, hashCode, toString, delegações, etc.
 - **IntelliJ `Alt + Insert`** — O "Generate" do IntelliJ, equivalente ao `Alt + Shift + S` do Eclipse. Contextual: dentro de uma classe gera membros, no Project Explorer cria novos arquivos/classes.
 - **IntelliJ `Alt + Enter`** — O atalho mais versátil do IntelliJ. Sugere e aplica correções automáticas para praticamente qualquer situação: importar classe, implementar métodos de interface, corrigir erros, adicionar anotações, converter estruturas de código, etc.
 - **`Ctrl + 1` (Eclipse) / `Alt + Enter` (IntelliJ) / `Ctrl + .` (VS Code)** — Todos acionam a "ação rápida" no contexto do cursor: corrigem erros de compilação, sugerem melhorias, importam classes ausentes. Habitue-se a usar sempre que aparecer um sublinhado vermelho ou amarelo.
 
 ---
 
 ## 5. Compilação e Execução
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Compilar projeto | `Ctrl + B` (Build) | `Ctrl + F9` | Automático (ou `Ctrl + Shift + B`) |
 | Executar última configuração | `Ctrl + F11` | `Shift + F10` | `F5` |
 | Executar arquivo atual | `Alt + Shift + X` → J | `Ctrl + Shift + F10` | `F5` (ou botão Run) |
 | Parar execução | Botão Stop | `Ctrl + F2` | `Shift + F5` |
 | Executar testes unitários | `Alt + Shift + X` → T | `Ctrl + Shift + F10` (em teste) | `Ctrl + ; Ctrl + A` (extensão Java Test) |
 | Reexecutar testes | — | `Ctrl + F5` | — |
 
 **Explicação detalhada:**
 
 - **Eclipse `Ctrl + F11`** — "Run Last Launched": executa a última classe que foi executada. Muito útil para não precisar sempre apontar o arquivo a ser executado.
 - **IntelliJ `Shift + F10`** — Equivalente ao `Ctrl + F11` do Eclipse. Executa a última configuração de execução salva no run manager.
 - **IntelliJ `Ctrl + Shift + F10`** — Executa o arquivo onde o cursor está posicionado diretamente, sem precisar de uma configuração salva. Detecta se é uma classe com `main()` ou um teste e age adequadamente.
 - **VS Code com extensão "Extension Pack for Java"** — O VS Code não tem suporte nativo a Java; instale o pack da Microsoft. Após isso, um botão `▶ Run` aparece acima do método `main` e dos métodos de teste.
 
 ---
 
 ## 6. Debug
 
 > Ferramentas para inspecionar o comportamento do programa em tempo de execução.
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Iniciar debug | `F11` | `Shift + F9` | `F5` |
 | Adicionar/remover breakpoint | `Ctrl + Shift + B` | `Ctrl + F8` | `F9` |
 | Continuar execução (até próx. breakpoint) | `F8` | `F9` | `F5` |
 | Avançar passo a passo (Step Over) | `F6` | `F8` | `F10` |
 | Entrar dentro do método (Step Into) | `F5` | `F7` | `F11` |
 | Sair do método (Step Out) | `F7` | `Shift + F8` | `Shift + F11` |
 | Executar até o cursor | — | `Alt + F9` | — |
 | Avaliar expressão | `Ctrl + Shift + I` | `Alt + F8` | Hover sobre variável |
 | Inspecionar variáveis | Painel Variables | Painel Variables | Painel Variables |
 | Modificar valor de variável em tempo real | Painel Variables → Edit | `F2` no painel Variables | — |
 | Adicionar breakpoint condicional | Clique direito no breakpoint | Clique direito no breakpoint | Clique direito no breakpoint |
 
 **Explicação detalhada:**
 
 - **Step Over (`F6/F8/F10`)** — Executa a linha atual completamente e vai para a próxima. Se a linha chama um método, o método é executado por inteiro sem entrar nele.
 - **Step Into (`F5/F7/F11`)** — Entra dentro do método chamado na linha atual, permitindo depurar o interior do método.
 - **Step Out (`F7/Shift+F8/Shift+F11`)** — Sai do método atual, retornando ao chamador. Útil quando você entrou acidentalmente em um método.
 - **IntelliJ `Alt + F8`** — Abre um painel para avaliar qualquer expressão Java no contexto atual do debug. Você pode escrever código e ver o resultado em tempo real, sem parar o programa.
 - **Breakpoint Condicional** — Clique com o botão direito no breakpoint e adicione uma condição Java (ex: `contador > 10`). O programa só vai parar naquele ponto quando a condição for verdadeira, economizando muito tempo em loops longos.
 
 ---
 
 ## 7. Git e Controle de Versão
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Ver alterações / diff do arquivo | `Team → Show Diff` | `Ctrl + D` | `Ctrl + Shift + G` |
 | Commit | `Team → Commit` | `Ctrl + K` | `Ctrl + Shift + G` → Commit |
 | Push | `Team → Push` | `Ctrl + Shift + K` | Botão no painel Git |
 | Pull | `Team → Pull` | `Ctrl + T` | Botão no painel Git |
 | Ver log / histórico | `Team → Show History` | `Alt + 9` (Git Log) | Extensão GitLens |
 | Reverter mudanças no arquivo | `Team → Replace with → HEAD` | `Ctrl + Alt + Z` | `U` (no painel Git) |
 | Abrir painel de controle de versão | `Team Menu` | `Alt + 9` | `Ctrl + Shift + G` |
 | Comparar branch | `Team → Compare` | Branch Popup | Extensão GitLens |
 
 **Explicação detalhada:**
 
 - **Eclipse** — Integração Git via plugin EGit (já incluído). Acesse pelas opções `Team` no menu contextual dos arquivos. A interface é funcional mas menos integrada que as demais.
 - **IntelliJ `Ctrl + K`** — Abre o diálogo de commit com diff visual completo, lista de arquivos modificados e checklist de revisão. Um dos fluxos de commit mais produtivos disponíveis.
 - **IntelliJ `Ctrl + Alt + Z`** — "Rollback": reverte as alterações do arquivo selecionado ou da seleção de linhas para o estado do último commit. Muito útil para desfazer mudanças pontuais.
 - **VS Code `Ctrl + Shift + G`** — Abre o painel Source Control. Para funcionalidades avançadas como blame, log detalhado e comparação de branches, instale a extensão **GitLens**.
 
 ---
 
 ## 8. Gerenciamento de Janelas e Abas
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Alternar entre abas abertas | `Ctrl + F6` | `Ctrl + Tab` | `Ctrl + Tab` |
 | Fechar aba atual | `Ctrl + W` | `Ctrl + F4` | `Ctrl + W` |
 | Fechar todas as abas | `Ctrl + Shift + W` | `Ctrl + Shift + F4` | `Ctrl + K W` |
 | Dividir editor verticalmente | Arrastar aba | `Ctrl + Alt + [` | `Ctrl + \` |
 | Maximizar editor | `Ctrl + M` | `Ctrl + Shift + F12` | `Ctrl + B` (oculta sidebar) |
 | Abrir terminal integrado | — | `Alt + F12` | `` Ctrl + ` `` |
 | Mostrar/ocultar Project Explorer | `Alt + Shift + Q + P` | `Alt + 1` | `Ctrl + Shift + E` |
 | Ir para arquivo aberto recentemente | `Ctrl + E` | `Ctrl + E` | `Ctrl + R` (no `Ctrl + P`) |
 | Focar no editor (sair do explorer) | `F12` | `Esc` | `Ctrl + 1` |
 
 **Explicação detalhada:**
 
 - **IntelliJ `Alt + 1`** — Abre/fecha o Project Explorer. Cada painel lateral tem um número: `Alt + 1` = Project, `Alt + 2` = Bookmarks, `Alt + 6` = Problems, `Alt + 9` = Git. Muito produtivo.
 - **VS Code `` Ctrl + ` ``** — Abre o terminal integrado sem sair da IDE. Você pode criar múltiplos terminais e navegar entre eles.
 - **IntelliJ `Alt + F12`** — Abre o Terminal integrado, similar ao VS Code.
 - **`Ctrl + E`** (Eclipse e IntelliJ) — Mostra a lista de arquivos abertos recentemente para navegação rápida entre eles.
 
 ---
 
 ## 9. Comentários e Formatação
 
 | Ação | Eclipse | IntelliJ IDEA | VS Code |
 |------|---------|---------------|---------|
 | Comentar/descomentar linha | `Ctrl + /` | `Ctrl + /` | `Ctrl + /` |
 | Comentar bloco `/* */` | `Ctrl + Shift + /` | `Ctrl + Shift + /` | `Shift + Alt + A` |
 | Formatar código (arquivo inteiro) | `Ctrl + Shift + F` | `Ctrl + Alt + L` | `Shift + Alt + F` |
 | Formatar seleção | `Ctrl + Shift + F` (com seleção) | `Ctrl + Alt + L` (com seleção) | `Shift + Alt + F` (com seleção) |
 | Indentar linha/seleção | `Tab` | `Tab` | `Tab` |
 | Remover indentação | `Shift + Tab` | `Shift + Tab` | `Shift + Tab` |
 | Gerar JavaDoc | `/**` + Enter | `/**` + Enter | `/**` + Enter |
 | Exibir JavaDoc do símbolo | `F2` ou hover | `Ctrl + Q` | Hover sobre o símbolo |
 
 **Explicação detalhada:**
 
 - **`Ctrl + /`** — Funciona igual nas três IDEs: comenta ou descomenta a linha atual (ou linhas selecionadas) usando `//`. Se já estiver comentado, remove o comentário.
 - **Formatação automática** — Cada IDE usa suas próprias regras de formatação, configuráveis em Settings/Preferences. Recomenda-se configurar um estilo de código padronizado (ex: Google Java Style Guide) e usar o atalho com frequência.
 - **`/**` + Enter** — Em todas as IDEs, digitar `/**` acima de um método e pressionar Enter gera automaticamente o esqueleto do JavaDoc com os parâmetros e o retorno do método já documentados.
 - **IntelliJ `Ctrl + Q`** — Mostra a documentação JavaDoc do símbolo onde o cursor está posicionado, em um popup elegante. No Eclipse e VS Code, basta passar o mouse sobre o símbolo (hover).
 
 ---
 
 ## 10. Dicas Finais
 
 ### 🏆 Os 10 Atalhos Mais Importantes (por IDE)
 
 **Eclipse:**
 1. `Ctrl + Space` — Autocomplete
 2. `Ctrl + 1` — Correção rápida
 3. `F3` — Ir para definição
 4. `Ctrl + Shift + R` — Buscar arquivo
 5. `Alt + Shift + R` — Renomear
 6. `Ctrl + Shift + F` — Formatar
 7. `Ctrl + Shift + O` — Organizar imports
 8. `Alt + Shift + S` — Gerar código
 9. `F11` — Debug
 10. `Ctrl + F11` — Executar
 
 **IntelliJ IDEA:**
 1. `Shift + Shift` — Buscar tudo
 2. `Alt + Enter` — Ação rápida
 3. `Ctrl + B` — Ir para definição
 4. `Shift + F6` — Renomear
 5. `Ctrl + Alt + L` — Formatar
 6. `Alt + Insert` — Gerar código
 7. `Ctrl + W` — Expandir seleção
 8. `Ctrl + K` — Commit
 9. `Alt + F8` — Avaliar expressão (debug)
 10. `Shift + F9` — Debug
 
 **VS Code:**
 1. `Ctrl + P` — Buscar arquivo
 2. `Ctrl + Shift + F` — Buscar em tudo
 3. `F12` — Ir para definição
 4. `F2` — Renomear
 5. `Ctrl + .` — Ação rápida / Quick Fix
 6. `Ctrl + D` — Selecionar próxima ocorrência
 7. `Alt + ↑/↓` — Mover linha
 8. `` Ctrl + ` `` — Terminal integrado
 9. `Ctrl + /` — Comentar linha
 10. `F5` — Executar / Debug
 
 ---
 
 ### 💡 Como Aprender os Atalhos Mais Rápido
 
 1. **Escolha 3 atalhos por semana** e use-os conscientemente até virar hábito.
 2. **Imprima ou deixe visível** um cheatsheet com os atalhos mais usados.
 3. **Desative o mouse temporariamente** durante sessões de prática para forçar o uso do teclado.
 4. **Use o "Key Promoter X"** (plugin do IntelliJ) que avisa quando você faz uma ação com o mouse que tem atalho disponível.
 5. **VS Code**: vá em `File → Preferences → Keyboard Shortcuts` (`Ctrl + K Ctrl + S`) para ver, pesquisar e personalizar todos os atalhos.
 6. **IntelliJ**: `Help → Keyboard Shortcuts PDF` baixa um PDF com todos os atalhos da sua plataforma.
 7. **Eclipse**: `Help → Keys` mostra todos os atalhos e permite configurá-los.
 
 ---
 
 ### ⚙️ Configurando Keymaps
 
 - **IntelliJ** suporta importar keymaps do Eclipse e VS Code: `Settings → Keymap` → selecione "Eclipse" ou "VSCode" para facilitar a migração.
 - **VS Code** tem extensões de keymaps: pesquise "Eclipse Keymap" ou "IntelliJ IDEA Keybindings" no Marketplace.
 - Personalize qualquer atalho conflitante clicando com o botão direito sobre ele nas configurações de teclado de cada IDE.
 
 ---
 
 *Guia elaborado com foco em Java Development. Versões: Eclipse 2023+, IntelliJ IDEA 2023+, VS Code 1.80+.*
