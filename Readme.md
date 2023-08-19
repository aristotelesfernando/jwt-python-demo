## Geração e Validação de Token JWT

### 1- Crie um virtual enviroment para a aplicação
#### $ virtualenv venv
#### $ venv/bin/activate 

### 2 - Instale as libs necessárias
#### $ pip install -r requirements.txt 

### 3 - Gerar certificado autoassinado
#### $ openssl req -x509 -nodes -newkey rsa:2048 -keyout private_key.pem -out public_key.pem -subj "/CN=jwt-turorial"
