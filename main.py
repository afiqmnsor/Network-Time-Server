import socket

def get_time_from_server(server_address, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Connect to the server
            client_socket.connect((server_address, server_port))

            # Send a request to the server
            client_socket.sendall(b"get_time")

            # Receive the response from the server
            data = client_socket.recv(1024) # Accepting 1024 bytes of data
            
            # Extract date and time from the response and decode to string
            date_time_bytes = [part.decode() for part in data.split()[1:3]]  # Decode bytes to string
            date_time_str = ' '.join(date_time_bytes)  # Join date and time with a space
            return date_time_str  # Return date and time as string

        except ConnectionError:
            raise ConnectionError("Failed to connect to the server.")

        except TimeoutError:
            raise TimeoutError("Connection to the server timed out.")

if __name__ == "__main__":
    # Server address and port
    server_address = "time-a-wwv.nist.gov"
    server_port = 13

    # Get the current time from the server
    try:
        current_time = get_time_from_server(server_address, server_port)
        print("Current date and time received from the server:", current_time)

    except (ConnectionError, TimeoutError) as e:
        print("Error:", e)