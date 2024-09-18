from time import sleep
k = 0
while True:
    with open('C:/Users/benja/Desktop/alarm.txt', 'w') as file:
        file.write(str(k))
        k = k + 1
        file.close()
        sleep(1)