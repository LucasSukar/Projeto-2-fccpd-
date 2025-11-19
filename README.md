# DESAFIO 1

## Objetivo
Criar dois containers Docker que se comunicam entre si utilizando uma rede Docker personalizada.  
- O primeiro container atua como **servidor web**.  
- O segundo container realiza **requisições periódicas** ao servidor e exibe os resultados no terminal.

---

## Descrição
Este projeto contém uma arquitetura simples composta por dois containers:

### 1. Servidor Web (`web/`)
- Implementado em **Python + Flask**.  
- Expõe uma rota HTTP que retorna:
  - hostname do container;
  - horário atual;
  - mensagem de status.
- Executado na porta **8080** dentro do container.

### 2. Cliente de Requisições (`client/`)
- Baseado em **Alpine Linux**.
- Executa um script shell que:
  - faz requisições contínuas ao servidor;
  - exibe logs com as respostas obtidas;
  - permite validar a comunicação via rede Docker.

Ambos os containers são conectados a uma **rede Docker personalizada** criada pelo Docker Compose.

---

## Estrutura

### `docker-compose.yml`
Arquivo responsável por orquestrar os serviços.

Principais funções:
- cria a rede personalizada;
- define os serviços **web** e **client**;
- usa `depends_on` para garantir a ordem de inicialização;
- conecta ambos os containers à mesma rede.

Pontos importantes:
- O servidor é acessado internamente via:  
  **`http://web:8080`**
- O nome do serviço atua como DNS interno entao não é necessário IP.

---

## Pasta `web/` — Servidor Web

### **`app.py`**
Aplicação Flask que responde em JSON contendo:
- mensagem de funcionamento;
- hostname do container;
- horário atual formatado.

### **`requirements.txt`**
Inclui as dependências:
- Flask

### **`Dockerfile`**
Define:
- imagem base Python 3.10;
- instalação das dependências;
- cópia do código do servidor;
- comando de inicialização (`python app.py`).

---

## Pasta `client/` — Cliente de Requisições

### **`client.sh`**
Script responsável por:
- definir o endereço do servidor (`http://web:8080/`);
- realizar requisições em loop infinito;
- exibir horário e resposta do servidor a cada tentativa;
- aguardar alguns segundos antes da próxima requisição.

### **`Dockerfile`**
Configura:
- Alpine Linux como base;
- instalação do `curl`;
- cópia e permissão do script;
- execução automática do script.

---

## ▶ Como Executar

### 1. Dar permissão ao script
```bash
chmod +x run.sh
