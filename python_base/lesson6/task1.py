# Задание 1 из домашней работы №6

import time

class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self):
        for i in range(3):
            if (i == 0):
                print(TrafficLight.__color[0])
                time.sleep(7)
            elif (i == 1):
                print(TrafficLight.__color[1])
                time.sleep(2)
            elif (i == 2):
                print(TrafficLight.__color[2])
                time.sleep(5)

TrafficLight = TrafficLight()
TrafficLight.running()
