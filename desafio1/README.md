# Desafio 1: Comunicação entre Containers (Cliente-Servidor)

##Objetivo
Demonstrar a comunicação básica de rede entre dois containers Docker. O objetivo é provar que containers na mesma rede personalizada podem se comunicar usando nomes de serviço (DNS interno) em vez de endereços IP.

## 📄 Descrição do Projeto
O sistema simula uma arquitetura simples de monitoramento:
1.  **Servidor (Web)**: Uma API que fornece dados sobre seu próprio estado.
2.  **Cliente**: Um "bot" que consulta essa API repetidamente para verificar se ela está online.

##Estrutura de Arquivos Explicada

### 1. `docker-compose.yml`
Este é o orquestrador do desafio.
* **Services**: Define dois serviços, `web` e `client`.
* **Build**: Indica que as imagens devem ser construídas localmente a partir das pastas `./web` e `./client`.
* **Networks**: Cria uma rede chamada `challenge_net`. Ambos os serviços são conectados a ela, permitindo visibilidade mútua.
* **Depends_on**: Garante que o container `client` só inicie após o container `web` estar rodando.

### 2. Pasta `web/` (O Servidor)
* **`app.py`**: O código da aplicação principal.
    * Usa o framework **Flask**.
    * Define uma rota `/` que retorna um JSON com: mensagem de boas-vindas, o `hostname` (ID do container) e a hora atual.
    * Configurado para rodar na porta **8080**.
* **`Dockerfile`**: A receita para criar a imagem do servidor.
    * Base: `python:3.11-slim` (leve).
    * Instala as dependências listadas em `requirements.txt`.
    * Copia o código e define o comando de entrada `python app.py`.
* **`requirements.txt`**: Lista as bibliotecas Python necessárias, especificamente `Flask==2.3.2`.

### 3. Pasta `client/` (O Cliente)
* **`client.sh`**: O script de automação.
    * Define o alvo como `http://web:8080/` (note o uso do nome do serviço `web` em vez de IP).
    * Entra em um loop `while true` que executa o comando `curl` a cada 5 segundos.
    * Imprime no terminal se a conexão foi "sucesso" ou "erro".
* **`Dockerfile`**: A receita para a imagem do cliente.
    * Base: `alpine:3.19` (extremamente leve).
    * Instala o pacote `curl` via `apk`.
    * Copia o script `client.sh`, dá permissão de execução (`chmod +x`) e o define como comando inicial.

##Funcionamento
Quando você sobe o projeto, o Docker cria a rede interna. O servidor sobe e fica ouvindo na porta 8080. O cliente sobe em seguida, resolvendo o DNS `web` para o IP interno do servidor e começa a enviar requisições HTTP, gerando logs no terminal.

##Como Executar
1.  Dê permissão ao script de execução:
    ```bash
    chmod +x run.sh
    ```
2.  Inicie o projeto (isso irá parar containers antigos e subir os novos com logs):
    ```bash
    ./run.sh
    ```
