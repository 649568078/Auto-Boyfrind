from PIL import Image
from ctypes import *
import win32gui
import win32con
import win32clipboard as w
import time

def send(name, msg):
    # 打开剪贴板
    w.OpenClipboard()
    # 清空剪贴板
    w.EmptyClipboard()
    # 设置剪贴板内容
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    # # 获取剪贴板内容
    # date = w.GetClipboardData()
    # 关闭剪贴板
    w.CloseClipboard()
    # 获取qq窗口句柄
    handle = win32gui.FindWindow(None, name)
    if handle == 0:
        print('未找到窗口！')
    # 显示窗口
    win32gui.ShowWindow(handle, win32con.SW_SHOWMINIMIZED)#附加
    win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)#附加
    win32gui.ShowWindow(handle, win32con.SW_SHOW)
    time.sleep(1)
    # 把剪切板内容粘贴到qq窗口
    win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
    time.sleep(1)
    # 按下后松开回车键，发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
  # 延缓进程

def sendImage(name,imgpath):
    im = Image.open(imgpath)
    im.save('1.bmp')
    aString = windll.user32.LoadImageW(0, r"1.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
    print(aString)
    if aString != 0:  ## 由于图片编码问题  图片载入失败的话  aString 就等于0
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_BITMAP, aString)
        # 关闭剪贴板
        w.CloseClipboard()
        # 获取qq窗口句柄
        handle = win32gui.FindWindow(None, name)
        if handle == 0:
            print('未找到窗口！')
        # 显示窗口
        win32gui.ShowWindow(handle, win32con.SW_SHOWMINIMIZED)#附加
        win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)#附加
        win32gui.ShowWindow(handle, win32con.SW_SHOW)
        time.sleep(1)
        # 把剪切板内容粘贴到qq窗口
        win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
        time.sleep(1)
        # 按下后松开回车键，发送消息
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
