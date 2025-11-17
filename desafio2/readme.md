README — Desafio Docker: Persistência com PostgreSQL

Este README explica, em detalhes, cada arquivo e passo do seu projeto que demonstra a persistência de dados usando Docker Compose e um volume Docker para PostgreSQL.

Estrutura do projeto (arquivos relevantes)

docker-compose.yml

init.sql

run.sh (ou script de shell que você usou — trechos com echo, docker-compose up, docker exec, docker-compose down, etc.)

Observação: nomes de arquivos podem variar. Aqui eu descrevo os conteúdos e a função de cada um com base no que você enviou.

1) docker-compose.yml — explicação detalhada

Este arquivo descreve os serviços que o Docker Compose deve orquestrar. No seu caso há um serviço postgres e um volume pgdata:

services:
  postgres:
    image: postgres:15
    container_name: desafio2
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: 123
      POSTGRES_DB: teste_desafio2
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5433:5432"


volumes:
  pgdata:
Campos e comportamento

image: postgres:15

Usa a imagem oficial do PostgreSQL versão 15.

container_name: desafio2

Define um nome amigável para o contêiner (facilita comandos docker exec, docker logs etc.).

environment:

POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB — variáveis utilizadas pela imagem oficial para criar um banco inicial e um usuário. Aqui: usuário admin, senha 123, banco teste_desafio2.

volumes:

pgdata:/var/lib/postgresql/data — volume nomeado que persiste os dados do PostgreSQL no host (ou no driver de volumes do Docker). Isso garante que, mesmo removendo o contêiner, os dados do banco persistam.

./init.sql:/docker-entrypoint-initdb.d/init.sql — bind mount que injeta um arquivo de inicialização dentro do contêiner. A imagem oficial executa scripts localizados em /docker-entrypoint-initdb.d/ apenas na primeira inicialização do volume (ou seja, somente quando o diretório de dados está vazio).

ports: - "5433:5432":

Mapeia a porta 5432 do PostgreSQL (dentro do contêiner) para a porta 5433 do host. Isso permite conectar localmente ao banco usando localhost:5433 sem conflitar com outras instâncias que usam 5432.

volumes: na raiz (definição pgdata:):

Declara o volume nomeado pgdata. Pode-se também especificar opções se necessário (driver, local path, etc.).

Observações importantes sobre persistência e init.sql

O bind ./init.sql:/docker-entrypoint-initdb.d/init.sql funciona apenas quando o diretório de dados do PostgreSQL dentro do contêiner estiver vazio. Se o volume pgdata já tiver sido criado em execuções anteriores, o script não será executado novamente.

Para forçar reexecução do init.sql você precisa remover o volume pgdata (por exemplo, docker-compose down -v ou docker volume rm <nome>), mas cuidado: isso apaga os dados.

2) init.sql — explicação detalhada

Conteúdo (conforme enviado):

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50)
);


INSERT INTO usuarios (nome) VALUES
    ('Lucas Sukar'),
    ('Caio Lima'),
    ('Rodrigo');
O que faz

Cria a tabela usuarios caso ela não exista.

Insere três registros iniciais.

Como e quando é executado

A imagem oficial do PostgreSQL executa automaticamente scripts .sql ou .sh presentes em /docker-entrypoint-initdb.d/ somente quando o banco é inicializado pela primeira vez (ou seja, quando a pasta de dados estiver vazia). Portanto, na primeira execução do docker-compose up com pgdata vazio, esse script será aplicado.

3) Script de execução (ex.: run.sh) — explicação detalhada

Você incluiu um script com os passos:

echo "Subindo container"
docker-compose up -d


echo "Aguardando PostgreSQL iniciar..."
sleep 3


echo "Dados iniciais:"
docker exec -it desafio2 psql -U admin -d teste_desafio2 -c "SELECT * FROM usuarios;"


echo ""
echo "Removendo container (volume permanece)"
docker-compose down


echo ""
echo "Subindo novamente para testar persistência"
docker-compose up -d
sleep 3


echo "Dados após recriação (persistência):"
docker exec -it desafio2 psql -U admin -d teste_desafio2 -c "SELECT * FROM usuarios;"
Explicação linha a linha

docker-compose up -d

Sobe os serviços (em segundo plano). Na primeira vez, a imagem é baixada, o contêiner criado e o init.sql executado (se o volume estiver vazio).

sleep 3

Pausa por 3 segundos para dar tempo do PostgreSQL iniciar. (Dependendo do hardware e da carga, pode ser necessário aumentar esse tempo — 3s é curto; em máquinas lentas 10–15s pode ser mais seguro.)

docker exec -it desafio2 psql -U admin -d teste_desafio2 -c "SELECT * FROM usuarios;"

Executa o cliente psql dentro do contêiner desafio2 para listar os registros da tabela usuarios.

docker-compose down

Para e remove os contêineres e a rede criada, porém mantém volumes nomeados por padrão. Como pgdata é um volume nomeado definido em docker-compose.yml, seus arquivos persistem.

Ao executar docker-compose up -d novamente, o contêiner será recriado, mas o volume pgdata será reaproveitado — portanto os dados inseridos anteriormente permanecem.

Observação sobre docker-compose down -v

Se usar docker-compose down -v, o Docker também removerá os volumes declarados — nesse caso a persistência será perdida e o init.sql será reexecutado na próxima vez.

Fluxo esperado (comportamento demonstrado)

Executar docker-compose up -d pela primeira vez:

O Docker baixa a imagem postgres:15 (se não estiver no host).

Cria o volume pgdata e monta em /var/lib/postgresql/data.

Copia e executa init.sql dentro de /docker-entrypoint-initdb.d/ — cria tabela e insere dados.

Rodar docker exec ... psql -c "SELECT * FROM usuarios;" mostra os 3 registros inseridos.

Executar docker-compose down sem -v:

Contêiner e rede são removidos, o volume pgdata persiste.

Executar docker-compose up -d novamente:

O contêiner é recriado usando os dados presentes no volume pgdata.

A mesma consulta SELECT * FROM usuarios; mostrará os registros anteriores — demonstrando persistência.