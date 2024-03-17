import time
import threading
import keyboard
import mouse
import pygetwindow as gw

class AutoClicker:
    def __init__(self):
        self.cps = 10  
        self.running = False
        self.mode = "toggle"  
        self.bind_key = "r"  
        self.target_window = None 

    def start_clicking(self):
        self.running = True
        while self.running:
            start_time = time.time()
            if self.target_window is None or gw.getActiveWindow().title == self.target_window:
                if self.mode == "toggle":
                    mouse.click(button="left")
                elif self.mode == "press":
                    mouse.press(button="left")
                    time.sleep(0.1)
                    mouse.release(button="left")
                elapsed_time = time.time() - start_time
                time.sleep(max(0, 1 / self.cps - elapsed_time))
            else:
                time.sleep(0.1)

    def stop_clicking(self):
        self.running = False

    def change_cps(self, cps):
        self.cps = cps

    def change_mode(self, mode):
        self.mode = mode

    def change_bind_key(self, key):
        self.bind_key = key

    def change_target_window(self, title):
        self.target_window = title

    def listen_for_bind_key(self):
        while True:
            if keyboard.is_pressed(self.bind_key):
                if self.running:
                    self.stop_clicking()
                else:
                    threading.Thread(target=self.start_clicking).start()
                time.sleep(0.2)  

auto_clicker = AutoClicker()

threading.Thread(target=auto_clicker.listen_for_bind_key).start()

while True:
    print("1. Ilość CPS")
    print("2. Zmień tryb (toggle/press)")
    print("3. Bind lpm")
    print("4. Wybierz okno mc")
    print("5. Taktyczny quit")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        cps = int(input("Podaj cps: "))
        auto_clicker.change_cps(cps)
    elif choice == "2":
        mode = input("tryb (toggle/press): ")
        if mode in ["toggle", "press"]:
            auto_clicker.change_mode(mode)
        else:
            print("ty tempy chuju wybierz spośród 'toggle' lub 'press'")
    elif choice == "3":
        key = input("bind lpm: ")
        auto_clicker.change_bind_key(key)
    elif choice == "4":
        print("Dostępne okna:")
        for window in gw.getAllTitles():
            print(window)
        title = input("Wybierz okno: ")
        auto_clicker.change_target_window(title)
    elif choice == "5":
        break
    else:
        print("Nieprawidłowa opcja debilu")
