DESAFIO 1 — Containers em Rede
Objetivo

Criar dois containers Docker que se comunicam entre si utilizando uma rede Docker personalizada.
Um container atua como servidor web, enquanto o outro realiza requisições periódicas ao servidor.

Descrição Geral

A arquitetura é composta por dois containers:

1. Servidor Web (pasta web/)

Desenvolvido com Python + Flask.

Possui uma rota HTTP que retorna:

hostname do container,

horário atual,

mensagem de status.

Executado na porta 8080.

2. Cliente de Requisições (pasta client/)

Baseado em Alpine Linux.

Executa um script que realiza requisições contínuas ao servidor.

Mostra no terminal o resultado de cada requisição.

Ambos utilizam uma rede Docker customizada, criada automaticamente pelo Docker Compose.

Estrutura do Projeto
docker-compose.yml

Define:

a rede Docker personalizada,

o container web e o cliente,

dependência do cliente em relação ao servidor (depends_on),

comunicação interna via DNS Docker (http://web:8080).

Pasta web/ – Servidor Web

app.py

Rota principal retorna um JSON com:

confirmação de funcionamento,

hostname,

horário atual,

status.

requirements.txt

Lista de dependências (Flask).

Dockerfile

Base Python 3.10.

Instala dependências.

Copia a aplicação.

Executa python app.py.

Pasta client/ – Cliente Automatizado

client.sh

Script que:

acessa http://web:8080/,

imprime horário local,

faz requisições usando curl,

repete continuamente.

Dockerfile

Base Alpine Linux.

Instala curl.

Copia e habilita o script.

Executa automaticamente o cliente.

Como Executar
chmod +x run.sh
./run.sh

Como Verificar

Observe no terminal as requisições e respostas contendo hostname e horário do servidor.

A comunicação contínua confirma o funcionamento da rede interna.

DESAFIO 2 — Volumes e Persistência
Objetivo

Demonstrar persistência de dados usando volumes Docker com um banco PostgreSQL.
Mesmo removendo o container, os dados permanecem armazenados.

Descrição Geral

O projeto inclui:

Banco PostgreSQL com volume persistente,

Arquivo init.sql para criar tabela e inserir dados iniciais,

Script que sobe o container duas vezes para demonstrar que os dados persistem.

Estrutura do Projeto
docker-compose.yml

Responsável por:

Criar o container PostgreSQL,

Definir usuário, senha e nome do banco,

Montar volume persistente,

Montar init.sql para execução automática,

Expor porta de acesso.

Pontos importantes:

O volume mantém os dados entre execuções.

init.sql roda apenas na primeira inicialização.

Arquivo init.sql

Cria tabela usuarios,

Insere registros iniciais.

Executado somente quando o banco é criado pela primeira vez.

Script run.sh

Automatiza todo o teste de persistência:

Sobe o container,

Aguarda inicialização,

Exibe dados,

Derruba container,

Sobe novamente,

Exibe novamente (confirmando persistência).

Como Executar
chmod +x run.sh
./run.sh

Como Verificar

Na primeira execução: dados vêm do init.sql.

Nas seguintes: mesmos dados são carregados do volume.

Volume só é apagado com:

docker-compose down -v

DESAFIO 3 — Docker Compose Orquestrando Serviços
Objetivo

Criar uma aplicação com três serviços integrados:

Web (Flask)

Banco (PostgreSQL)

Cache (Redis)

Todos orquestrados via Docker Compose, com comunicação interna e dependências configuradas.

Descrição Geral

A aplicação é composta por:

1. Web (Flask)

Página inicial,

Rota para testar PostgreSQL,

Rota para testar Redis.

2. Banco (PostgreSQL)

Armazena dados com persistência via volume.

3. Cache (Redis)

Fornece armazenamento rápido para testes.

Todos conectados à rede interna chamada internal.

Componentes do Projeto
docker-compose.yml

Define:

Variáveis de ambiente do PostgreSQL,

Volume persistente,

Rede interna,

Dependências (depends_on),

Comunicação interna via nomes dos containers:

web

db

cache

Pasta web/

Aplicação Flask com rotas:

/ página inicial,

/db teste de conexão com PostgreSQL,

/cache teste de conexão com Redis.

Script run.sh

Remove containers antigos,

Sobe todos os serviços,

Exibe logs iniciais,

Deixa tudo pronto para testes.

Como Executar
chmod +x run.sh
./run.sh

Como Verificar

Acesse no navegador:

Página inicial
http://localhost:5000

Teste do banco
http://localhost:5000/db

Teste do Redis
http://localhost:5000/cache

As rotas retornam mensagens confirmando a comunicação entre os serviços.
