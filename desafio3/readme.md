Este projeto foi feito para praticar o uso do Docker Compose, criando uma aplicação com três serviços que se comunicam entre si:

web → aplicação Flask

db → banco PostgreSQL

cache → Redis para cache

A ideia é mostrar como orquestrar múltiplos containers usando uma rede interna e o depends_on.

Descrição dos serviços
1. Web (Flask)

Roda um servidor Flask simples.

Tem rotas para testar comunicação com o banco e o Redis.

Porta exposta para acessar pelo navegador: 5000.

2. Banco (PostgreSQL)

Usa a imagem oficial do Postgres.

Salva os dados em um volume para não perder nada quando o container for destruído.

3. Cache (Redis)

Usa Redis Alpine (imagem mais leve).

Serve para testar comunicação com cache.

Comunicação entre os serviços

Todos os serviços estão na mesma rede interna chamada internal, então conseguem se comunicar pelos nomes:

db → PostgreSQL

cache → Redis

web → Flask

Exemplo dentro do Flask:

host="db"

Como rodar o projeto

Antes de tudo, dê permissão ao script:

chmod +x run.sh


Agora execute:

./run.sh


O script faz três coisas:

Derruba qualquer container antigo

Sobe os serviços com build

Mostra os logs

Testando no navegador

Com tudo rodando, abra:

✔ Serviço web

http://localhost:5000/

✔ Teste do banco

http://localhost:5000/db

✔ Teste do Redis

http://localhost:5000/cache