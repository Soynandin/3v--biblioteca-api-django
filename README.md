# Sistema de Gerenciamento de Livros e Coleções - API

## Fernando Silva Ferreira

Este projeto é uma API RESTful desenvolvida em Django REST Framework para gerenciar livros, categorias, autores e coleções. Inclui funcionalidades para autenticação, permissões personalizadas e geração de documentação automática.

## Funcionalidade
- **Livros:**
    Adicionar, listar, detalhar, atualizar e excluir livros.
    Filtragem por título, autor e categoria.
    Ordenação por título, autor, categoria e data de publicação.

- **Categorias:**
    Adicionar, listar, detalhar, atualizar e excluir categorias.
    Filtragem por nome.

- **Autores:**
    Adicionar, listar, detalhar, atualizar e excluir autores.
    Filtragem por nome.

- **Coleções:**
    Associar coleções de livros a um usuário autenticado.
    Listar, detalhar, criar, atualizar e excluir coleções.
    Filtragem por nome e colecionador.

O sistema permite que os usuários criem coleções de livros e as associem a um **colecionador** (usuário autenticado). Cada coleção pode conter diversos livros e é visível para outros usuários, mas apenas o colecionador tem permissão para editar ou excluir sua coleção. A API também possui endpoints para listar, criar, editar e excluir coleções.

- **Autenticação:**
    Implementada com JWT usando a biblioteca rest_framework_simplejwt.

- **Documentação:**
    Geração automática de documentação Swagger e Redoc usando drf-spectacular.

### Recursos

- **Coleção**: Representa um conjunto de livros que um usuário (colecionador) pode criar e gerenciar.
- **Autenticação**: Utiliza **JWT (JSON Web Tokens)** para autenticação de usuários, permitindo que apenas usuários autenticados possam criar ou modificar coleções.
- **Permissões**: Apenas o colecionador (usuário que criou a coleção) pode editar ou excluir a coleção. Usuários não autenticados podem apenas visualizar as coleções.
- **Documentação da API**: A API é documentada utilizando **drf-spectacular**, facilitando o uso por desenvolvedores externos.
- **CORS**: Configuração de **Cross-Origin Resource Sharing (CORS)** para permitir que clientes externos consumam a API a partir de um IP específico.
- **Testes Automatizados**: O sistema inclui testes automatizados para garantir a criação correta de coleções, controle de permissões e validação de autenticação.

### Recursos

#### **Livros**

1. **Listar Livros**  
   - **URL**: `/api/livros/`  
   - **Método**: `GET`  
   - **Descrição**: Lista todos os livros disponíveis.  
   - **Permissões**: Acesso público (não requer autenticação).

2. **Detalhar Livro**  
   - **URL**: `/api/livros/{id}/`  
   - **Método**: `GET`  
   - **Descrição**: Recupera os detalhes de um livro específico.  
   - **Permissões**: Acesso público (não requer autenticação).

3. **Criar Livro**  
   - **URL**: `/api/livros/`  
   - **Método**: `POST`  
   - **Descrição**: Cria um novo livro.  
   - **Permissões**: Acesso público (não requer autenticação).

4. **Editar Livro**  
   - **URL**: `/api/livros/{id}/`  
   - **Método**: `PUT` ou `PATCH`  
   - **Descrição**: Atualiza os dados de um livro específico.  
   - **Permissões**: Acesso público (não requer autenticação).

5. **Excluir Livro**  
   - **URL**: `/api/livros/{id}/`  
   - **Método**: `DELETE`  
   - **Descrição**: Exclui um livro específico.  
   - **Permissões**: Acesso público (não requer autenticação).


#### **Categorias**

6. **Listar Categorias**  
   - **URL**: `/api/categorias/`  
   - **Método**: `GET`  
   - **Descrição**: Lista todas as categorias disponíveis.  
   - **Permissões**: Acesso público (não requer autenticação).

7. **Detalhar Categoria**  
   - **URL**: `/api/categorias/{id}/`  
   - **Método**: `GET`  
   - **Descrição**: Recupera os detalhes de uma categoria específica.  
   - **Permissões**: Acesso público (não requer autenticação).

8. **Criar Categoria**  
   - **URL**: `/api/categorias/`  
   - **Método**: `POST`  
   - **Descrição**: Cria uma nova categoria.  
   - **Permissões**: Acesso público (não requer autenticação).

9. **Editar Categoria**  
   - **URL**: `/api/categorias/{id}/`  
   - **Método**: `PUT` ou `PATCH`  
   - **Descrição**: Atualiza os dados de uma categoria específica.  
   - **Permissões**: Acesso público (não requer autenticação).

10. **Excluir Categoria**  
    - **URL**: `/api/categorias/{id}/`  
    - **Método**: `DELETE`  
    - **Descrição**: Exclui uma categoria específica.  
    - **Permissões**: Acesso público (não requer autenticação).


#### **Autores**

11. **Listar Autores**  
    - **URL**: `/api/autores/`  
    - **Método**: `GET`  
    - **Descrição**: Lista todos os autores disponíveis.  
    - **Permissões**: Acesso público (não requer autenticação).

12. **Detalhar Autor**  
    - **URL**: `/api/autores/{id}/`  
    - **Método**: `GET`  
    - **Descrição**: Recupera os detalhes de um autor específico.  
    - **Permissões**: Acesso público (não requer autenticação).

13. **Criar Autor**  
    - **URL**: `/api/autores/`  
    - **Método**: `POST`  
    - **Descrição**: Cria um novo autor.  
    - **Permissões**: Acesso público (não requer autenticação).

