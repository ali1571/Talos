import pygetwindow as gw
import pyautogui
import time
import pyperclip
from PIL import ImageGrab
import pytesseract
import random
import tkinter as tk
import keyboard
from numbergenonly import generate_phone_number

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

sidebar_items = [
    # {'name': 'Olivia', 'offset_x': 100, 'offset_y': 277}, blocked
    {'name': 'Emma', 'offset_x': 100, 'offset_y': 281},
    #{'name': 'Sophie', 'offset_x': 100, 'offset_y': 331},
    {'name': 'Amelia', 'offset_x': 100, 'offset_y': 351},
    {'name': 'Lily', 'offset_x': 100, 'offset_y': 400},
    {'name': 'Miranda', 'offset_x': 100, 'offset_y': 445},
    {'name': 'Hazel', 'offset_x': 100, 'offset_y': 475},
    {'name': 'Zoe', 'offset_x': 100, 'offset_y': 530},
    {'name': 'Ella', 'offset_x': 100, 'offset_y': 545},
    # {'name': 'Luna', 'offset_x': 100, 'offset_y': 575},
    {'name': 'Hannah', 'offset_x': 100, 'offset_y': 631},
    {'name': 'Claire', 'offset_x': 100, 'offset_y': 665},
    {'name': 'Elizabeth', 'offset_x': 100, 'offset_y': 700},
    {'name': 'Eleanor', 'offset_x': 100, 'offset_y': 745},
    {'name': 'Ailany', 'offset_x': 100, 'offset_y': 800},
    {'name': 'Ailany', 'offset_x': 100, 'offset_y': 840},
    {'name': 'Camila', 'offset_x': 100, 'offset_y': 875},
    {'name': 'Valentina', 'offset_x': 100, 'offset_y': 905},
    {'name': 'Valentina', 'offset_x': 100, 'offset_y': 945},
    {'name': 'Athena', 'offset_x': 100, 'offset_y': 980},
    {'name': 'Scottie', 'offset_x': 100, 'offset_y': 1025},
    {'name': 'Mary', 'offset_x': 100, 'offset_y':  1060},
    {'name': 'Johan Renata', 'offset_x': 100, 'offset_y': 1100},
]


def highlight_region(x, y, w, h, duration=2000):
    root = tk.Tk()
    root.overrideredirect(True)  # no window borders
    root.attributes('-alpha', 0.3)  # transparent
    root.attributes('-topmost', True)  # always on top
    root.geometry(f'{w}x{h}+{x}+{y}')
    root.configure(bg='red')
    root.after(duration, root.destroy)  # disappears after 2 seconds
    root.mainloop()


dm = ["💸 What's a completely normal amount of money that would genuinely change your life right now? 🤔",
      "🤑If I gave you $10k but you had to spend it all on making more money, where would it go? 📈",
      "💰 You can invest in one thing only: yourself, a business, or the stock market. Which gets the money? 👀"]

print(gw.getAllTitles())
win = gw.getWindowsWithTitle('\u200eQWERTS1571')[0]
win.activate()  # brings it to focus

win_x = win.left
win_y = win.top
print(win_x, win_y)

i = 0

time.sleep(0.5)

with open("link.txt", "r") as f:
    for item in sidebar_items:
        # open sidebar
        pyautogui.click(win_x + 41, win_y + 62)  # hamburger
        time.sleep(0.5)  # wait for sidebar to open
        print("hamburger")

        # click the sidebar item
        pyautogui.click(win_x + item['offset_x'], win_y + item['offset_y'])
        print("clicked the acc", sidebar_items[i]['name'])

        success_count = 0
        print("successful dms on", sidebar_items[i]['name'], 'are', success_count)
        time.sleep(0.5)
        location = pyautogui.locateOnScreen('saved_msg.png', confidence=0.7)

        loc = True
        time.sleep(0.7)
        f_iter = iter(f)
        while success_count != 1:

            try:
                line = next(f_iter)
                time.sleep(0.5)

                if location:
                    time.sleep(0.5)
                    pyautogui.click(location)





                while True:
                    key = keyboard.read_key()
                    if key == 'enter':
                        break

                    # pyautogui.press('enter')
                time.sleep(0.5)
                success_count += 1
                print("success count : ", success_count)


            except StopIteration:
                print("No more lines")

        if loc == False:
            print("cudnt identify savedmsgs breaking FOR too")
            break
        time.sleep(1)
        i += 1



