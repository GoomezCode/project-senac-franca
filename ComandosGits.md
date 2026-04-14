# 🐙 Guia Completo de Comandos Git — Terminal

> **Referência essencial** para o dia a dia com Git no terminal.  
> Desde os primeiros passos até fluxos avançados de trabalho em equipe.

---

## 📋 Índice

1. [Configuração Inicial](#1-configuração-inicial)
2. [Criar e Clonar Repositórios](#2-criar-e-clonar-repositórios)
3. [Status e Inspeção](#3-status-e-inspeção)
4. [Staging e Commit](#4-staging-e-commit)
5. [Branches](#5-branches)
6. [Merge e Rebase](#6-merge-e-rebase)
7. [Repositório Remoto (Remote)](#7-repositório-remoto-remote)
8. [Desfazer e Corrigir Erros](#8-desfazer-e-corrigir-erros)
9. [Stash — Guardar Mudanças Temporariamente](#9-stash--guardar-mudanças-temporariamente)
10. [Tags](#10-tags)
11. [Log e Histórico](#11-log-e-histórico)
12. [Diff — Comparar Mudanças](#12-diff--comparar-mudanças)
13. [Fluxos de Trabalho Comuns](#13-fluxos-de-trabalho-comuns)
14. [Aliases Úteis](#14-aliases-úteis)
15. [Cheatsheet Rápido](#15-cheatsheet-rápido)

---

## 1. Configuração Inicial

> Configure sua identidade antes de qualquer coisa. Essas informações ficam registradas em cada commit.

```bash
# Definir seu nome (aparece nos commits)
git config --global user.name "Seu Nome"

# Definir seu e-mail (deve ser o mesmo da sua conta GitHub/GitLab)
git config --global user.email "seu@email.com"

# Definir o editor padrão para mensagens de commit (escolha um)
git config --global core.editor "code --wait"    # VS Code
git config --global core.editor "nano"           # Nano
git config --global core.editor "vim"            # Vim

# Definir o nome padrão da branch principal
git config --global init.defaultBranch main

# Ativar cores no terminal para melhor leitura
git config --global color.ui auto

# Ver todas as configurações atuais
git config --list

# Ver uma configuração específica
git config user.name

# Ver onde cada configuração está definida
git config --list --show-origin
```

**Explicação:**
- `--global` aplica a configuração para todos os repositórios do seu usuário no sistema. Sem ele, a configuração vale apenas para o repositório atual.
- O e-mail deve coincidir com o cadastrado no GitHub/GitLab para que os commits apareçam vinculados ao seu perfil.
- O editor é aberto quando você digita `git commit` sem `-m`, para escrever mensagens longas.

---

## 2. Criar e Clonar Repositórios

```bash
# Inicializar um novo repositório Git na pasta atual
git init

# Inicializar com nome de branch personalizado
git init -b main

# Clonar um repositório remoto (baixa tudo)
git clone https://github.com/usuario/repositorio.git

# Clonar em uma pasta com nome personalizado
git clone https://github.com/usuario/repositorio.git meu-projeto

# Clonar apenas uma branch específica
git clone -b nome-da-branch https://github.com/usuario/repositorio.git

# Clonar sem o histórico completo (mais rápido para repos grandes)
git clone --depth 1 https://github.com/usuario/repositorio.git

# Clonar via SSH (requer chave SSH configurada)
git clone git@github.com:usuario/repositorio.git
```

**Explicação:**
- `git init` cria a pasta oculta `.git/` que controla todo o versionamento. Nunca delete essa pasta.
- `git clone` já configura automaticamente o remote `origin` apontando para o repositório de origem.
- `--depth 1` faz um "shallow clone", trazendo apenas o último commit. Ideal para CI/CD ou quando você não precisa do histórico antigo.
- SSH é mais seguro e prático que HTTPS para uso frequente, pois não pede senha a cada push/pull.

---

## 3. Status e Inspeção

> Antes de qualquer ação, verifique o estado atual do repositório.

```bash
# Ver o estado atual: arquivos modificados, staged e untracked
git status

# Versão compacta do status
git status -s
# M = modificado, A = adicionado, ? = não rastreado, D = deletado

# Ver status incluindo arquivos ignorados pelo .gitignore
git status --ignored

# Listar arquivos rastreados pelo Git
git ls-files

# Ver quem escreveu cada linha de um arquivo (blame)
git blame nome-do-arquivo.java

# Ver quem escreveu cada linha com data e commit
git blame -l nome-do-arquivo.java

# Ver informações detalhadas de um commit específico
git show abc1234

# Ver apenas os arquivos alterados em um commit
git show --stat abc1234

# Ver o conteúdo de um arquivo em um commit específico
git show abc1234:src/Main.java
```

**Explicação:**
- `git status` é o comando mais usado no dia a dia. Execute-o com frequência para saber exatamente o que está acontecendo no repositório.
- O status compacto (`-s`) mostra duas colunas: a primeira é o estado na staging area, a segunda é o estado no working directory.
- `git blame` é essencial para descobrir quem introduziu uma linha de código e em qual commit, facilitando investigações de bugs.

---

## 4. Staging e Commit

> O Git tem três áreas: **Working Directory** (seus arquivos), **Staging Area** (o que vai no próximo commit) e **Repository** (histórico de commits).

```bash
# ── STAGING (preparar para commit) ──────────────────────────

# Adicionar um arquivo específico à staging area
git add nome-do-arquivo.java

# Adicionar todos os arquivos modificados e novos
git add .

# Adicionar todos os arquivos de uma pasta específica
git add src/

# Adicionar arquivos por padrão (ex: todos os .java)
git add "*.java"

# Adicionar interativamente (escolher trecho por trecho)
git add -p
# Vai perguntando: y = adicionar, n = pular, s = dividir o hunk, e = editar

# Ver o que está na staging area (pronto para commit)
git diff --staged


# ── COMMIT (salvar no histórico) ────────────────────────────

# Commit com mensagem curta inline
git commit -m "feat: adiciona endpoint de login"

# Commit com mensagem longa (abre o editor configurado)
git commit

# Adicionar todos os arquivos modificados E commitar (não inclui arquivos novos)
git commit -am "fix: corrige validação de e-mail"

# Corrigir o último commit (mensagem ou arquivos esquecidos)
git commit --amend -m "feat: adiciona endpoint de login com validação"

# Commitar com data personalizada
git commit -m "feat: nova feature" --date="2024-01-15T10:00:00"


# ── BOAS PRÁTICAS DE MENSAGEM (Conventional Commits) ────────
# feat:     nova funcionalidade
# fix:      correção de bug
# docs:     alteração em documentação
# style:    formatação, sem mudança de lógica
# refactor: refatoração de código
# test:     adicionar ou corrigir testes
# chore:    tarefas de build, configs, etc.
```

**Explicação:**
- A **staging area** (index) é uma área intermediária entre seus arquivos e o commit. Isso permite commitar apenas parte das mudanças.
- `git add -p` é extremamente poderoso: permite selecionar partes específicas de um arquivo para commitar, mantendo outras mudanças fora. Ideal para commits atômicos e organizados.
- `git commit --amend` **reescreve** o último commit. Use **apenas se ainda não fez push** para o repositório remoto, pois muda o histórico.
- `git commit -am` é um atalho mas ignora arquivos novos (untracked). Prefira `git add .` + `git commit -m` para ter mais controle.
- **Conventional Commits** é um padrão amplamente adotado que facilita geração automática de changelogs e versionamento semântico.

---

## 5. Branches

> Branches permitem trabalhar em funcionalidades isoladas sem afetar o código principal.

```bash
# ── LISTAR BRANCHES ─────────────────────────────────────────

# Listar branches locais (a atual aparece com *)
git branch

# Listar branches remotas
git branch -r

# Listar todas (locais + remotas)
git branch -a

# ── CRIAR BRANCHES ──────────────────────────────────────────

# Criar uma nova branch
git branch nome-da-branch

# Criar e já mudar para a nova branch
git checkout -b nome-da-branch

# Forma moderna (Git 2.23+)
git switch -c nome-da-branch

# Criar branch a partir de um commit ou tag específica
git checkout -b hotfix abc1234

# Criar branch local rastreando uma branch remota
git checkout -b feature/login origin/feature/login

# ── MUDAR DE BRANCH ─────────────────────────────────────────

# Mudar para uma branch existente
git checkout nome-da-branch

# Forma moderna
git switch nome-da-branch

# Voltar para a branch anterior
git checkout -
git switch -

# ── RENOMEAR E DELETAR ──────────────────────────────────────

# Renomear a branch atual
git branch -m novo-nome

# Renomear outra branch
git branch -m nome-antigo novo-nome

# Deletar branch local (seguro: só deleta se já foi merged)
git branch -d nome-da-branch

# Deletar branch local forçado (mesmo sem merge)
git branch -D nome-da-branch

# Deletar branch remota
git push origin --delete nome-da-branch

# ── VERIFICAR BRANCHES MERGED ───────────────────────────────

# Ver branches que já foram mergeadas na branch atual
git branch --merged

# Ver branches que ainda NÃO foram mergeadas
git branch --no-merged
```

**Explicação:**
- Use branches para cada feature, bugfix ou tarefa. O padrão `feature/nome-da-feature` e `fix/nome-do-bug` é amplamente adotado.
- `git switch` é o comando moderno introduzido no Git 2.23 para substituir `git checkout` na função de trocar branches. O `checkout` ainda funciona e é muito comum.
- `git branch -d` (minúsculo) é seguro: o Git se recusa a deletar se a branch não foi mergeada. Use `-D` (maiúsculo) com cautela.
- Sempre delete branches remotas após o merge no GitHub/GitLab para manter o repositório organizado.

---

## 6. Merge e Rebase

> Integrar mudanças de uma branch em outra, de duas formas diferentes.

```bash
# ── MERGE ────────────────────────────────────────────────────

# Trazer as mudanças de outra branch para a atual
git merge nome-da-branch

# Merge sem fast-forward (sempre cria um commit de merge)
git merge --no-ff nome-da-branch

# Merge squash (junta todos os commits em um só, sem commit automático)
git merge --squash nome-da-branch
git commit -m "feat: adiciona módulo de pagamento"

# Abortar um merge com conflito em andamento
git merge --abort


# ── REBASE ──────────────────────────────────────────────────

# Reaplicar os commits da branch atual em cima de outra branch
git rebase main

# Rebase interativo: reescrever/reorganizar os últimos N commits
git rebase -i HEAD~3
# Opções em cada commit:
# pick   = manter o commit
# reword = manter, mas editar a mensagem
# edit   = pausar para fazer alterações
# squash = juntar com o commit anterior (mantém ambas as mensagens)
# fixup  = juntar com o commit anterior (descarta a mensagem)
# drop   = remover o commit completamente

# Abortar um rebase em andamento
git rebase --abort

# Continuar rebase após resolver conflito
git rebase --continue


# ── RESOLVER CONFLITOS ──────────────────────────────────────
# 1. O Git marca os conflitos no arquivo assim:
#    <<<<<<< HEAD
#    seu código
#    =======
#    código da outra branch
#    >>>>>>> nome-da-branch
#
# 2. Edite o arquivo manualmente e escolha o que manter
# 3. Marque o conflito como resolvido:
git add arquivo-com-conflito.java
# 4. Continue o merge ou rebase:
git commit       # para merge
git rebase --continue  # para rebase


# ── QUANDO USAR CADA UM ──────────────────────────────────────
# Merge:  preserva o histórico completo, cria um commit de merge.
#         Ideal para integrar branches principais (main ← feature).
# Rebase: histórico linear e limpo, sem commits de merge.
#         Ideal para atualizar sua branch feature com o main.
```

**Explicação:**
- **Merge** preserva todo o histórico, mostrando exatamente quando e como as branches foram integradas. Mais seguro e rastreável.
- **Rebase** reescreve o histórico de commits, criando uma linha do tempo linear. Facilita a leitura do `git log`, mas **nunca faça rebase de branches públicas** que outras pessoas estão usando — isso causa problemas graves para o time.
- `git rebase -i` (interativo) é uma das ferramentas mais poderosas do Git para limpar o histórico antes de um merge: junte commits pequenos demais, corrija mensagens, remova commits errados.
- `--squash` junta todos os commits da feature em um único commit limpo, útil para manter o histórico do main organizado.

---

## 7. Repositório Remoto (Remote)

> Sincronizar seu trabalho local com servidores como GitHub, GitLab ou Bitbucket.

```bash
# ── GERENCIAR REMOTES ────────────────────────────────────────

# Ver os remotes configurados
git remote -v

# Adicionar um remote
git remote add origin https://github.com/usuario/repo.git

# Adicionar um segundo remote (ex: fork upstream)
git remote add upstream https://github.com/original/repo.git

# Alterar a URL de um remote
git remote set-url origin https://github.com/usuario/novo-repo.git

# Remover um remote
git remote remove origin

# Renomear um remote
git remote rename origin novo-nome


# ── FETCH, PULL e PUSH ──────────────────────────────────────

# Baixar mudanças do remote SEM fazer merge (apenas atualiza referências)
git fetch origin

# Baixar mudanças de todos os remotes
git fetch --all

# Baixar e já fazer merge na branch atual (fetch + merge)
git pull

# Pull com rebase ao invés de merge (histórico mais limpo)
git pull --rebase

# Pull de uma branch específica
git pull origin main

# Enviar commits da branch atual para o remote
git push

# Enviar pela primeira vez e configurar o upstream tracking
git push -u origin nome-da-branch

# Forçar push (CUIDADO: reescreve o histórico remoto)
git push --force

# Force push seguro (falha se o remote mudou desde seu último pull)
git push --force-with-lease

# Enviar todas as branches
git push --all origin

# Enviar todas as tags
git push --tags


# ── SINCRONIZAR FORK COM UPSTREAM ───────────────────────────

# Buscar mudanças do repositório original
git fetch upstream

# Aplicar na sua main local
git checkout main
git merge upstream/main

# Enviar atualização para seu fork
git push origin main
```

**Explicação:**
- **`git fetch`** baixa as mudanças do remote mas **não altera seus arquivos**. Seguro para ver o que mudou antes de integrar.
- **`git pull`** é um atalho para `git fetch` + `git merge`. Prefira `git pull --rebase` para manter o histórico mais limpo.
- **`git push -u`** (ou `--set-upstream`): só precisa usar na primeira vez que envia uma branch. Depois, `git push` sem argumentos já sabe para onde enviar.
- **`git push --force`** é perigoso em branches compartilhadas: sobrescreve o histórico remoto e pode apagar commits de colegas. Prefira sempre `--force-with-lease`, que verifica se o remote não foi modificado por outra pessoa antes de forçar.
- **upstream** é a convenção para o repositório original de um fork. Permite sincronizar seu fork com as atualizações do projeto original.

---

## 8. Desfazer e Corrigir Erros

> Um dos pontos mais importantes do Git: como voltar atrás com segurança.

```bash
# ── DESFAZER ANTES DO COMMIT ────────────────────────────────

# Descartar mudanças em um arquivo (volta ao último commit)
git checkout -- nome-do-arquivo.java
# Forma moderna:
git restore nome-do-arquivo.java

# Descartar TODAS as mudanças não commitadas (irreversível!)
git restore .
git checkout -- .

# Remover arquivo da staging area (mantém as mudanças no arquivo)
git restore --staged nome-do-arquivo.java
# Equivalente antigo:
git reset HEAD nome-do-arquivo.java


# ── DESFAZER COMMITS (sem alterar arquivos) ──────────────────

# Desfazer o último commit, mantendo as mudanças na staging area
git reset --soft HEAD~1

# Desfazer o último commit, mantendo as mudanças no working directory
git reset --mixed HEAD~1   # (comportamento padrão do reset)

# Desfazer os últimos 3 commits
git reset --mixed HEAD~3

# Desfazer até um commit específico
git reset --mixed abc1234


# ── DESFAZER COMMITS (descartando arquivos também) ──────────

# PERIGO: desfaz o commit E descarta as mudanças nos arquivos
git reset --hard HEAD~1

# Voltar para um commit específico descartando tudo depois
git reset --hard abc1234

# Após um reset --hard "acidental", recuperar com reflog
git reflog
git reset --hard HEAD@{2}


# ── REVERTER COMMIT (forma segura para branches públicas) ────

# Cria um novo commit que desfaz as mudanças de um commit anterior
git revert abc1234

# Reverter sem abrir o editor (usa mensagem padrão)
git revert abc1234 --no-edit

# Reverter múltiplos commits
git revert abc1234..def5678

# Reverter o último commit
git revert HEAD


# ── RECUPERAR ARQUIVOS DELETADOS ────────────────────────────

# Recuperar arquivo deletado que ainda não foi commitado
git restore nome-do-arquivo.java

# Recuperar arquivo deletado de um commit específico
git checkout abc1234 -- src/Main.java

# Ver commits que deletaram um arquivo
git log --all --full-history -- "src/Main.java"
```

**Explicação:**

| Comando | Altera arquivos? | Altera histórico? | Seguro para remotes? |
|---------|-----------------|-------------------|----------------------|
| `git restore` | Sim (descarta) | Não | ✅ Sim |
| `git reset --soft` | Não | Sim (local) | ⚠️ Não |
| `git reset --mixed` | Não | Sim (local) | ⚠️ Não |
| `git reset --hard` | Sim (descarta) | Sim (local) | ⚠️ Não |
| `git revert` | Sim (novo commit) | Não (adiciona) | ✅ Sim |

- **`git revert`** é a forma **segura** de desfazer commits em branches públicas, pois cria um novo commit em vez de reescrever o histórico.
- **`git reset --hard`** é destrutivo: você perde as mudanças nos arquivos. Use com muito cuidado.
- **`git reflog`** é sua rede de segurança: registra tudo que você fez no repositório local, mesmo operações que "apagam" commits. Se você errou um `reset --hard`, o reflog pode salvar seu trabalho.

---

## 9. Stash — Guardar Mudanças Temporariamente

> Salve mudanças que ainda não estão prontas para commit, sem perdê-las ao trocar de branch.

```bash
# Guardar as mudanças atuais no stash
git stash

# Guardar com uma descrição personalizada
git stash push -m "WIP: implementando validação do formulário"

# Guardar incluindo arquivos novos (untracked)
git stash push -u -m "descrição"

# Guardar incluindo arquivos ignorados também
git stash push -a

# Listar todos os stashes salvos
git stash list
# Resultado: stash@{0}: WIP on main: abc1234 commit message
#            stash@{1}: WIP: implementando validação...

# Aplicar o stash mais recente (mantém no stash)
git stash apply

# Aplicar o stash mais recente e removê-lo da lista
git stash pop

# Aplicar um stash específico
git stash apply stash@{2}

# Ver o conteúdo de um stash sem aplicar
git stash show
git stash show -p stash@{1}   # mostra o diff completo

# Remover o stash mais recente
git stash drop

# Remover um stash específico
git stash drop stash@{2}

# Remover TODOS os stashes (cuidado!)
git stash clear

# Criar uma branch a partir de um stash
git stash branch nova-branch stash@{1}
```

**Explicação:**
- Use `git stash` quando precisar trocar de branch urgentemente (ex: um bug crítico apareceu) mas não quer commitar código incompleto.
- `git stash pop` = `git stash apply` + `git stash drop`. Prefira `pop` quando quiser aplicar e já remover da lista.
- Por padrão, o stash não guarda arquivos novos (untracked). Use `-u` para incluí-los.
- `git stash branch` cria uma nova branch já com as mudanças do stash aplicadas, resolvendo possíveis conflitos de uma vez.

---

## 10. Tags

> Marque pontos específicos no histórico, como releases e versões.

```bash
# Listar todas as tags
git tag

# Listar tags com padrão
git tag -l "v1.*"

# Criar tag leve (apenas um ponteiro para o commit)
git tag v1.0.0

# Criar tag anotada (recomendado: inclui autor, data e mensagem)
git tag -a v1.0.0 -m "Release versão 1.0.0"

# Criar tag em um commit específico
git tag -a v1.0.0 abc1234 -m "Release versão 1.0.0"

# Ver detalhes de uma tag
git show v1.0.0

# Enviar uma tag para o remote
git push origin v1.0.0

# Enviar todas as tags para o remote
git push origin --tags

# Deletar tag local
git tag -d v1.0.0

# Deletar tag remota
git push origin --delete v1.0.0

# Voltar o código para o estado de uma tag
git checkout v1.0.0
```

**Explicação:**
- **Tags leves** são apenas um ponteiro para um commit, sem informação extra.
- **Tags anotadas** (`-a`) são objetos Git completos com autor, data, mensagem e podem ser assinadas com GPG. São a forma recomendada para marcar releases.
- Siga o **Versionamento Semântico (SemVer)**: `MAJOR.MINOR.PATCH` (ex: `v2.1.3`). Major = mudança incompatível, Minor = nova funcionalidade compatível, Patch = correção de bug.
- Tags **não são enviadas automaticamente** com `git push`. Você precisa enviá-las explicitamente com `--tags`.

---

## 11. Log e Histórico

> Visualize o histórico de commits de diferentes formas.

```bash
# Ver o histórico de commits
git log

# Histórico compacto (uma linha por commit)
git log --oneline

# Histórico com gráfico de branches
git log --oneline --graph --all

# Histórico com gráfico decorado (mais bonito)
git log --oneline --graph --all --decorate

# Ver os últimos N commits
git log -5

# Ver commits de um autor específico
git log --author="João Silva"

# Ver commits de um período
git log --after="2024-01-01" --before="2024-06-30"

# Ver commits que modificaram um arquivo
git log --follow -- src/Main.java

# Buscar commits pela mensagem
git log --grep="fix:"

# Ver commits que adicionaram ou removeram um texto específico
git log -S "nome-da-funcao"

# Histórico de tudo que você fez localmente (incluindo resets)
git reflog

# Ver o diff de cada commit no log
git log -p

# Resumo das mudanças por arquivo em cada commit
git log --stat

# Histórico bonito personalizado
git log --pretty=format:"%C(yellow)%h%Creset %C(blue)%an%Creset %C(green)%ar%Creset %s"
```

**Explicação:**
- `git log --oneline --graph --all` é o comando mais útil para visualizar a estrutura de branches no terminal. Configure um alias para ele.
- `git log -S "texto"` (pickaxe) busca todos os commits que adicionaram ou removeram aquela string exata. Extremamente útil para rastrear quando uma linha de código apareceu ou foi removida.
- `git reflog` é diferente de `git log`: enquanto `log` mostra o histórico do projeto, `reflog` mostra o histórico das suas ações locais (checkout, reset, merge, etc.), sendo sua rede de segurança para recuperar situações complicadas.

---

## 12. Diff — Comparar Mudanças

```bash
# Ver mudanças não staged (working directory vs último commit)
git diff

# Ver mudanças staged (o que vai no próximo commit)
git diff --staged
git diff --cached  # mesmo comando, nome alternativo

# Comparar dois commits
git diff abc1234 def5678

# Comparar duas branches
git diff main feature/login

# Comparar um arquivo específico entre duas branches
git diff main feature/login -- src/Main.java

# Ver apenas os nomes dos arquivos alterados
git diff --name-only

# Ver resumo estatístico das mudanças
git diff --stat

# Ver diff de um arquivo específico
git diff src/Main.java

# Comparar com a versão de um commit específico
git diff HEAD~3 src/Main.java
```

**Explicação:**
- `git diff` sem argumentos compara seus arquivos atuais com o último commit (HEAD), mostrando o que ainda não foi para a staging area.
- `git diff --staged` mostra o que está na staging area e será incluído no próximo commit. Use antes de commitar para revisar o que vai entrar.
- `git diff main feature/login` é muito útil antes de um merge para ver exatamente o que será integrado.

---

## 13. Fluxos de Trabalho Comuns

> Sequências de comandos para situações do dia a dia.

### 🚀 Fluxo básico diário

```bash
# 1. Atualizar sua branch com as últimas mudanças do time
git pull --rebase origin main

# 2. Criar branch para sua tarefa
git switch -c feature/minha-feature

# 3. Desenvolver... editar arquivos...

# 4. Ver o que mudou
git status
git diff

# 5. Adicionar e commitar
git add .
git commit -m "feat: adiciona funcionalidade X"

# 6. Enviar para o remote
git push -u origin feature/minha-feature

# 7. Abrir Pull Request no GitHub/GitLab (via interface web)

# 8. Após o merge, limpar a branch local
git switch main
git pull
git branch -d feature/minha-feature
```

---

### 🐛 Hotfix urgente em produção

```bash
# 1. Guardar trabalho em andamento
git stash push -m "WIP: feature em progresso"

# 2. Ir para a main e atualizar
git switch main
git pull origin main

# 3. Criar branch de hotfix
git switch -c hotfix/corrige-bug-login

# 4. Corrigir o bug e commitar
git add .
git commit -m "fix: corrige validação de sessão no login"

# 5. Enviar e abrir PR urgente
git push -u origin hotfix/corrige-bug-login

# 6. Após o merge, voltar ao trabalho anterior
git switch feature/minha-feature
git stash pop
```

---

### 🔄 Atualizar branch feature com mudanças do main

```bash
# Opção 1: Rebase (histórico linear — recomendado)
git switch feature/minha-feature
git fetch origin
git rebase origin/main

# Opção 2: Merge
git switch feature/minha-feature
git merge main

# Se houver conflitos em qualquer opção:
# 1. Edite os arquivos conflitantes
# 2. git add arquivo-resolvido.java
# 3. git rebase --continue  (ou git merge --continue)
```

---

### 🧹 Limpeza de branches antigas

```bash
# Ver branches já mergeadas
git branch --merged main

# Deletar todas as branches locais já mergeadas (exceto main e develop)
git branch --merged main | grep -v "^\*\|main\|develop" | xargs git branch -d

# Remover referências a branches remotas que já foram deletadas
git remote prune origin

# Ver o que seria removido antes de executar
git remote prune origin --dry-run
```

---

## 14. Aliases Úteis

> Configure atalhos para os comandos mais usados no seu `~/.gitconfig`.

```bash
# Configurar aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.sw switch
git config --global alias.br branch
git config --global alias.cm "commit -m"
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.last "log -1 HEAD"
git config --global alias.unstage "restore --staged"
git config --global alias.undo "reset --soft HEAD~1"
git config --global alias.aliases "config --get-regexp alias"

# Após configurar, você pode usar assim:
git st          # git status
git co main     # git checkout main
git lg          # log bonito com gráfico
git undo        # desfaz último commit mantendo arquivos
git aliases     # lista todos os aliases configurados
```

**Ou edite diretamente o arquivo `~/.gitconfig`:**

```ini
[alias]
    st  = status
    co  = checkout
    sw  = switch
    br  = branch
    cm  = commit -m
    lg  = log --oneline --graph --all --decorate
    last = log -1 HEAD
    unstage = restore --staged
    undo = reset --soft HEAD~1
    aliases = config --get-regexp alias
    # Mostra as branches mais recentemente usadas
    recent = branch --sort=-committerdate --format='%(refname:short)' -10
```

---

## 15. Cheatsheet Rápido

> Referência rápida dos comandos mais usados no dia a dia.

```
── SETUP ──────────────────────────────────────────────────────
git config --global user.name "Nome"        Configura nome
git config --global user.email "email"      Configura e-mail

── INICIAR ────────────────────────────────────────────────────
git init                                    Novo repositório
git clone <url>                             Clonar repositório

── STATUS ─────────────────────────────────────────────────────
git status                                  Estado atual
git status -s                               Estado compacto
git log --oneline --graph --all             Histórico visual

── STAGING & COMMIT ───────────────────────────────────────────
git add .                                   Adicionar tudo
git add <arquivo>                           Adicionar arquivo
git add -p                                  Adicionar parcialmente
git commit -m "mensagem"                    Commitar
git commit --amend                          Corrigir último commit

── BRANCHES ───────────────────────────────────────────────────
git branch                                  Listar branches
git switch -c <branch>                      Criar e entrar
git switch <branch>                         Trocar de branch
git branch -d <branch>                      Deletar branch
git merge <branch>                          Fazer merge

── REMOTE ─────────────────────────────────────────────────────
git fetch                                   Baixar sem merge
git pull                                    Baixar e merge
git pull --rebase                           Baixar com rebase
git push                                    Enviar commits
git push -u origin <branch>                 Enviar nova branch
git push --force-with-lease                 Force push seguro

── DESFAZER ───────────────────────────────────────────────────
git restore <arquivo>                       Descartar mudanças
git restore --staged <arquivo>              Tirar da staging
git reset --soft HEAD~1                     Desfazer commit (mantém arquivos)
git reset --hard HEAD~1                     Desfazer commit (APAGA arquivos)
git revert <commit>                         Desfazer com segurança
git stash                                   Guardar temporariamente
git stash pop                               Recuperar do stash

── INSPECIONAR ────────────────────────────────────────────────
git diff                                    Ver mudanças não staged
git diff --staged                           Ver mudanças staged
git log -S "texto"                          Buscar por conteúdo
git blame <arquivo>                         Ver autor por linha
git reflog                                  Histórico de ações locais
```

---

### 🛡️ Regras de Ouro do Git

1. **Nunca faça `rebase` ou `reset` em branches públicas** que outras pessoas estão usando.
2. **Prefira `revert`** para desfazer commits já enviados ao remote.
3. **Use `--force-with-lease`** no lugar de `--force` sempre que possível.
4. **Faça commits pequenos e frequentes** com mensagens descritivas.
5. **Sempre faça `git pull --rebase`** antes de começar a trabalhar para evitar divergências.
6. **Nunca commite credenciais** (senhas, tokens, chaves API). Configure o `.gitignore` antes do primeiro commit.
7. **Use o `git reflog`** quando achar que perdeu algo — o Git raramente apaga dados permanentemente.

---

*Guia elaborado para Git 2.30+. A maioria dos comandos funciona em versões anteriores, exceto `git switch` e `git restore` (introduzidos no Git 2.23).*
