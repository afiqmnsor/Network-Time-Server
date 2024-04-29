# Connect To A Network Time Server (Using Python)

## Socket Programming
Sockets are used for client and server interaction. The client(s) connect to the server, exchange information and disconnect. More about <a href="https://www.ibm.com/docs/en/i/7.5?topic=communications-socket-programming" target= "blank"> Socket Programming</a> can be found here.

## Network Time Protocol (NTP)
Network Time Protocol(NTP) is a protocol that allows the synchronization of system clocks. NTP provides reliability for transmitting and receiving accurate time over TCP/IP based networks. NTP is widely deployed to sync computer clocks to each other and to international standards.
 
## Overview
The script is designed to retrieve current time and date from a Network Time Server using Network time Protocol (NTP). It **establishes** a TCP connection with the Network Time Server, **sends** a request for the current time and date, **receives** the response, **decodes** binary data into a string and **returns** the data.

```python
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
```
### Output
![Example Image](https://github.com/addff/2403-ITT440/blob/main/10%25%20Individual%20Assignment/12%20MUHAMMAD%20AFIQ%20BIN%20MANSOR/TimeOutput.png)

 
## Script Documentation
<table>
  <tr>
    <td>Dependencies</td>
    <td><code>import socket</code></td>
  </tr>
  <tr>
    <td>Usage</td>
    <td>Specify <code>server_address</code> and <code>server_port</code> as the arguments to the <code>get_time_from_server()</code> function. The function returns the data and display as a string.</td>
  </tr>
  <tr>
    <td>Parameters</td>
    <td><code>server_address</code> (str): The IP Address or hostname of the server.<br>
        <code>port_address</code> (int): The port number of the time server.</td>
  </tr>
  <tr>
    <td>Returns</td>
    <td>string: The current time from the server.</td>
  </tr>
  <tr>
    <td>Raises</td>
    <td><code>ConnectionError</code>: If unable to connect to server.<br>
        <code>TimeoutError</code>: If connection times out.</td>
  </tr>
</table>

Refer comments to understand each code block.

The server address and server port (TCP) is hard-coded into the script for simplicity purpose.
