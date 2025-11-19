# Desafio 5: API Gateway Pattern

## Objetivo
Implementar o padrão de projeto API Gateway. Em vez do cliente saber o endereço de cada microsserviço (Users, Orders), ele conhece apenas um endereço (Gateway), que roteia a chamada para o lugar certo.

##  Descrição do Projeto
Três serviços distintos rodando simultaneamente:
1.  **Gateway**: porteiro. Recebe tudo na porta 8000.
2.  **Service Users**: API interna de usuários.
3.  **Service Orders**: API interna de pedidos.

## Estrutura de Arquivos Explicada

### 1. `docker-compose.yml`
* Levanta 3 serviços.
* **Gateway**: Exposto na porta **8000**.
* **Service_users**: Exposto na 5001, apenas para debug, mas a comunicação real é interna.
* **Service_orders**: Exposto na 5002, para debug.

### 2. Pasta `gateway/`
* **`app.py`**:
    * Configura as URLs constantes: `http://service_users:5000/users` e `http://service_orders:5000/orders`.
    * Rota `/users`: O Gateway recebe, chama o serviço de usuários e devolve a resposta exata dele.
    * Rota `/orders`: O Gateway recebe, chama o serviço de pedidos e devolve a resposta.
* **`Dockerfile`**: Instala `flask` e `requests` para poder atuar como proxy reverso simples.

### 3. Pastas `service_users/` e `service_orders/`
* Ambas contêm aplicações Flask simples que retornam dados estáticos JSON para serem consumidos pelo Gateway.
* **Users**: Retorna IDs e Nomes.
* **Orders**: Retorna IDs de pedidos e bens (carro, moto).

### 4. `run.sh`
* Um script que pode Aceitar argumentos:
    * `./run.sh` (sem nada): Inicia os containers (`up -d`).
    * `./run.sh stop`: Para e remove containers e volumes (`down -v`).

##  Funcionamento
Isso simula um ambiente de produção real onde IPs e portas de serviços internos mudam ou são protegidos. O cliente só precisa decorar `localhost:8000`. O Gateway cuida de descobrir onde estão os dados dentro da rede Docker.

##  Como Executar
Iniciar o sistema:
```bash
./run.sh
