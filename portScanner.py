import socket

def port_scan(target, start_port, end_port):
    print(f"Port taraması başlatılıyor: {target}")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Açık")
        else:
            print(f"Port {port}: Kapalı")

        sock.close()

if __name__ == "__main__":
    target_host = input("Hedef IP adresini girin: ")
    start_port = int(input("Başlangıç portunu girin: "))
    end_port = int(input("Bitiş portunu girin: "))

    port_scan(target_host, start_port, end_port)
