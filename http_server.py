import socket
from http import HTTPStatus

HOST = '127.0.0.1'
PORT = 8888

server_addr = (HOST, PORT)
end_of_stream = '\r\n\r\n'


def handle_client(connection, addr):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            print('Received:', data)
            if not data:
                break
            client_data += data.decode()
            if end_of_stream in client_data:
                break
        req_method = client_data.split()[0]
        req_headers = client_data.split('\r\n')[1:-2]
        req_status = int(client_data.split('status=')[1].split()[0])
        try:
            status = HTTPStatus(req_status)
        except ValueError:
            status = HTTPStatus(200)

        status_line = f"HTTP/1.1 {status.value} {' '.join(status.name.split('_'))}\r\n"

        response = (f'Request Method: {req_method}\r\n'
                    f'Request Source: {addr}\r\n'
                    f"Response Status: {status.value} {' '.join(status.name.split('_'))}\r\n")
        for header in req_headers:
            response += f'{header}\r\n'

        connection.send(status_line.encode() + response.encode())


with socket.socket() as srv_socket:
    srv_socket.bind(server_addr)
    print(f'Started socket on {HOST}:{PORT}')
    srv_socket.listen()

    while True:
        client_conn, client_addr = srv_socket.accept()
        handle_client(client_conn, client_addr)
        print(f'Sent data to {client_addr}')
