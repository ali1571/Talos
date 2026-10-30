import pygetwindow as gw
import pyautogui
import time
import pyperclip
from PIL import ImageGrab, Image, ImageOps
import pytesseract
import random
import tkinter as tk
import keyboard
from numbergenonly import generate_phone_number

pyautogui.PAUSE = 0.15

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

sidebar_items = [
    #"Lily",
    #"Miranda",
    #"Ailany",
    #"Valentina", down
    #"Hazel",
    #"Ella", down
    #"Luna", down
   # "Hannah", down
    #"Claire",
   # "Elizabeth", down
    #"Eleanor",
    #"Camila",
    #"Athena",
    "Scottie",
    #"Mary", DOWN
    #"Johan",
    #"Shanice", down
    "Benjamin",
    "Brittney",
    "Adrianna",
    "Raylan",
    "Gretchen",
    "Irwin",
    "Ailany",
    "Valentina",
    "Genesis",
    #"Sophie",
    #"Zoe",
    #"Olivia",
    #"Emma",
]



def highlight_region(x, y, w, h, duration=1000):
    root = tk.Tk()
    root.overrideredirect(True)  # no window borders
    root.attributes('-alpha', 0.3)  # transparent
    root.attributes('-topmost', True)  # always on top
    root.geometry(f'{w}x{h}+{x}+{y}')
    root.configure(bg='red')
    root.after(duration, root.destroy)  # disappears after 2 seconds
    root.mainloop()


clicked_positions = []  # keep this at module/global level, outside sidebar_scan

def already_clicked(x, y, tolerance=15):
    for (px, py) in clicked_positions:
        if abs(x - px) < tolerance and abs(y - py) < tolerance:
            return True
    return False


def sidebar_scan(name, attempt = 1, max_attempts=5):

    clicked = False

    sidebar_region = ImageGrab.grab(bbox=(
        win_x + 60,  # left
        win_y + 161,  # top
        win_x + 255,  # right
        win_y + 1129  # bottom
    ))

    sidebar_region.save("debug_capture.png")

    #highlight_region(win_x + 60,
    #                 win_y + 161,
    #                 255 - 60,
    #                 1129 - 161,
    #                 duration=600)

    time.sleep(0.3)
    data = pytesseract.image_to_data(sidebar_region, output_type=pytesseract.Output.DICT)
    print(data['text'])
    print(data['conf'])
    for i, word in enumerate(data['text']):

        if word.strip().lower() in name.lower() and word.strip() != '':
            print("found", name, 'as', word.strip().lower())
            word_center_x = data['left'][i] + data['width'][i] // 2
            word_center_y = data['top'][i] + data['height'][i] // 2

            click_x = win_x + 60 + word_center_x
            click_y = win_y + 161 + word_center_y

            if already_clicked(click_x, click_y):
                print(name, "match at", click_x, click_y, "already used, skipping")
                continue  # keep looking for another match further down

            print("found", name, "at", click_x, click_y)
            pyautogui.click(click_x, click_y)
            clicked_positions.append((click_x, click_y))

            pyautogui.click(click_x, click_y)
            clicked = True
            print(name, "clicked")
            break

    if not clicked:
        if attempt >= max_attempts:
            print(name, "not found after", max_attempts, "attempts - giving up")
            return False

        print(f"{name} not visible, scrolling ( attempt {attempt}/{max_attempts})")

        scroll_x, scroll_y = 267, 369
        scroll_amount = -1000

        pyautogui.moveTo(scroll_x, scroll_y)
        print(f"placed cursor at {scroll_x}, {scroll_y}")
        pyautogui.scroll(scroll_amount)
        print("scrolled")

        return sidebar_scan(name, attempt=attempt+1, max_attempts=5)

    return True


print(gw.getAllTitles())
win = gw.getWindowsWithTitle('\u200eQWERTS1571')[0]
win.activate()  # brings it to focus



win_x = win.left
win_y = win.top
print(win_x, win_y)

start_time = time.time()


with open("link.txt", "r") as f:

    for i in  sidebar_items:

        # open sidebar
        pyautogui.click(win_x + 41, win_y + 62)  # hamburger
        time.sleep(0.2)  # wait for sidebar to open
        print("hamburger")

        print('runnning sidebar scan')
        result = sidebar_scan(i)

        if result:

            success_count = 0
            print("successful dms on", i, 'are', success_count)
            time.sleep(0.2)

            f_iter = iter(f)
            while success_count != 2:
                time.sleep(0.5)
                location = pyautogui.locateOnScreen('saved_msg.png', confidence=0.65)
                loc = True


                try:
                    line = next(f_iter)

                    if location:

                        pyautogui.click(location)

                    else:
                        loc = False
                        print("cudnt identify savedmsgs breaking while")
                        break

                    time.sleep(0.2)

                    # pyautogui.click(win_x + 700, win_y + 1400)

                    pyautogui.hotkey('ctrl', 'a')

                    pyautogui.press('backspace')

                    pyperclip.copy(str(line))  # copy to clipboard
                    print(line)
                    pyautogui.hotkey('ctrl', 'v')  # paste it
                    pyautogui.press('enter')

                    time.sleep(0.4)  # wait for number to appear after pressing enter
                    pyautogui.click(win_x + 680, win_y + 1080)  # clicking number
                    time.sleep(1)

                    # grab just the region where the text appears

                    while True:

                        key = keyboard.read_key()

                        if key == "esc":
                            break

                        text_region = ImageGrab.grab(bbox=(
                            win_x + 550,  # pushed right
                            win_y + 30,  # pushed up
                            win_x + 750,  # pushed right
                            win_y + 60  # pushed up
                        ))

                        #highlight_region(
                        #    win_x + 550,
                        #    win_y + 30,
                        #    750 - 550,
                        #    60 - 30
                        #)

                        # upscale
                        scale = 4
                        text_region = text_region.resize(
                            (text_region.width * scale, text_region.height * scale),
                            Image.LANCZOS
                        )

                        # grayscale + invert (if light text on dark bg) + threshold
                        gray = text_region.convert('L')
                        inverted = ImageOps.invert(gray)
                        binarized = inverted.point(lambda p: 255 if p > 128 else 0)

                        text = pytesseract.image_to_string(binarized, config='--psm 7').strip().lower()
                        print(repr(text))

                        #time.sleep(1)
                        text = pytesseract.image_to_string(text_region).strip().lower()
                        print(repr(text))
                        #time.sleep(0.9)

                        # string manipulation, since typewrite on works in ascii so had to copy paste emojis
                        msg_string = str(text).split(' ')[0].capitalize()
                        #msg_string = (msg_string + "?")
                        msg_string = msg_string + f"?"
                        print(msg_string)
                        #time.sleep(0.5)



                        pyautogui.typewrite(msg_string, interval=0.01)

                        while True:
                            key = keyboard.read_key()
                            if key == 'enter':
                                time.sleep(0.5)
                                success_count += 1
                                print("success count : ", success_count)
                                break

                            elif key == 'esc':
                                print("skipped, success count unchanged:", success_count)
                                break

                        break

                    # pyautogui.press('enter')

                    time.sleep(0.4)




                except StopIteration:
                    print("No more lines")
                print("done with", i)

            if loc == False:
                print("cudnt identify savedmsgs breaking FOR too")
                break
            time.sleep(1.3)




        if result == False:
            break


endtime = time.time()
print("time taken for the code: ", endtime - start_time)





