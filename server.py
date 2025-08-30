import socket


class Server:
    def __init__(self, host = "0.0.0.0", port = 1234):
        """_summary_

        Args:
            host (str, optional): _description_. Defaults to "0.0.0.0".
            port (int, optional): _description_. Defaults to 1234.
        """
        self.host = host
        self.port = port


    def setup_listener(self):
        """_summary_
        """
        listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener_socket.bind((self.host, self.port))

        client, addr = listener_socket.accept()
