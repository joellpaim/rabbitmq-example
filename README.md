# 🐇 RabbitMQ Example with Python & Poetry

---

Este projeto é uma demonstração simples e didática do uso do **RabbitMQ** com **Python**, utilizando o gerenciador de dependências **Poetry**. Ele exemplifica o envio e o recebimento de mensagens através de uma fila chamada `hello`.

---

## 📦 Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org)
- [Poetry](https://python-poetry.org/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [pika](https://pika.readthedocs.io/en/stable/)

---

## 🧱 Estrutura do Projeto

```md
rabbitmq_example/
├── pyproject.toml # Configuração do Poetry
├── README.md # Documentação do projeto
├── rabbitmq_example/
│ ├── **init**.py
│ ├── send.py # Script para envio de mensagens
│ └── receive.py # Script para consumir mensagens
```

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/rabbitmq_example.git
cd rabbitmq_example
```

### 2. Instale as dependências com Poetry

```bash
poetry install
```

### 3. Suba o RabbitMQ com Docker (se necessário)

```bash
docker run -d --name rabbitmq \
  -p 5672:5672 -p 15672:15672 \
  rabbitmq:3-management
```

A interface de gerenciamento ficará disponível em:
🔗 [http://localhost:15672](http://localhost:15672)

Login: `guest`
Senha: `guest`

---

## ✉️ Enviando uma mensagem

```bash
poetry run python rabbitmq_example/send.py
```

Saída esperada:

```
 [x] Sent 'Hello, RabbitMQ!'
```

---

## 📥 Recebendo uma mensagem

Em outro terminal:

```bash
poetry run python rabbitmq_example/receive.py
```

Saída esperada:

```
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received Hello, RabbitMQ!
```

---

## 🧠 Conceitos Demonstrados

- Declaração de fila com `queue_declare`
- Envio de mensagem com `basic_publish`
- Consumo de mensagens com `basic_consume`
- Callback para processar mensagens recebidas
- Uso do `BlockingConnection` do `pika`

---

## 🧪 Teste rápido sem Poetry (opcional)

Você também pode rodar os scripts diretamente (caso tenha o `pika` instalado globalmente):

```bash
python rabbitmq_example/send.py
python rabbitmq_example/receive.py
```

---

## 📚 Referências

- [RabbitMQ Tutorial (Python)](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
- [Documentação do Pika](https://pika.readthedocs.io/en/stable/)
- [Poetry](https://python-poetry.org/docs/)

---

## 🛠️ Autor

Desenvolvido por **Joel Paim** 💻

Caso queira adaptar ou usar como base em aulas, sinta-se à vontade!

---
