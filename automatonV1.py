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

pyautogui.PAUSE = 0.15

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

sidebar_items = [
    # {'name': 'Olivia', 'offset_x': 100, 'offset_y': 277}, blocked
    #{'name': 'Emma', 'offset_x': 100, 'offset_y': 275},
    {'name': 'Amelia', 'offset_x': 100, 'offset_y': 303},
    {'name': 'Lily', 'offset_x': 100, 'offset_y': 340},
    #{'name': 'Miranda', 'offset_x': 100, 'offset_y': 383},
    {'name': 'Hazel', 'offset_x': 100, 'offset_y': 420},
    {'name': 'Zoe', 'offset_x': 100, 'offset_y': 460},
    #{'name': 'Ella', 'offset_x': 100, 'offset_y': 500},
    #{'name': 'Luna', 'offset_x': 100, 'offset_y': 540},
    {'name': 'Hannah', 'offset_x': 100, 'offset_y': 581},
    {'name': 'Claire', 'offset_x': 100, 'offset_y': 622},
    {'name': 'Elizabeth', 'offset_x': 100, 'offset_y': 663},
    {'name': 'Eleanor', 'offset_x': 100, 'offset_y': 703},
    {'name': 'Ailany', 'offset_x': 100, 'offset_y': 743}, #cant send dmLucas?
    {'name': 'Ailany', 'offset_x': 100, 'offset_y': 782},
    {'name': 'Camila', 'offset_x': 100, 'offset_y': 822},
    {'name': 'Valentina', 'offset_x': 100, 'offset_y': 861},
    {'name': 'Valentina', 'offset_x': 100, 'offset_y': 903},
    {'name': 'Athena', 'offset_x': 100, 'offset_y': 940},
    {'name': 'Scottie', 'offset_x': 100, 'offset_y': 983},
    {'name': 'Mary', 'offset_x': 100, 'offset_y':  1023},
    {'name': 'Johan Renata', 'offset_x': 100, 'offset_y': 1063},
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
            print("clicked the acc", item['name'])


            success_count = 0
            print("successful dms on", sidebar_items[0]['name'], 'are', success_count)
            time.sleep(1)
            location = pyautogui.locateOnScreen('saved_msg.png', confidence=0.7)


            loc = True
            time.sleep(0.5)
            f_iter = iter(f)
            while success_count != 1:

                try:
                    line = next(f_iter)


                    if location:
                        time.sleep(0.5)
                        pyautogui.click(location)

                    else:
                        loc = False
                        print("cudnt identify savedmsgs breaking while")
                        break

                    time.sleep(1)

                    #pyautogui.click(win_x + 700, win_y + 1400)

                    pyautogui.hotkey('ctrl', 'a')

                    pyautogui.press('backspace')

                    pyperclip.copy(str(line))  # copy to clipboard
                    print(line)
                    pyautogui.hotkey('ctrl', 'v')# paste it
                    pyautogui.press('enter')
                    i +=1
                    time.sleep(1)  # wait for number to appear after pressing enter
                    pyautogui.click(win_x + 680, win_y + 1080) #clicking number
                    time.sleep(1)

                    # grab just the region where the text appears

                    text_region = ImageGrab.grab(bbox=(
                        win_x + 550,  # pushed right
                        win_y + 30,  # pushed up
                        win_x + 750,  # pushed right
                        win_y + 60  # pushed up
                    ))

                    highlight_region(
                        win_x + 550,
                        win_y + 30,
                        750 - 550,
                        60 - 30
                    )

                    time.sleep(1)
                    text = pytesseract.image_to_string(text_region).strip().lower()
                    print(repr(text))
                    time.sleep(1)






                    #string manipulation, since typewrite on works in ascii so had to copy paste emojis
                    msg_string = str(text).split(' ')[0].capitalize()
                    msg_string=(msg_string+"?")
                    print(msg_string)
                    time.sleep(0.5)



                    pyautogui.typewrite(msg_string, interval=0.09)

                    while True:
                        key = keyboard.read_key()
                        if key == 'enter':
                            break

                    #pyautogui.press('enter')
                    time.sleep(1)
                    success_count += 1
                    print("success count : ", success_count)


                except StopIteration:
                    print("No more lines")
                print("done with", item['name'])


            if loc == False:
                print("cudnt identify savedmsgs breaking FOR too")
                break
            time.sleep(2)
            i +=1





