'''
uses pynput instead of keyboard
becauase of time.sleep(), sometimes a keypress was not registered
pynput uses threading and monitor keypress accurately

'''
from pynput import keyboard
import pyautogui
import threading
import numpy as np


active_state = False
INTERVAL = 0.2
delta = 0.05
np.random.uniform(INTERVAL-delta, INTERVAL+delta)

def on_press(key):
    global active_state
    if key == keyboard.Key.f2:
        active_state = not active_state
        # print(active_state)
        if active_state:
            print("Started. Press F2 again to stop")
        else:
            print("Stopped. Press F2 again to start")


def click():
    global active_state
    while True:
        if active_state:
            pyautogui.click(interval=INTERVAL)


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        # doesnt work
        return False

# main
print("Click bot ready")
print("Press F2 to start")
print("Press alt+f4 to exit")
print("==========")

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

thread = threading.Thread(target=click)
thread.start()

