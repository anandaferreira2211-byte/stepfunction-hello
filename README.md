# StepFunction Olá 👋

Projeto de exemplo que integra **AWS Lambda** e **AWS Step Functions**.

---

## 💡 Objetivo
Demonstrar uma máquina de estado que chama a função Lambda `HelloLambdaLab`
e retorna uma saudação simples.

---

## ⚙️ Estrutura

lambda/
└── hello_lambda/
├── app.py
state_machine/
└── state_machine.asl.json


---

## ▶️ Execução
1. No console AWS, acesse **Step Functions** → selecione sua máquina `StepFunctionHello`.
2. Clique em **Iniciar execução**.
3. Use o seguinte JSON de entrada:
   ```json
   { "name": "Ananda" }
Resultado esperado:
{
  "statusCode": 200,
  "body": "Olá, Ananda — execução Step Functions OK!"
}

🧱 Tecnologias

AWS Lambda
AWS Step Functions
Python 3.11

📜 Licença
MIT © 2025

---

