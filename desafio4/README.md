Objetivo

Desenvolver dois microsserviços totalmente independentes que se comunicam via HTTP, cada um com seu próprio Dockerfile e executados através de um docker-compose. O objetivo é demonstrar compreensão de isolamento, comunicação entre serviços e arquitetura básica de microsserviços.

Arquitetura Geral

A arquitetura é composta por dois serviços:

Microsserviço A (Service A)
Responsável por disponibilizar uma lista de usuários através de uma API simples.
Endpoint principal:

GET /users

Microsserviço B (Service B)
Consome o endpoint do Service A, processa ou combina as informações recebidas e retorna um texto mais descritivo.
Endpoint principal:

GET /info

A comunicação entre eles ocorre internamente via rede criada pelo docker-compose.
O Service B acessa o Service A utilizando o nome do container:
http://service_a:5000/users

Descrição dos Componentes
1. Service A

É uma pequena aplicação que retorna uma lista fixa de usuários em formato JSON.
Serve como provedor de dados.
Sua responsabilidade é apenas entregar os dados solicitados, sem lógica adicional.

2. Service B

É uma aplicação que faz uma requisição HTTP ao Service A, recebe os dados e retorna um texto combinando as informações.
Demonstra o consumo de APIs internas entre microsserviços.

3. Dockerfiles

Cada microsserviço possui seu próprio Dockerfile, o que garante isolamento e independência.
Eles definem:

imagem base utilizada

diretório de trabalho

dependências necessárias

comando de execução da aplicação

Esse isolamento permite que cada serviço evolua sem afetar o outro.

4. docker-compose.yml

Arquivo responsável por:

construir as imagens dos dois serviços

mapear as portas externas (5001 e 6001)

criar a rede interna onde os serviços se comunicam

garantir que o Service B só inicie depois do Service A

É o ponto central que coordena a execução de toda a arquitetura.

5. Script roda.sh

Um script simples para facilitar o uso:

./roda.sh inicia os dois microsserviços

./roda.sh stop derruba todos os containers e remove os volumes

Ele apenas automatiza os comandos do docker-compose.

Funcionamento da Comunicação

O fluxo ocorre da seguinte forma:

O usuário acessa http://localhost:6001/info

O Service B recebe a requisição

O Service B envia internamente uma requisição para o Service A:
http://service_a:5000/users

O Service A responde com sua lista de usuários em JSON

O Service B processa esses dados e devolve a resposta final ao navegador

Isso demonstra comunicação entre serviços totalmente independentes, utilizando apenas HTTP.