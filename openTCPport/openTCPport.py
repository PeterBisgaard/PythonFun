# DISP:TEXT "WAITING..."
import socket

# Angiv host (kan være en tom streng for at lytte på alle tilgængelige netværksgrænseflader) og port
host = ""
port = 2000

# Opret en socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket til den angivne host og port
server_socket.bind((host, port))

# Lyt efter indkommende forbindelser
server_socket.listen(5)
print(f"Server lytter på port {port}...")

# Accepter en indkommende forbindelse
client_socket, client_address = server_socket.accept()
print(f"Forbundet til {client_address}")

while True:
    # Modtag data fra klienten
    data = client_socket.recv(1024)

    # Håndter dataen (du kan tilpasse denne del efter dine behov)
    if data:
        received_data = data.decode("utf-8")
        print(f"Modtaget data: {received_data}")

        # Hvis dataen er 'Q', luk serveren
        if received_data.strip() == "Q":
            print("Serveren lukker...")
            break

# Luk forbindelsen til klienten
client_socket.close()

# Luk serverens hovedsocket
server_socket.close()
