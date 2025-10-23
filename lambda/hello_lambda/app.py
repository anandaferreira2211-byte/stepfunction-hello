def lambda_handler(event, context):
    name = event.get("name", "mundo")
    body = f"Olá, {name} — execução Step Functions OK!"
    return {
        "statusCode": 200,
        "body": body
    }
