# ✅ Projeto de Qualidade 

Este projeto de QA abrange testes funcionais e não funcionais realizados sobre a plataforma [Restful Booker](https://github.com/prof-desiglo/restful-booker-platform), disponível online em [https://www.automationintesting.online](https://www.automationintesting.online) e também para execução local.

---

## 🧪 Testes de API (Postman)

- Local: `qa-challenge/postman/`
- Ferramenta: [Postman](https://www.postman.com/)
- Endpoint: `http://localhost:3003/api/room`

### ✔️ Cobertura dos testes:

- `GET /api/room`: lista todos os quartos (positivo e negativo)
- `POST /api/room`: cria um quarto (positivo e negativo)
- `PUT /api/room/:id`: edita quarto (positivo e negativo)
- `DELETE /api/room/:id`: exclui quarto (positivo e negativo)
- Validações de:
  - Códigos de status: 200, 201, 400, 404, 500
  - Tempo de resposta
  - Estrutura do JSON no corpo da resposta

### ▶️ Como executar:

1. Importe o arquivo `restful-booker.postman_collection.json` no Postman
2. Configure o ambiente com o `restful-booker.postman_environment.json`
3. Execute a collection completa com o botão **Run**

---

## 🧑‍💻 Testes de Interface WEB (Selenium)

- Local: `qa-challenge/selenium/`
- Ferramenta: [Selenium com Python](https://www.selenium.dev/)

### ✔️ Cobertura dos testes:

- Login com credenciais válidas (positivo)
- Login com credenciais inválidas (negativo)
- Acesso ao dashboard após login
- Criação de novo quarto
- Exclusão de um quarto

### ▶️ Como executar:

1. Crie um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute os testes:
   ```
   pytest tests/
   ```

---

## 📈 Testes de Performance (JMeter)

- Local: `qa-challenge/performance/`
- Ferramenta: [Apache JMeter](https://jmeter.apache.org/)

### Cenários de carga:

| Cenário         | Usuários Virtuais | Duração | Endpoint |
|-----------------|-------------------|---------|----------|
| Leve            | 20                | 1 min   | `/api/room` |
| Moderado        | 50                | 1 min   | `/api/room` |
| Pesado          | 100               | 1 min   | `/api/room` |

### ▶️ Como executar:

1. Abra o JMeter
2. Carregue o arquivo `restful-booker-performance.jmx`
3. Selecione o grupo de threads desejado
4. Clique em **Start**
5. Veja os resultados em `View Results Tree` ou `Summary Report`

### 📊 Resultados:

Estão disponíveis em:
```
qa-challenge/performance
```

---

## 🔐 Autenticação

Alguns testes (API e Web) requerem autenticação:

- **Usuário**: `admin`
- **Senha**: `password`

---

## 📹 Vídeo de Apresentação

[🔗 Link para o vídeo explicativo no YouTube](https://youtu.be/YO-mfMjU3rA)

---

## 👨‍💻 Autores

Arthur Fenili RM 552752
Enzo Antunes Oliveira RM 553185
Vinicío Raphael RM 553813
