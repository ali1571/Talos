import pygetwindow as gw
import pyautogui
import time
import pyperclip
from PIL import ImageGrab
import pytesseract
import random
import tkinter as tk
from numbergenonly import generate_phone_number

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

sidebar_items = [
    #{'name': 'Olivia', 'offset_x': 100, 'offset_y': 277},
    #{'name': 'Emma', 'offset_x': 100, 'offset_y': 331},
    #{'name': 'Sophie', 'offset_x': 100, 'offset_y': 381},
    #{'name': 'Amelia', 'offset_x': 100, 'offset_y':439 },
    #{'name': 'Lily', 'offset_x': 100, 'offset_y': 488},
   # {'name': 'Miranda', 'offset_x': 100, 'offset_y': 539},
    #{'name': 'Hazel', 'offset_x': 100, 'offset_y': 589},
    #{'name': 'Zoe', 'offset_x': 100, 'offset_y': 639},
    #{'name': 'Ella', 'offset_x': 100, 'offset_y': 688},
    {'name': 'Luna', 'offset_x': 100, 'offset_y': 740},
    {'name': 'Hannah', 'offset_x': 100, 'offset_y': 788},
    {'name': 'Claire', 'offset_x': 100, 'offset_y': 838},
    {'name': 'Elizabeth', 'offset_x': 100, 'offset_y': 889},
]

#numbers = []

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

#def clean_num (numarray):
#    return [str(num)[1:] for num in numarray]

#numbers = clean_num(numbers)

print(gw.getAllTitles())
win = gw.getWindowsWithTitle('\u200eQWERTS1571')[0]
win.activate()  # brings it to focus


win_x = win.left
win_y = win.top
print(win_x, win_y)

i = 0

for item in sidebar_items:
    # open sidebar
    pyautogui.click(win_x + 41, win_y + 62)  # hamburger
    time.sleep(0.5)  # wait for sidebar to open
    print("hamburger")


    # click the sidebar item
    pyautogui.click(win_x + item['offset_x'], win_y + item['offset_y'])
    print("clicked the acc", sidebar_items[0]['name'])


    success_count = 0
    print("successful dms on", sidebar_items[0]['name'], 'are', success_count)
    time.sleep(1)
    location = pyautogui.locateOnScreen('saved_msg.png', confidence=0.8)

    if location:
        pyautogui.click(location)
    while success_count != 3:
        print('entering numbers...')
        num = generate_phone_number()


        textfield = pyautogui.locateOnScreen('textfield.png', confidence=0.6)
        if textfield:
            pyautogui.click(textfield)
            pyperclip.copy(str(num))  # copy to clipboard
            print(num)
            pyautogui.hotkey('ctrl', 'v')  # paste it
            pyautogui.press('enter')
            i +=1
            time.sleep(0.8)  # wait for number to appear after pressing enter
            pyautogui.click(win_x + 680, win_y + 918) #clicking number
            time.sleep(0.8)

            # grab just the region where the text appears
            text_region = ImageGrab.grab(bbox=(
                win_x + 720,  # pushed right
                win_y + 870,  # pushed up
                win_x + 850,  # pushed right
                win_y + 910  # pushed up
            ))
            '''
            highlight_region(
                win_x + 720,
                win_y + 870,
                850 - 720,
                910 - 870
            )
            '''


            time.sleep(0.9)
            text = pytesseract.image_to_string(text_region).strip().lower()
            print(repr(text))
            time.sleep(0.5)

            if "view profile" in text:
                with open("found_nums", "a") as file:
                    file.write(num + "\n")

                pyautogui.click(win_x + 749, win_y + 899)
                print('clicked view profile')
                success_count+=1
                time.sleep(0.8)  # wait for box to appear after pressing enter

                #locating msgbox after clicking view profile
                msgbox = pyautogui.locateOnScreen('msgbox.png', confidence=0.6)
                print(msgbox)
                time.sleep(0.8)
                pyautogui.click(msgbox)
                time.sleep(0.8)

                #string manipulation, since typewrite on works in ascii so had to copy paste emojis
                msg_string = str(random.choice(dm))
                emoji1, emoji2 = msg_string[0], msg_string[len(msg_string)-1]

                time.sleep(1)
                pyperclip.copy(emoji1)
                pyautogui.hotkey('ctrl', 'v')

                pyautogui.typewrite(msg_string, interval=0.09)

                pyperclip.copy(emoji2)
                pyautogui.hotkey('ctrl', 'v')


                pyautogui.press('enter')
                time.sleep(1)

            else:
                pyautogui.click(textfield)

    time.sleep(1)