14. **Editar Autor**  
    - **URL**: `/api/autores/{id}/`  
    - **Método**: `PUT` ou `PATCH`  
    - **Descrição**: Atualiza os dados de um autor específico.  
    - **Permissões**: Acesso público (não requer autenticação).

15. **Excluir Autor**  
    - **URL**: `/api/autores/{id}/`  
    - **Método**: `DELETE`  
    - **Descrição**: Exclui um autor específico.  
    - **Permissões**: Acesso público (não requer autenticação).


#### **Coleções**

16. **Listar Coleções**  
    - **URL**: `/api/colecoes/`  
    - **Método**: `GET`  
    - **Descrição**: Lista todas as coleções associadas ao usuário autenticado.  
    - **Permissões**: Requer autenticação (usuário autenticado).

17. **Detalhar Coleção**  
    - **URL**: `/api/colecoes/{id}/`  
    - **Método**: `GET`  
    - **Descrição**: Recupera os detalhes de uma coleção específica.  
    - **Permissões**: Requer autenticação (somente coleções do usuário autenticado são visíveis).

18. **Criar Coleção**  
    - **URL**: `/api/colecoes/`  
    - **Método**: `POST`  
    - **Descrição**: Cria uma nova coleção associada ao usuário autenticado.  
    - **Permissões**: Requer autenticação (usuário autenticado).

19. **Editar Coleção**  
    - **URL**: `/api/colecoes/{id}/`  
    - **Método**: `PUT` ou `PATCH`  
    - **Descrição**: Atualiza os dados de uma coleção específica.  
    - **Permissões**: Requer autenticação e permissão de colecionador (somente o colecionador pode editar).

20. **Excluir Coleção**  
    - **URL**: `/api/colecoes/{id}/`  
    - **Método**: `DELETE`  
    - **Descrição**: Exclui uma coleção específica.  
    - **Permissões**: Requer autenticação e permissão de colecionador (somente o colecionador pode excluir).


#### **Autenticação**

21. **Obter Token**  
    - **URL**: `/api/token/`  
    - **Método**: `POST`  
    - **Descrição**: Obtém o token de acesso e refresh com base nas credenciais do usuário.  
    - **Permissões**: Acesso público (necessário fornecer credenciais válidas).

22. **Atualizar Token**  
    - **URL**: `/api/token/refresh/`  
    - **Método**: `POST`  
    - **Descrição**: Atualiza o token de acesso usando o token de refresh.  
    - **Permissões**: Acesso público (necessário fornecer um token de refresh válido).

## Tecnologias Utilizadas

- **Django**: Framework web para o back-end.
- **Django Rest Framework (DRF)**: Para construção da API RESTful.
- **drf-spectacular**: Para documentação automática da API.
- **django-cors-headers**: Para configuração de CORS.
- **JWT (JSON Web Tokens)**: Para autenticação de usuários.
- **coverage.py**: Para cobertura de testes automatizados.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.10+
- Django 5.1
- Django REST Framework
- SQLite3 (banco de dados padrão)

### Passos para Execução

1. Clone este repositório:
    ```bash
    git clone <url-do-repositorio>
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/macOS
    venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações:
    ```bash
    python manage.py migrate
    ```

5. Execute o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

6. Acesse a API em [http://localhost:8000](http://localhost:8000).

## Como Testar a API

O sistema inclui testes automatizados que podem ser executados com o seguinte comando:

```bash
python manage.py test
```

## Autentição

## Autenticação com JWT

### O que é JWT?
JSON Web Token (JWT) é uma forma compacta e segura de transmitir informações entre o cliente e o servidor. No contexto da autenticação, o JWT é utilizado para gerar tokens que representam a identidade do usuário após ele fornecer suas credenciais. Esses tokens podem ser enviados nas requisições subsequentes para validar a identidade do usuário e garantir que ele tenha permissão para acessar os recursos.

### Fluxo de Autenticação

1. **Obter o Token de Acesso (Login)**  
   O primeiro passo para um usuário acessar os endpoints protegidos da API é autenticar-se utilizando suas credenciais (nome de usuário e senha) e obter um token de acesso. Isso é feito através do endpoint `POST /api/token/`.

2. **Enviando o Token nas Requisições**  
   Após o login bem-sucedido, o servidor envia dois tokens:
   - **Access Token**: Esse é o token utilizado para acessar os endpoints protegidos da API. Ele tem uma vida útil mais curta.
   - **Refresh Token**: Usado para gerar um novo access token quando o token de acesso expirar. Ele possui uma vida útil mais longa.

   O token de acesso deve ser enviado nas requisições subsequentes utilizando o cabeçalho HTTP `Authorization`:

   ```http
   Authorization: Bearer <access_token>
   ```

3. **Atualizando o Token de Acesso**
Quando o access token expira, o usuário pode obter um novo access token enviando o **refresh token** para o endpoint POST `/api/token/refresh/`.

## Documentação

*Acesse a documentação automática gerada por drf-spectacular:*

- Swagger UI: http://localhost:8000/api/docs/swagger/
- Redoc: http://localhost:8000/api/docs/redoc/


## Permissões
- *Coleções:*
- Apenas usuários autenticados podem criar, editar e excluir coleções.
- Apenas o colecionador pode editar ou excluir sua coleção.

- *Livros, Categorias e Autores:*
- Acessíveis a qualquer usuário (anônimo ou autenticado).

## Filtros e Paginação
*Filtros:*
- Livros: titulo, autor, categoria.
- Coleções: nome, colecionador.
- Paginação:

*Configuração padrão:* LimitOffsetPagination (limite e deslocamento personalizáveis).