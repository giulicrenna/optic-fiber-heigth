import socket
from time import sleep

import cv2 as cv

# get the hostname
host = socket.gethostname()
port = 8000  # initiate port no above 1024

# get instance
server_socket = socket.socket()
# look closely. The bind() function takes tuple as argument
server_socket.bind((host, port))  # bind host address and port together
# configure how many client the server can listen simultaneously
server_socket.listen(2)


def server_program(data):
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    conn.send(data.encode())  # send data to the client
    # conn.close()  # close the connection


def prom(videoSource=0,
         factor_h=2,
         factor_w=4,
         sensibility=.3):
    video = cv.VideoCapture(videoSource)
    isTrue, image = video.read()

    width_portion = image.shape[1] // factor_w
    height_portion = image.shape[0] // factor_h

    print("height: " + str(height_portion * 2) +
          " width: " + str(width_portion * 4))

    # height, width
    # p7 is higher than p0
    p0 = image[0:height_portion, 0:width_portion]
    p1 = image[0:height_portion, width_portion:width_portion * 2]
    p2 = image[0:height_portion, width_portion * 2:width_portion * 3]
    p3 = image[0:height_portion, width_portion * 3:width_portion * 4]
    p4 = image[height_portion:height_portion * 2, 0:width_portion]
    p5 = image[height_portion:height_portion *
               2, width_portion:width_portion * 2]
    p6 = image[height_portion:height_portion *
               2, width_portion * 2:width_portion * 3]
    p7 = image[height_portion:height_portion *
               2, width_portion * 3:width_portion * 4]

    count_p0 = 0  # counts pixels in each portion of image
    count_p1 = 0
    count_p2 = 0
    count_p3 = 0
    count_p4 = 0
    count_p5 = 0
    count_p6 = 0
    count_p7 = 0

    red_p0 = 0
    red_p1 = 0
    red_p2 = 0
    red_p3 = 0
    red_p4 = 0
    red_p5 = 0
    red_p6 = 0
    red_p7 = 0

    portions = [p0, p1, p2, p3, p4, p5, p6, p7]
    counts = [int(count_p0), int(count_p1), int(count_p2), int(count_p3), int(count_p4), int(count_p5), int(count_p6),
              int(count_p7)]
    reds = [red_p0, red_p1, red_p2, red_p3, red_p4, red_p5, red_p6, red_p7]

    for portion in range(len(portions)):
        for row in portions[portion]:
            for pixel in row:
                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                    pass
                else:
                    counts[portion] += 1
                    reds[portion] += pixel[2]

    for red in range(len(reds)):
        if counts[red] != 0:
            reds[red] = int(reds[red] / counts[red])
            # print(reds[red])

    inversed_reds = reds.copy()
    inversed_reds.reverse()
    # print(reds)

    flag = 255 * sensibility

    for red in range(len(inversed_reds)):
        if inversed_reds[red] > flag:
            if red == 0:
                server_program("80m")
                print("80 m")
                break
            if red == 1:
                server_program("70m")
                print("70 m")
                break
            if red == 2:
                server_program("50m")
                print("50 m")
                break
            if red == 3:
                server_program("40m")
                print("40 m")
                break
            if red == 4:
                server_program("30m")
                print("30 m")
                break
            if red == 5:
                server_program("20m")
                print("20 m")
                break
            if red == 6:
                server_program("10m")
                print("10 m")
                break
            if red == 7:
                server_program("5m")
                print("5 m")
                break


if __name__ == '__main__':
    while True:
        prom()

        sleep(.5)
