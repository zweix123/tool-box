import os
import time
import pyautogui

Time_wait = 10
ignore_list = ["訾经典题目", "Data-Structure-and-Sort"]


def export_classic():  # typora软件自动导出
    # 文件(E):(25, 35)
    pyautogui.moveTo(25, 35, duration=1)
    time.sleep(1)  # 等待平稳
    pyautogui.click(button='left')
    time.sleep(1)  # 等待弹出
    # 导出:(.., 580)
    pyautogui.moveTo(25, 580, duration=1)
    # html:(480,..)
    pyautogui.moveTo(480, 580, duration=1)
    # pdf:(.., 525)
    pyautogui.moveTo(480, 525, duration=1)
    time.sleep(1)  # 等待平稳
    pyautogui.click(button='left')
    #保存:(620, 660)
    time.sleep(Time_wait)
    # 这里不知道保存窗口弹出要多久，所以保留的时间多一点
    pyautogui.moveTo(623, 643, duration=1)
    pyautogui.click(button='left')
    # 导出需要时间，这里停留几秒
    time.sleep(Time_wait)


def export_integrated():
    pass


def check_is_ignore(file_name):
    global ignore_list
    for ignore in ignore_list:
        if ignore in file_name:
            return True
    return False


def export_from_typora(root=os.getcwd()):
    global ignore_list
    file_list = [  # get_file_list(., "md")
        os.path.join(pre, file_name)
        for pre, dirs, files in os.walk(root)
        for file_name in files
        if str(file_name).endswith(".md")
    ]
    ignore_list = ignore_list + [  # 对遍历的文件去掉后缀名的get_file_list(., "pdf")
        os.path.join(pre, file_name.split(".")[0])
        for pre, dirs, files in os.walk(root)
        for file_name in files
        if str(file_name).endswith(".pdf")
    ]
    for file in file_list:
        if check_is_ignore(file) is False:
            # 打开文件
            os.startfile(file)
            # 等待几秒它打开
            time.sleep(Time_wait)
            # 下面导出方式选择对应的外观
            export_classic()  # 开始导出
            # export_integrated()  # k
            # 热键关闭
            pyautogui.hotkey('altleft', 'f4')


if __name__ == '__main__':
    export_from_typora()
