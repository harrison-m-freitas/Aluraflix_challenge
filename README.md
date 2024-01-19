# Desafio Alura - Backend

Este é um projeto Django que implementa uma API REST para gerenciamento de vídeos e categorias, seguindo as diretrizes do desafio proposto pela Alura.

## Funcionalidades Implementadas

- Rotas RESTful para manipulação de categorias e vídeos.
- Autenticação JWT para acesso às rotas CRUD.
- Rota `/videos/free/` para acesso público a vídeos.

## Estrutura do Projeto

- `categories/`: Implementação da funcionalidade de categorias.
- `videos/`: Implementação da funcionalidade de vídeos.
- `api/token/`: Rota para obtenção do token de acesso.
- `api/token/refresh/`: Rota para atualização do token de acesso.

## Instalação

1. Clone o repositório: `git clone <URL_DO_REPOSITORIO>`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações: `python manage.py migrate`
4. Execute o servidor: `python manage.py runserver`

## Uso

- Acesse a documentação da API em `http://localhost:8000/docs/` para obter detalhes sobre as rotas disponíveis e como utilizá-las.

## Contribuições

Contribuições são bem-vindas. Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).