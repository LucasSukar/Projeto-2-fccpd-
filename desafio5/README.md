README – Desafio 5: Arquitetura com API Gateway e Microsserviços
Descrição

Este projeto implementa uma arquitetura simples baseada em microsserviços, utilizando Docker e Docker Compose. O sistema é composto por dois serviços independentes (Users e Orders) e um API Gateway responsável por centralizar o acesso do cliente. O objetivo é demonstrar integração entre serviços, comunicação interna via Docker e organização da arquitetura.

Arquitetura

A arquitetura possui três componentes principais:

Service Users – retorna uma lista de usuários.

Service Orders – retorna uma lista de pedidos.

API Gateway – ponto único de entrada. Recebe requisições e encaminha para o microsserviço correspondente.

O cliente acessa apenas o gateway. As chamadas aos serviços internos acontecem pela rede criada pelo Docker Compose.

Funcionamento

O gateway expõe os endpoints /users e /orders.

Ao acessar /users, o gateway consulta o serviço de usuários.

Ao acessar /orders, o gateway consulta o serviço de pedidos.

Os microsserviços retornam dados simples em JSON.

Todos os serviços rodam isolados em containers separados.

Como executar

Para iniciar todos os serviços:

./run.sh


Para parar e remover tudo:

./run.sh stop

Como verificar

Após iniciar o sistema, é possível acessar pelo navegador ou Postman:

Gateway: http://localhost:8000

Usuários: http://localhost:8000/users

Pedidos: http://localhost:8000/orders

Os microsserviços também podem ser acessados diretamente nas portas 5001 e 5002, caso seja necessário.

Conclusão

O projeto demonstra o uso de microsserviços integrados através de um API Gateway, com comunicação interna gerenciada pelo Docker Compose. A arquitetura é simples, modular e adequada para aprendizado dos conceitos principais de microsserviços e orquestração com Docker.