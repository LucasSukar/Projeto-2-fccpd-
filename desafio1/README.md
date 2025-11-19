# DESAFIO 1 — Containers em Rede

## Objetivo
Criar dois containers Docker que se comunicam usando uma **rede personalizada**.  
- Um container executa um **servidor web Flask**.  
- O outro executa um **cliente** que envia requisições periódicas ao servidor.

---

## Como funciona
O projeto possui dois serviços conectados na mesma rede Docker:

### Servidor Web (`web/`)
- Responde na rota `/` com status, hostname e horário.
- Executa na porta interna **8080**.

### Cliente (`client/`)
- Executa um script (`client.sh`) que envia requisições contínuas ao servidor.
- Exibe no terminal os logs com as respostas.

A comunicação entre eles ocorre pela rede criada no `docker-compose.yml`, permitindo que o cliente acesse o servidor usando `http://web:8080`.

---

## Arquivos Principais

### docker-compose.yml
- Define os serviços `web` e `client`.
- Usa `build` para criar cada imagem.
- Usa `depends_on` para iniciar cliente após o servidor.
- Coloca ambos na mesma rede.  
  Acesso interno: **http://web:8080**

### Pasta web/
- `app.py`: servidor Flask, retorna JSON com status e horário.
- `requirements.txt`: instala Flask.
- `Dockerfile`: prepara imagem Python e executa `app.py`.

### Pasta client/
- `client.sh`: envia requisições em loop usando `curl`.
- `Dockerfile`: instala curl e executa o script.

---

## Como Executar
```bash
chmod +x run.sh
./run.sh
