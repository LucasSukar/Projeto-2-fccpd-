Este projeto contém dois containers Docker que se comunicam por meio de uma rede Docker customizada. Um container representa um servidor web simples e o outro executa um cliente que envia requisições periódicas ao servidor.


docker-compose.yml
Este arquivo é o responsável por comandar os dois containers, criar a rede de comunicação entre eles, construir suas imagens e definir como cada serviço deve funcionar.

Principais elementos do arquivo:
services: Define os dois serviços (containers)
web: o servidor web.
client: o cliente que envia requisições.
build: Indica em qual pasta está o Dockerfile de cada serviço.
Ex: build: ./web  e  build: ./client
networks: Coloca os dois containers na mesma rede para que possam se comunicar via DNS do Docker.
Ex: rede: desafio 1
depends_on: Garante que o cliente só inicie após o container web estar rodando.

Pasta web/
Esta pasta contém todo o código referente ao servidor web.

Arquivo: web/app.py
Este é o código da aplicação web escrita em Python usando o framework Flask.
Quando recebe uma requisição HTTP, ele retorna uma mensagem com:
uma confirmação de que o servidor está ativo,
o hostname do container,e o horário atual.
A rota principal (/) devolve um JSON contendo esses dados.

Arquivo: web/requirements.txt

Lista as dependências necessárias para o servidor web funcionar.
O Flask é instalado dentro do container usando este arquivo.

Arquivo: web/Dockerfile
Este arquivo descreve como construir a imagem do container web.
Elementos importantes:
FROM python:3.10-alpine: Indica a imagem base com Python.
WORKDIR /app: Define que todos os comandos serão executados dentro da pasta /app do container.
COPY requirements.txt .: Copia a lista de dependências para dentro do container.
RUN pip install -r requirements.txt: Instala as dependências necessárias (Flask).
COPY app.py .: Copia o código do servidor para dentro do container.
CMD ["python", "app.py"]: Comando que inicia o servidor web quando o container é executado.

Pasta client/
Esta pasta contém o script cliente e o Dockerfile responsável por montar o container que executa o script.

Arquivo: client/client.sh
Este é o script responsável por fazer requisições ao servidor web a cada intervalo de tempo.
Funções principais do script:
Define o endereço do servidor web:
porta="http://web:8080/
Define o intervalo em segundos entre as requisições:
intervalo=5
Um loop infinito que:
obtém a hora atual,
envia uma requisição HTTP usando curl,
verifica se houve sucesso ou erro,
imprime a resposta no terminal,
aguarda alguns segundos antes da próxima tentativa.
É o responsável pela comunicação e geração de logs.
Importante: o script começa com #!/bin/sh para permitir sua execução dentro do Linux.

Arquivo: client/Dockerfile
Este arquivo monta a imagem do container cliente.

Elementos principais:
FROM alpine:3.19:Define uma imagem mínima do Linux.
RUN apk add --no-cache curl: Instala o programa curl, necessário para enviar requisições.
WORKDIR /app: Define a pasta onde o script será executado.
COPY client.sh .: Copia o script cliente para dentro do container.
RUN chmod +x client.sh: Garante que o script tem permissão de execução.
CMD ["./client.sh"]: Define que o script será executado automaticamente quando o container iniciar.