DESAFIO 1
#Objetivo
Criar dois containers Docker que se comunicam entre si utilizando uma rede Docker personalizada.
O primeiro container atua como servidor web e o segundo executa requisições periódicas ao servidor, exibindo os resultados no terminal.
---
#Descrição Geral
Este projeto contém uma arquitetura simples composta por dois containers:

##1. Servidor Web (pasta web/)
   -Implementado em Python com Flask.
   -Expõe uma rota HTTP que retorna informações do container, como hostname e horário atual.
   -Executado na porta 8080 dentro do container.

2. Cliente de Requisições (pasta client/)

Um container leve baseado em Alpine Linux.

Executa um script shell que faz requisições contínuas para o servidor web.

Exibe logs a cada requisição, permitindo verificar a comunicação.

Ambos os containers são conectados a uma rede Docker customizada criada pelo Docker Compose.

Estrutura do Projeto
docker-compose.yml

Este arquivo é o responsável por orquestrar os containers.
Funções principais:

cria a rede Docker personalizada;

define os serviços web e client;

garante que o cliente só inicia após o servidor estar de pé (via depends_on);

coloca ambos na mesma rede, permitindo comunicação pelo nome do serviço.

Pontos importantes:

O servidor pode ser acessado internamente via http://web:8080.

O cliente usa esse DNS interno automaticamente, sem necessidade de IP.

Pasta web/ – Servidor Web
app.py

Aplicação Flask que responde com:

confirmação de que o servidor está funcionando;

hostname do container;

horário atual formatado;

mensagem de status.

A rota principal / envia uma resposta em JSON.

requirements.txt

Lista contendo as dependências necessárias:

Flask

Dockerfile

Descreve como o container do servidor é montado:

usa Python 3.10 como base;

copia dependências;

instala os pacotes da aplicação;

copia o código do servidor;

define o comando de inicialização: python app.py.

Pasta client/ – Cliente Automatizado
client.sh

Script principal do container cliente:

define o endereço do servidor (http://web:8080/);

define um intervalo entre requisições;

cria um loop infinito que:

obtém a hora atual;

faz a requisição HTTP usando curl;

imprime o resultado no terminal;

espera alguns segundos e tenta novamente.

Dockerfile

Container do cliente:

usa Alpine Linux;

instala o pacote curl;

copia e habilita o script client.sh;

executa o script automaticamente.

▶Como Executar

Dê permissão ao script:

chmod +x run.sh

Inicie os containers:

./run.sh

O script sobe os serviços e exibe os logs.

Como Verificar

Observe no terminal as requisições feitas pelo cliente.

As respostas devem conter hostname e horário do servidor.

Os logs comprovam a comunicação contínua entre containers.

Ambos estão conectados na mesma rede Docker personalizada.

DESAFIO 2 — Volumes e Persistência
Objetivo

Demonstrar como a persistência de dados funciona utilizando volumes Docker em um banco PostgreSQL.

Descrição Geral

Este projeto monta um banco PostgreSQL dentro de um container, mas seus dados são gravados em um volume externo.
Assim, ao remover o container, os dados continuam existindo.

O projeto também inclui:

um arquivo init.sql que cria tabela e insere dados iniciais;

um script que sobe o container duas vezes para demonstrar a persistência.

Estrutura do Projeto
docker-compose.yml

Responsável por:

criar o container PostgreSQL;

configurar usuário, senha e nome do banco;

montar um volume onde os dados serão salvos;

montar o arquivo init.sql no local correto para execução automática;

expor a porta para acesso externo.

Pontos importantes:

O volume garante a persistência real dos dados.

O arquivo init.sql só roda quando o volume está vazio.

Arquivo init.sql

Script SQL que:

cria a tabela usuarios;

insere registros iniciais (exemplo: nomes definidos por você).

Este arquivo é executado automaticamente na primeira vez em que o banco é criado.

Script run.sh

Automatiza todo o processo:

Sobe o container;

Aguarda o banco inicializar;

Exibe os dados da tabela;

Derruba o container (volume permanece);

Sobe novamente o container;

Mostra novamente os dados, comprovando persistência.

▶Como Executar

Permitir execução:

chmod +x run.sh

Executar:

./run.sh

Como Verificar

Na primeira execução, o script mostra os dados vindos do init.sql.

Na segunda, os mesmos dados aparecem, provando que o volume mantém as informações mesmo após remover o container.

O volume só é apagado manualmente com docker-compose down -v.

DESAFIO 3 — Docker Compose Orquestrando Serviços
Objetivo

Criar uma aplicação com três serviços (web, banco e cache), orquestrados via Docker Compose, demonstrando comunicação interna e dependências.

Descrição Geral

O projeto utiliza três containers que trabalham juntos:

1. Web (Flask)

Exibe página inicial;

Possui rota para testar PostgreSQL;

Possui rota para testar Redis.

2. Banco (PostgreSQL)

Armazena dados;

Usa volume para persistência real.

3. Cache (Redis)

Fornece armazenamento rápido;

Usado para teste de comunicação e leitura/escrita.

Todos estão conectados à mesma rede interna chamada internal.

Componentes do Projeto
docker-compose.yml

Coordena os três serviços:

define ambiente do PostgreSQL;

cria volume para dados;

cria rede interna;

define depends_on para ordem de inicialização;

garante que os serviços se comunicam pelos nomes:

db para banco;

cache para Redis;

web para aplicação.

Pasta web/

Contém a aplicação Flask que:

responde na porta 5000;

possui rotas:

/ → página inicial;

/db → testa conexão com PostgreSQL;

/cache → testa conexão com Redis.

Script run.sh

Facilita a execução:

derruba containers antigos;

sobe todos os serviços novamente;

mostra os logs iniciais;

deixa tudo pronto para testes no navegador.

▶Como Executar

Permitir permissão:

chmod +x run.sh

Rodar:

./run.sh

Como Verificar

Acesse:

Página inicial
http://localhost:5000

Teste do banco
http://localhost:5000/db

Teste do Redis
http://localhost:5000/cache

Cada rota retorna mensagens confirmando a comunicação interna entre os serviços.

no inicio eu tentei formatar corretamente mas deu muito trabalho, me mandfe o aquivo compoleto sem mudar nada mas totalmente formatado
