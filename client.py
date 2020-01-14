import socketserver, socket, sys

msg=""

def create_tcp_socket():
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print("failed to create socket")
        sys.exit()
    print("socket created successfully")
    return sock;

def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("hostname could not be resolved")
        sys.exit()

    return remote_ip

def send_data(serversocket,payload):
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print("send failed")
        sys.exit()
    print("payload sent successfully")

def main():
    try:    
        host = "www.google.com"
        port = 80
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
        bufferSize = 4096

        s = create_tcp_socket()

        remote_ip = get_remote_ip(host)

        s.connect((remote_ip,port))
        print("socket connected to "+ host +" on ip "+remote_ip)

        send_data(s,payload)
        s.shutdown(socket.SHUT_WR)

        full_data = b" "
        while True:
            data = s.recv(bufferSize)
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

if __name__ == "__main__":
    main()