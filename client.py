import socket
import time
from configs.paths import *

def socket_client():
    """
    Create a socket client.
    Parameters: 
        None
    Returns: 
        Object: socket client object
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # client.settimeout(5)
    
    try:
        client.connect((HOST_NAME, int(HOST_PORT)))
        print(client.getsockname())
        while True:
            client.send(bytes('Hello', 'utf-8'))
            time.sleep(5)
            response = str(client.recv(1024), 'utf-8')
            print(response)
    except socket.error as e:
        if e.args[0] == 10061:
            time.sleep(5)
            print('Connection refused')
            socket_client()
   
    
    # print(client.settimeout(5))
    
    # message = input('-> ')
    # while True:
    #     client.send(bytes('Hello', 'utf-8'))
    #     response = str(client.recv(1024), 'utf-8')
    #     print(response)
    #     message = input('-> ')
    
    # while message.lower().strip() != 'exit':
    #     client.send(bytes(message, 'utf-8'))
    #     response = str(client.recv(1024), 'utf-8')
    #     print(response)
    #     message = input('-> ')
        
    client.close()

if __name__ == '__main__':
    socket_client()