import socket
import headers as H 
import data_base_api as DB;

def start_server():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    server.bind(('127.0.0.1', 1028));
    server.listen()
    DB.DataBase.connect();
    print('server starts...')
    
    
    # while True:
    #     s_client, address = server.accept()
    #     request_path = parse_request_path(s_client);
    #     choose_endpoint(request_path);
        # content = 'content'.encode('UTF-8')
        # s_client.send(H.Headerors.H200.encode("UTF-8")+ content);

def parse_request_path(client):
    data = client.recv(1024).decode('UTF-8')
    return data.split(' ')[1];

def choose_endpoint(path):
    if path == '/get_list':
        DB.DataBase.get_list()
    elif path == '/add_item':
        DB.DataBase.add_item();
    elif path == '/remove_item':
        DB.DataBase.remove_item();
    elif path == '/update_item':
        DB.DataBase.update_item();
        



start_server()