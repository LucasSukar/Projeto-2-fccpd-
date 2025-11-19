# Desafio 2: Persistência de Dados (PostgreSQL + Volumes)

## Objetivo
Ensinar o conceito de Volumes no Docker. O objetivo é mostrar que containers perdem dados ao serem deletados, mas volumes mantêm dados independentemente do container.

##  Descrição do Projeto
Um banco de dados PostgreSQL que é inicializado automaticamente com uma tabela e dados. Um script de teste prova que, mesmo destruindo o banco, os dados inseridos anteriormente permanecem salvos.

##  Estrutura

### 1. `docker-compose.yml`
* **Service `postgres`**: Usa a imagem oficial `postgres:15`.
* **Environment**: Define as variáveis `POSTGRES_USER`, `PASSWORD` e `DB` para configurar o acesso automaticamente.
* **Volumes**:
    * `./init.sql:/docker-entrypoint-initdb.d/init.sql`: Mapeia o script local para a pasta especial do Postgres que executa scripts na inicialização.
    * `pgdata:/var/lib/postgresql/data`: Mapeia a pasta de dados interna do banco para um volume nomeado gerenciado pelo Docker.

### 2. `init.sql`
* Este arquivo contém SQL puro.
* Cria a tabela `usuarios` se ela não existir.
* Insere três registros iniciais: 'Lucas Sukar', 'Caio Lima', e 'Rodrigo'.

### 3. `roda.sh` 
Este script automatiza a prova de conceito:
1.  Sobe o banco (`docker-compose up`).
2.  Consulta os dados atuais.
3.  Destrói o container (`docker-compose down`).  aqui apagaria os dados se não houvesse volumes.
4.  Sobe o banco novamente.
5.  Consulta os dados de novo para provar que "Lucas, Caio e Rodrigo" ainda estão lá.

##  Como Fuciona
O volume `pgdata` atua como um HD externo virtual plugado no container. Quando o container morre, o "HD" é desconectado, mas os dados ficam nele. Quando um novo container nasce, o "HD" é reconectado, restaurando o estado anterior.

##  Como Executar
Execute o script de teste automatizado:
```bash
chmod +x roda.sh
./roda.sh
