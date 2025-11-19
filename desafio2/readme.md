# Desafio 2 — Comunicação entre Containers (Servidor + Cliente)

## Descrição Geral
Este projeto demonstra a comunicação entre dois containers Docker através de uma rede interna personalizada definida pelo `docker-compose.yml`.

A arquitetura possui dois serviços principais:

1. **Servidor Web** – Desenvolvido em Python + Flask.
2. **Cliente** – Executa requisições periódicas ao servidor e exibe os resultados.

Ambos operam dentro da mesma rede Docker.

---

## Como Funciona

### Servidor Web (`web/`)
- Responde na rota `/` exibindo:
  - Status da aplicação  
  - Hostname do container  
  - Data e horário atual
- Utiliza a porta interna **8080**.

### Cliente (`client/`)
- Executa o script `client.sh` em loop.
- Envia requisições contínuas para `http://web:8080`.
- Mostra no terminal todas as respostas recebidas do servidor.

A comunicação ocorre utilizando o nome do serviço definido no Compose, sem necessidade de IP.

---

## Arquitetura
O `docker-compose.yml` cria automaticamente uma rede interna onde:
- O servidor fica disponível como `web`.
- O cliente se conecta diretamente usando `http://web:8080`.

---

## Passo a Passo para Executar

### 1. Build e inicialização
No diretório do projeto:

```bash
docker-compose up --build
