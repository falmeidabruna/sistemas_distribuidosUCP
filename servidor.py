import socket

HOST = '0.0.0.0'
PORTA = 12345
BUFFER = 1024


def iniciar_servidor() -> None:
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORTA))
    servidor.listen()

    print('==========================================================')
    print('SERVIDOR TCP INICIADO')
    print(f'Host configurado: {HOST}')
    print(f'Porta configurada: {PORTA}')
    print('Status: aguardando conexões...')
    print('==========================================================')

    try:
        while True:
            conexao, endereco_cliente = servidor.accept()
            ip_cliente, porta_cliente = endereco_cliente

            print('\nNova conexão recebida!')
            print(f'IP do cliente: {ip_cliente}')
            print(f'Porta do cliente: {porta_cliente}')

            try:
                mensagem = conexao.recv(BUFFER).decode('utf-8')
                print(f'Mensagem recebida do cliente: {mensagem}')

                resposta = mensagem.upper()
                print(f'Resposta enviada ao cliente: {resposta}')

                conexao.sendall(resposta.encode('utf-8'))
                print('Conexão com o cliente encerrada pelo servidor.')
            except Exception as erro:
                print(f'Erro ao processar a conexão: {erro}')
            finally:
                conexao.close()
    except KeyboardInterrupt:
        print('\nServidor finalizado manualmente.')
    finally:
        servidor.close()
        print('Socket do servidor fechado com sucesso.')


if __name__ == '__main__':
    iniciar_servidor()