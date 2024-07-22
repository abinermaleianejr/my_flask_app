import jwt
import datetime

# Chave secreta para codificação e decodificação do token
SECRET_KEY = 'oi'


def create_token(payload, secret_key=SECRET_KEY, exp_horas=1):
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=exp_horas)
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


def decode_token(token, secret_key=SECRET_KEY):
    try:
        decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        print(decoded_payload)

        return decoded_payload
    except jwt.ExpiredSignatureError:
        raise jwt.ExpiredSignatureError('Token expirado. Por favor, faça login novamente.')
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError('Token inválido. Por favor, faça login novamente.')


if __name__ == '__main__':
    # Exemplo de uso das funções
    dados = {'user_id': 123, 'username': 'usuario'}
    token = create_token(dados)
    print(f'Token JWT: {token}')

    try:
        decoded_data = decode_token(token)
        print(f'Dados decodificados: {decoded_data}')
    except jwt.ExpiredSignatureError as e:
        print(e)
    except jwt.InvalidTokenError as e:
        print(e)
