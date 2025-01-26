# README - Lambda para Gerenciamento de Autenticação com AWS Cognito

## Introdução

Este projeto implementa uma função AWS Lambda para gerenciar operações de autenticação e registro de usuários utilizando o Amazon Cognito. A aplicação oferece endpoints REST para login, registro e manipulação de sessões autenticadas.

O objetivo é demonstrar o uso de serviços AWS, como **Amazon Cognito**, **AWS Lambda** e **Amazon API Gateway**, para construir soluções seguras e escaláveis de gerenciamento de identidade.

---

## Funcionalidades

1. **Login de usuários**:
   - Autenticação via credenciais de usuário (username e senha).
   - Retorna um token JWT para sessão autenticada.

2. **Registro de novos usuários**:
   - Cria contas de usuário no Amazon Cognito.
   - Adiciona atributos personalizados, como nome e e-mail.

3. **Páginas HTML dinâmicas**:
   - Renderiza interfaces de login, registro e retorno com informações personalizadas.

4. **Confirmação de registro automática**:
   - Confirma registros diretamente no pool de usuários.

---

## Pré-requisitos

1. **Configuração do Amazon Cognito**:
   - Um User Pool configurado com o ID correspondente (é necessário ajustar `USER_POOL_ID` no código).
   - Um App Client com credenciais ajustadas (`CLIENT_ID`).

2. **Arquivos HTML**:
   - Arquivos `login.html`, `register.html` e `logged.html` no mesmo diretório que o código Lambda.
   - Uma imagem `background_videoframe.jpeg` para renderização dinâmica.

3. **Permissões IAM**:
   - A função Lambda deve possuir permissões para:
     - Chamar as operações do Amazon Cognito.
     - Ler os arquivos estáticos hospedados no diretório local.

4. **Configuração do API Gateway**:
   - Configurar mapeamento de rotas para os endpoints:
     - `/cadastro/login` (GET)
     - `/cadastro/logged` (POST)
     - `/cadastro/register` (GET e POST)

---

## Estrutura do Código

### Principais Componentes

1. **`load_html(name)`**  
   Carrega o conteúdo de arquivos HTML e insere dinamicamente uma imagem de fundo codificada em base64.

2. **`handle_login(event)`**  
   Renderiza a página de login ao receber uma requisição GET.

3. **`handle_logged(event)`**  
   Processa autenticação do usuário e renderiza a página de confirmação com o token JWT.

4. **`handle_register(event)`**  
   Renderiza a página de registro ao receber uma requisição GET.

5. **`handle_registration(event)`**  
   Cria um novo usuário no Cognito, confirmando o registro automaticamente.

6. **`lambda_handler(event, context)`**  
   Roteia as requisições recebidas para os manipuladores adequados com base no método HTTP e no caminho do endpoint.

---

## Configuração e Deploy

### 1. **Configuração do AWS Lambda**
- Crie uma nova função Lambda no console AWS.
- Suba o código como arquivo `.zip` ou utilizando um IDE compatível.
- Configure as variáveis de ambiente:
  ```plaintext
  USER_POOL_ID=<ID do User Pool>
  CLIENT_ID=<ID do App Client>
  ```
- Vincule uma função IAM com permissões apropriadas.

### 2. **Configuração do API Gateway**
- Configure rotas para os seguintes endpoints:
  - `/cadastro/login` (GET)
  - `/cadastro/logged` (POST)
  - `/cadastro/register` (GET e POST)
- Integre cada rota à função Lambda.

### 3. **Configuração do Cognito**
- Crie ou ajuste um User Pool com:
  - Configuração de atributos obrigatórios (e-mail, nome).
  - Um App Client para autenticação sem fluxo de secret.

---

## Fluxo de Funcionamento

1. **Login de Usuário**:
   - O usuário acessa `/cadastro/login`.
   - Insere credenciais que são enviadas para autenticação.
   - O token JWT é retornado na página de sucesso.

2. **Registro de Usuário**:
   - O usuário acessa `/cadastro/register`.
   - Insere informações como nome, e-mail, usuário e senha.
   - O registro é confirmado automaticamente e uma resposta é retornada.

---

## Exemplo de Respostas

### Sucesso no Registro:
```json
{
  "statusCode": 201,
  "headers": {
    "Content-type": "application/json"
  },
  "body": "{\"cadastro\": true}"
}
```

### Erro de Usuário Existente:
```json
{
  "statusCode": 500,
  "headers": {
    "Content-type": "application/json"
  },
  "body": "{\"cadastro\": true, \"error\": \"Usuário já existe\"}"
}
```

### Sucesso no Login:
```json
{
  "statusCode": 200,
  "headers": {
    "Content-type": "text/html"
  },
  "body": "<HTML renderizado com token e nome do usuário>"
}
```

---

## Diagrama da Arquitetura

```plaintext
[ Usuário ] -> [ API Gateway ] -> [ Lambda Function ]
                                   ↸          ↶
                            [ Cognito ]      [ Arquivos Estáticos ]
```

---

## Pontos de Aprendizado

- Integração segura com o Amazon Cognito para autenticação.
- Geração dinâmica de páginas HTML no contexto serverless.
- Uso do AWS API Gateway para criação de APIs REST.

---

**Apresentação prática:** Durante a demonstração, serão apresentados os fluxos de login e registro, incluindo o retorno de tokens JWT e a renderização de páginas dinâmicas com informações personalizadas.

