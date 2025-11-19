# Desafio 4: Comunicação entre Microsserviços (Service-to-Service)

##  Objetivo
Simular uma arquitetura de microsserviços onde um serviço consome dados de outro serviço via HTTP, demonstrando desacoplamento e comunicação síncrona.

##  Descrição do Projeto
* **Service A**: ele que possui os dados e Retorna apenas JSON cru.
* **Service B**: processa os dados. Pede dados ao A, formata uma frase amigável para o usuário e retorna.

##  Estrutura de Arquivos 

### 1. `docker-compose.yml`
* Mapeia portas diferentes para evitar conflito no host local:
    * `service_a`: Porta externa 5000.
    * `service_b`: Porta externa 5001.
* Define que `service_b` depende de `service_a`.

### 2. Pasta `service_a/` (Provider)
* **`app.py`**: Endpoint `/users` retorna uma lista estática de dicionários: `[{"id": 1, "nome": "Lucas sukar"}...]`.
* **`Dockerfile`**: Imagem Python simples expondo a porta 5000.

### 3. Pasta `service_b/` (Consumer)
* **`app.py`**:
    * Define a URL do serviço A como `http://service_a:5000/users`. usa o nome do container definido no Compose.
    * A rota `/info` faz um `requests.get(SERVICE_A_URL)`.
    * Itera sobre o JSON recebido e cria uma string personalizada: "Usuário [Nome] ativos na faculdade...".
* **`Dockerfile`**: Instala `flask` e `requests` (necessário para chamar o outro serviço).

##  Funcionamento
O fluxo de requisição é:
`Cliente (Browser)` -> `Service B (Info)` -> `Service A (Users)` -> `Service B (Formata)` -> `Cliente`.

##  Como Executar
```bash
./roda.sh
