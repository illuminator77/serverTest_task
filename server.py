import socket
import threading
import time
import re


PORT = 5050
SERVER = socket.gethostbyname('localhost')
FORMAT = 'utf-8'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind( (SERVER,PORT) )


def handle_client(cleint_socket, addr):
    print(f"Connect{addr}")
    cleint_socket.send("Command kit: !summaryCommand, !HelpInfoSummaryCommand, !disconnected ".encode())
    connected = True

    while connected:
        request = cleint_socket.recv(1024)
        response = request.decode(FORMAT)

        if response == "!disconnected":
            cleint_socket.send("Server close ".encode())
            connected = False

        elif response == "!HelpInfoSummaryCommand":
            cleint_socket.send("Формат данных BBBBxNNxHH:MM:SS.zhqxGGCR \n Где BBBB - номер участника x - пробельный символ NN - id канала \n HH - Часы MM - минуты SS - секунды zhq - десятые сотые тысячные GG \n - номер группы CR - «возврат каретки» (закрывающий символ)".encode())

        elif response == "!summaryCommand":

            cleint_socket.send("Enter data \" BBBBxNNxHH:MM:SS.zhqxGGCR (0002 C1 01:13:02.877 00[CR]) \"".encode())
            response_summary = cleint_socket.recv(1024).decode(FORMAT)
            log_file = open('log.txt', 'a')
            if response_summary != None:
                match = re.findall(r'([0-9]{4,4})+\s(.{2})+\s([0-2][0-9]:[0-5][0-9]:[0-6][0-9])\.([0-9]{3,3})+\s([0-9]{2,2})([\[ \]A-Z]{4,4})',response_summary)
                if match == []:
                    print("sorry your data not correct please type new data")
                    cleint_socket.send("sorry your data not correct please type new data \npress any key to continue".encode())
                else:
                    if match[0][4] == '00':
                        cleint_socket.send(f"Ok Формат прошел проверку и записан - спортсмен, нагрудный номер {match[0][0]} прошёл отсечку {match[0][1]} в {match[0][2]}".encode())
                    else:
                        cleint_socket.send("Ok Формат прошел проверку и записан".encode())
                    log_file.write(response_summary + '\n')

            log_file.close()


        elif response == "None":
            cleint_socket.send("Отклика нет".encode())

        else:
            cleint_socket.send("Неизвестный запрос".encode())


    print("server close")
    cleint_socket.close()



def start():
    server_socket.listen(5)
    while True:
        cleint_socket, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client,args=(cleint_socket,addr))
        thread.start()

print(f"server is starting {SERVER}")
start()
