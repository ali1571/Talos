import pyautogui, time

seconds = 5
print(f"Hover over your target. Capturing in {seconds} seconds...")
time.sleep(seconds)

x, y = pyautogui.position()
print(f"X: {x}, Y: {y}")