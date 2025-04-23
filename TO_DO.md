## 🔁 1. Automatizar e aprimorar o fluxo básico
Objetivo: Tornar o uso mais rápido e seguro pro dia a dia

- Adicionar a data atual como chave no JSON automaticamente (ex: "2025-04-16").
- Verificar se o dia já existe no arquivo, e evitar sobrescrever sem querer.
- Permitir editar um dia específico.
- Função para listar os registros de um mês inteiro.
- Tratar erros: entrada inválida, arquivos ausentes etc.

## 📁 2. Estruturar por mês
Objetivo: Melhor organização dos dados

- Salvar cada mês em um arquivo separado (2025-04.json).
- Criar um diretório chamado registros/ ou dados/.
- Gerar o nome do arquivo com datetime.date.today().strftime("%Y-%m").
- Ler todos os arquivos e montar um resumo do mês, se quiser.

## 🧠 Algo mais avançado (pra depois)
- Interface simples com Tkinter ou Textual (pra um visual básico) (PyQT?).
- API REST com Flask pra mandar esses dados pra um front.
- Exportar pra CSV ou Excel depois.
- Automatizar envio por e-mail / backup no GitHub.