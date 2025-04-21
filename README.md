# Controle de Ponto (Reescrita em Python)

Este repositório contém um projeto pessoal de **controle de ponto**, originalmente desenvolvido em outra linguagem e agora **reescrito em Python**. A proposta é registrar os horários de entrada e saída de dois turnos diários, de forma simples, utilizando a biblioteca `datetime`.

## 🧠 Contexto

Esse é um projeto antigo meu, que estou trazendo de volta à vida como forma de aprendizado e prática em Python. A ideia é reconstruir o projeto, melhorando a estrutura, legibilidade e aproveitando os recursos nativos da linguagem.

## 🔁 Evolução do Projeto

O desenvolvimento está sendo versionado aos poucos, conforme o código vai sendo aprimorado. Cada versão traz uma melhoria ou refatoração, e todas estão sendo **commitadas no GitHub**, para acompanhar a evolução.
Até a versão 7 houve apenas o aprimoramento em cima do código inicial.
A partir da ***versão 8*** o foco é os - [📌 Próximos passos](#-próximos-passos)

### ✔️ Versão 1 (V1)
- Estrutura baseada em várias classes (`segundo`, `minuto`, `hora`, `dia`, etc.).
- Alto nível de abstração, mas também complexidade desnecessária.
- Métodos internos com sintaxe confusa e chamadas incorretas.
- Utilização de herança entre `hora`, `minuto` e `segundo`, o que tornava a manipulação dos dados mais difícil.


### ⚙️ Versão 7 (V7)

- Reestruturação total da classe `dia`.
- Uso direto da biblioteca `datetime` para manipular horários.
- Entrada dos dados via `input`, convertendo para `datetime.time`.
- Armazenamento dos horários em atributos simples.
- Métodos claros: `set_turnos()` para preencher os dados e `get_turnos()` para retornar todos os horários.


### ⚙️ Versão 8 (V8)

- Manipulando arquivo `.json` para leitura e escrita.

## 📌 Próximos passos

- Deixar esse código ainda mais bonito.
- Viabilizar salvamento automático do ponto também.
- Criar uma interface mais amigável para visualização dos horários.
- Armazenar os dados em arquivos (como `.json` ou `.csv`).
- Adicionar suporte para múltiplos dias ou até um mês completo.
- Tratar erros de entrada de dados (validação dos horários).

## 🚀 Objetivo

Além de reviver um projeto antigo, este repositório também serve como **diário de aprendizado em Python**, marcando cada avanço de forma clara. Cada commit conta uma história da evolução da lógica, da estrutura e da forma de pensar.

Feito com dedicação, nostalgia e aprendizado. 😄
