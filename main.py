import pyautogui
import time

# 定义屏幕宽度
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

# 输入QQ号数据
qqinput = pyautogui.prompt(text='请输入用【空格】区分的QQ号 例：123 456 987 654',
                           title='请输入QQ号', default='')
print(qqinput)
# qqlist = [int(n) for n in qqinput.split()]
qqlist = qqinput.split()
print(qqlist)

# 提示框提醒确认QQ号
confirm_qqlist = pyautogui.confirm(
    text='请检查是否为预期QQ号码{}'.format(qqlist), title='请检查QQ号', buttons=['确定！', '取消'])
print(confirm_qqlist)

if confirm_qqlist in "确定！":
    # 提示框确定开始
    confirm_message = pyautogui.alert(
        text='请确保已打开QQ小程序权限管理页面', title='程序开始确认框', button='确定！')
    print(confirm_message)

    # 第一次激活输入框
    pyautogui.click(screenWidth / 2, screenHeight / 5.2)
    pyautogui.press('browserrefresh')
    time.sleep(1.5)

    # 循环填写QQ号
    for qqnum in list(qqlist):
        pyautogui.click(screenWidth / 2, screenHeight / 5.2)
        pyautogui.press('tab')
        pyautogui.write(qqnum, interval=0.01)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(0.6)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(0.2)

    # 勾选体验者权限并跳转至最后
    tiyan_clickbox = pyautogui.locateCenterOnScreen(
        r'tiyan_clickbox.png', grayscale=True)
    if tiyan_clickbox is None:
        pyautogui.alert(
            text='无法找到体验权限按钮！请手动进行后续操作！', title='错误：无法定位体验权限按钮', button='确定！')
    else:
        pyautogui.click(tiyan_clickbox)
        pyautogui.press('end')
        pyautogui.alert(
            text='已完成！请点击【确认添加】', title='成功结束！', button='辛苦了！接下来的路我自己走！')
# 用户手动取消
else:
    canceled = pyautogui.alert(
        text='取消执行！', title='执行已取消', button='确定')
    print(canceled)
