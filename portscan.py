import socket

def bannerGrabing(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.send(b'200 OK\r\n')
        data = str(sock.recv(256), 'ascii')
        sock.close()
        return data.strip('b\'\\n\\r')
    except Exception:
        print("[!] - Houve um erro ao receber dados do servidor")
        pass

def scanHost(host):
    socket.setdefaulttimeout(5)
    print("[*] - Scan iniciado")
    for port in range(1, 65535):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not sock.connect_ex((host, port)):
                print(f"[!] - Porta {port} aberta")
                print(f"[!] - Banner:\n{bannerGrabing(host, port)}")
        except socket.error as err:
            if 'timed out' in str(err):
                print(f"[!] - Porta {port} filtrada")
            else:
                print(f"[!] - Porta {port} fechada")
        finally:
            sock.close()

def main():
    host = input("[+] - Digite o host: ")
    scanHost(host)

if __name__ == '__main__':
    main()