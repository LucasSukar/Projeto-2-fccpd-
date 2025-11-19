# Desafio 3: Orquestração Completa (Web, DB, Cache)

## Objetivo
Praticar a configuração de um ambiente Full Stack usando Docker Compose, gerenciando dependências de inicialização e conectividade entre três tecnologias diferentes: Python, Postgres e Redis.

##  Descrição do Projeto
Uma aplicação web central que se conecta a dois serviços auxiliares:
1.  **Banco de Dados**: Para persistência relacional.
2.  **Cache**: Para armazenamento rápido em memória (chave-valor).

##  Estrutura dos Arquivos 

### 1. `docker-compose.yml`
Configura a topologia da rede:
* **Services**:
    * `web`: A aplicação principal. Tem `depends_on: db, cache` para evitar erros de conexão na partida.
    * `db`: PostgreSQL na versao 15 com volume persistente.
    * `cache`: Redis.
* **Networks**: Define a rede `internal` para isolar a comunicação desses serviços do mundo externo.

### 2. Pasta `web/`
* **`app.py`**:
    * Rota `/db`: Usa a biblioteca `psycopg2` para conectar no host `db` (definido no compose) e autenticar com as credenciais do banco.
    * Rota `/cache`: Usa a biblioteca `redis` para conectar no host `cache`, porta 6379. Grava uma chave de teste (`set("teste", "ok")`) para validar a escrita.
* **`Dockerfile`**:
    * Instala dependências de sistema e bibliotecas Python (`flask`, `psycopg2-binary`, `redis`) necessárias para conectar nos outros serviços.

### 3. `run.sh`
* Automação para reiniciar o ambiente do zero. Executa `down` para limpar e `up -d --build` para garantir que alterações no código Python sejam refletidas na nova imagem.

##  Funcionamento
Ao acessar a aplicação web, ela atua como um "proxy" de verificação. 
Se você acessar `/db`, o Python vai até o container Postgres e volta. 
Se acessar `/cache`, ele vai até o Redis e volta. 
tudo Isso comprova que a rede interna do Docker está roteando o tráfego corretamente entre os containers.

##  Como Rodar
1.  Inicie o ambiente:
    ```bash
    ./run.sh
    ```
2.  Teste no navegador:
    * App: `http://localhost:5000/`
    * Conexão DB: `http://localhost:5000/db`
    * Conexão Redis: `http://localhost:5000/cache`
