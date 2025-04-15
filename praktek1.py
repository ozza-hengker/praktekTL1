import keyboard
import threading
import time



print("Tekan 'a' untuk menyalakan sensor. Tekan 's' untuk menyalakan aktuator, Tekan 'd' untuk menyalakan sensor, Tekan 'ASD' untuk menyalak ketiganya sekaligus ")

    
def sensor_satu():
    while True:
        if keyboard.is_pressed('a'):
            print("Sensor 1 aktif")
            time.sleep(1)
    
def aktuator():
    while True:
        if keyboard.is_pressed('s'):
            print('Aktuator aktif')
            time.sleep(0.5)
    
def sensor_dua():
    while True:
        if keyboard.is_pressed('d'):
            print('Sensor 2 aktif')
            time.sleep(2)
            
   
t1 = threading.Thread(target=sensor_satu)
t2 = threading.Thread(target=aktuator)
t3 = threading.Thread(target=sensor_dua)

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
