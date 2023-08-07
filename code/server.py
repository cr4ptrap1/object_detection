import socket
import struct
import pickle
import cv2

def show_frame(frame):
    frame = pickle.loads(frame, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow("from client", frame)
    cv2.waitKey(1)

HOST = "192.168.0.221"
PORT = 20000
BUFFER_SIZE = 4096

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((HOST, PORT))
tcp_server.listen(10)

print("Server is starting...")

connection, address = tcp_server.accept()
print(f"Connected to: {address}")

payload_size = struct.calcsize(">L")

while True:
    all_data = b''

    while (len(all_data) < payload_size):
        all_data += connection.recv(BUFFER_SIZE)

    packed_message_size = all_data[:payload_size]
    all_data = all_data[payload_size:]
    message_size = struct.unpack(">L", packed_message_size)[0]

    while len(all_data) < message_size:
        all_data += connection.recv(BUFFER_SIZE)

    frame_data = all_data[:message_size]
    all_data = all_data[message_size:]

    #connection.sendall("Recieved!".encode())

    frame_data = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame_data = cv2.imdecode(frame_data, cv2.IMREAD_COLOR)
    cv2.imshow("from client", frame_data)
    cv2.waitKey(1)