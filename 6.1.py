from time import sleep
class TrafficLight:
    __color = 'Changing'
    def running(self):
        while True:
            print('Red! Stop!')
            sleep(7)
            print('Yellow! Wait!')
            sleep(2)
            print('Green! Go!')
            sleep(7)
            print('Yellow! Wait!')
            sleep(2)
trafficlight = TrafficLight()
trafficlight.running()