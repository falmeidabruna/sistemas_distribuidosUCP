import socket

IP_SERVIDOR = '127.0.0.1'
PORTA = 12345
BUFFER = 1024


def iniciar_cliente() -> None:
    frase = input('Digite uma frase para enviar ao servidor: ')

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print('\nTentando conectar ao servidor...')
        print(f'IP do servidor: {IP_SERVIDOR}')
        print(f'Porta do servidor: {PORTA}')

        cliente.connect((IP_SERVIDOR, PORTA))
        print('Conexão com o servidor realizada com sucesso.')

        cliente.sendall(frase.encode('utf-8'))
        print(f'Mensagem enviada ao servidor: {frase}')

        resposta = cliente.recv(BUFFER).decode('utf-8')
        print(f'Resposta recebida do servidor: {resposta}')
    except ConnectionRefusedError:
        print('Erro: conexão recusada. Verifique se o servidor está em execução.')
    except Exception as erro:
        print(f'Erro na comunicação com o servidor: {erro}')
    finally:
        cliente.close()
        print('Conexão encerrada.')


if __name__ == '__main__':
    iniciar_cliente()