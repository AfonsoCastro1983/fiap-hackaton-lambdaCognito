def load_html():
    with open('logged.html', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    with open("background_videoframe.jpeg", "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')

    conteudo = conteudo.replace('{{ BACKGROUND }}', 'data:image/png;base64,'+base64_string)
    
    return conteudo

def lambda_handler(event, context):
    # O evento contém as informações do usuário logado
    user_pool_id = event['userPoolId']
    username = event['userName']
    token = event['request']['groupConfiguration']

    conteudo = load_html()
    conteudo = conteudo.replace('{{ Fulano }}', username)
    conteudo = conteudo.replace('{{ Token }}', token)

    return {
        "statusCode": 200,
        "headers": {'Content-type': 'text/html'},
        "body": conteudo
    }