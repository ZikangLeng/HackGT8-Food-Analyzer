import serial
import time
import schedule


def main_func():
    arduino = serial.Serial('com6', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded = str(arduino_data[0:len(arduino_data)].decode("utf-8"))

    print(f'Collected readings from Arduino: {decoded}')

    arduino_data = 0
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used


print('Program started')

# Setting up the Arduino
schedule.every(3).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)