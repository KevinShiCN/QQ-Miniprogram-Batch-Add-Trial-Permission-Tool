import pyautogui
import time

# 定义屏幕宽度
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

# 提示框确定开始
confirm_message = pyautogui.alert(
    text='请确保已打开QQ小程序权限管理页面', title='程序开始确认框', button='确定！')
print(confirm_message)

pyautogui.click()
pyautogui.press('browserrefresh')
