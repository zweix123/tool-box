# 将微信全屏, 鼠标悬停在要删除的记录那里运行程序, 程序会运行到该点无消息可删除为止
import pyautogui as ag
import time


def clear_one(st):
    ag.moveTo(st)
    ag.click(button="right")
    time.sleep(0.5)  # 等待识别
    loc = ag.locateCenterOnScreen("tar_WeChat.png")
    if loc is None:
        return False
    ag.moveTo(loc)
    ag.click(button="left")  # 删除
    ag.moveTo(908, 559)  # 确认删除位置
    ag.click(button="left")  # 确认删除
    return True


def work_clear():
    st = ag.position()
    flag = clear_one(st)
    while flag:
        flag = clear_one(st)


if __name__ == "__main__":
    # print(ag.position())
    work_clear()
