#  Catálogo de Filmes — Projeto Web em Flask

Este é um sistema simples de **catálogo de filmes**, desenvolvido com **Python + Flask**, permitindo **cadastrar, listar, editar e apagar filmes**, incluindo **upload de imagens**.

Desenvolvedoras:

* **Emanuella de Fátima Oliveira de Sousa**
* **Phamela Julia Sena da Silva**
* **Hayanna Yohara Cavalcante de Castro**

---

##  O que é um Catálogo?

Um **catálogo** é uma aplicação que organiza itens de forma estruturada, permitindo visualizar seus dados e realizar operações como adicionar, editar e excluir.

Neste caso, nosso catálogo armazena:

* Título do filme
* Ano de lançamento
* Descrição
* Foto
* ID gerado automaticamente

---

##  Lógica por Trás do Sistema

O Flask utiliza o padrão **MVC**:

* **Models** → Representam os dados (classe Filme)
* **Views** → Arquivos HTML (templates)
* **Controllers** → As rotas dentro de `views.py`

Quando um usuário acessa uma rota:

1. O Flask recebe a URL
2. A função correspondente é executada
3. Ela consulta o banco de dados se necessário
4. Renderiza um template HTML
5. Envia o resultado ao navegador

O fluxo é simples, mas extremamente poderoso.

---

##  Por que existe a pasta `.venv`?

A pasta **`.venv`** é o *Ambiente Virtual* do Python.

Ela serve para:

* Isolar as versões das bibliotecas do projeto
* Evitar conflitos com outras aplicações
* Manter o projeto organizado
* Permitir que outros desenvolvedores instalem apenas o necessário

Tudo o que o Flask precisa para rodar fica dentro dessa pasta.

---

##  Explicação das Rotas

###  ** /**

Exibe a página inicial do site.

---

### 🎥 **GET /filmes**

Lista todos os filmes cadastrados no banco de dados.

---

###  **GET /adicionar**

Mostra o formulário de cadastro de filmes.

---

###  **POST /adicionar**

Recebe os dados enviados e salva no banco.

Processos internos:

* Validação do formulário
* Conversão da imagem para base64
* Inserção no banco
* Redirecionamento para `/filmes`

---

###  **GET /editar/<id>**

Exibe o formulário de edição preenchido com os dados do filme.

---

###  **POST /editar/<id>**

Atualiza o filme no banco.

Processos:

* Validação
* Atualização dos campos
* Substituição da imagem caso enviada
* Redirecionamento para a lista

---

###  **GET /apagar/<id>**

Exibe uma página pedindo confirmação antes de excluir.

---

###  **POST /apagar/<id>**

Apaga o registro permanentemente do banco de dados.

---

## Estilização (CSS)

Todo o estilo está em:

```
app/static/css/style.css
```

Inclui:

* Cabeçalho fixo
* Tabela estilizada e centralizada
* Botões padronizados
* Layout responsivo

O CSS é carregado via:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

Colocado dentro de `base.html` para que **todas as páginas** recebam o estilo automaticamente.

---

## 💽 Banco de Dados

O Flask utiliza **SQLite** (arquivo `.db`) por padrão.

A classe `Filme` possui:

```python
titulo
ano
foto_base64
```

---

##  Como Rodar o Projeto

1. Ativar a venv:

   ```
   .venv/Scripts/activate
   ```
2. Instalar dependências:

   ```
   pip install -r requirements.txt
   ```
3. Executar:

   ```
   flask run
   ```

---

##  Conclusão

Este projeto demonstra:

* uso de rotas
* formulários Flask
* upload de imagens
* uso de SQLite
* templates Jinja
* ambiente virtual `.venv`
* organização MVC



---
