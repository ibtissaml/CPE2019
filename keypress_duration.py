from pynput import keyboard  # pip install pynput
from time import time
from sys import exit


def pressed(key): 
    delta_t = str(time() - t0)[0:5] 
    print(key, "is pressed for", delta_t, "seconds")
    return False


def released(key):
    return False


while True:
	try:
		with keyboard.Listener(on_press = released) as l1: 
			l1.join()
		t0 = time()
		with keyboard.Listener(on_release = pressed) as l2:
			l2.join()
	except KeyboardInterrupt:
		print("bye bye!")
		exit(0)
