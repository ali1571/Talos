import pyautogui, time
import pygetwindow as gw

print(gw.getAllTitles())

win = gw.getWindowsWithTitle('QWERTS1571')[0]
win_x = win.left
win_y = win.top
win.activate()

print(f"Window origin: {win_x}, {win_y}")

print("Move mouse to TOP-LEFT of sidebar region...")
time.sleep(3)
pos = pyautogui.position()
print(f"Absolute: {pos}")
print(f"Offset: {pos.x - win_x}, {pos.y - win_y}")


print("Move mouse to TOP-RIGHT of sidebar region...")
time.sleep(3)
pos = pyautogui.position()
print(f"Absolute: {pos}")
print(f"Offset: {pos.x - win_x}, {pos.y - win_y}")

print("Move mouse to BOTTOM-LEFT of sidebar region...")
time.sleep(3)
pos = pyautogui.position()
print(f"Absolute: {pos}")
print(f"Offset: {pos.x - win_x}, {pos.y - win_y}")


print("Move mouse to BOTTOM-RIGHT of sidebar region...")
time.sleep(3)
pos = pyautogui.position()
print(f"Absolute: {pos}")
print(f"Offset: {pos.x - win_x}, {pos.y - win_y}")



# 267, 369
