# # 这里不知道为什么匹配到对应按钮那么慢，因此暂时弃用。采用手动点击扫码的方式。
# confirm_submit = pyautogui.locateCenterOnScreen(
#     r'confirm_submit.png', grayscale=True)
# if confirm_submit is None:
#     pyautogui.alert(
#         text='无法找到确认添加按钮！请手动进行后续操作！', title='程序开始确认框', button='确定！')
# else:
#     pyautogui.click(confirm_submit)


# # 判断是否在正确的页面，当前逻辑存在问题，因此不建议使用！！
# tab = pyautogui.locateCenterOnScreen(
#     r'tab.png', grayscale=True)
# wrongtab = pyautogui.locateCenterOnScreen(
#     r'wrongtab.png', grayscale=True, region=(0, 0, 9999, 300))
# if tab is None:
#     if wrongtab is None:
#         pyautogui.alert(
#             text='无法确认当前是否在正确页面！已退出', title='程序开始确认框', button='确定！')
#         import sys
#         exit(0)
#     else:
#         pyautogui.click(wrongtab)
# else:
#     print('go')

# # 通过识别输入框的方式发现无法找到输入框，此方法弃用
# qquid = pyautogui.locateCenterOnScreen(
#     r'./screenshots/qquid.png', grayscale=True, region=(0,0, screenWidth, 1000))
# if qquid is None:
#     pyautogui.alert(
#         text='无法找到输入框！请手动进行后续操作！', title='程序开始确认框', button='确定！')
# else:
#     pyautogui.click(qquid)