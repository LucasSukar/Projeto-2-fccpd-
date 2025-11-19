# DESAFIO 1 — Containers em Rede

## Objetivo
Criar dois containers Docker que se comunicam usando uma **rede personalizada**.  
- Um container executa um **servidor web Flask**.  
- O outro executa um **cliente** que envia requisições periódicas ao servidor.

---

## Descrição Geral
O projeto possui dois serviços:

### Servidor Web (`web/`)
- Desenvolvido em **Python + Flask**.
- Responde na rota `/` com: status, hostname e horário.
- Roda na porta interna **8080**.

### Cliente (`client/`)
- Baseado em **Alpine Linux**.
- Executa um script (`client.sh`) que envia requisições contínuas ao servidor.
- Exibe logs com as respostas recebidas.

Ambos estão na mesma rede Docker criada pelo `docker-compose.yml`.

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
