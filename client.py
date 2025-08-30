import socket
import os


class Client:
    def __init__(self, server_host = "127.0.0.1", server_port = 1234):
        """_summary_

        Args:
            host (str, optional): _description_. Defaults to "127.0.0.1".
            port (int, optional): _description_. Defaults to 1234.
        """
        self.server_host = server_host
        self.server_port = server_port
    

    def connect_to_server(self):
        """_summary_
        """
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((self.server_host, self.server_port))
        except (ConnectionRefusedError, socket.timeout, OSError) as e:
            print(f"Server or socket down - description: {e}")
            os._exit(0)
