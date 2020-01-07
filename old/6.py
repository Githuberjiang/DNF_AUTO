# coding=utf-8
from ctypes import *
from ctypes import wintypes
import win32con

SetWindowsHookEx=windll.user32.SetWindowsHookExA
UnhookWindowsHookEx=windll.user32.UnhookWindowsHookEx
CallNextHookEx=windll.user32.CallNextHookEx
GetMessage=windll.user32.GetMessageA
GetModuleHandle=windll.kernel32.GetModuleHandleW
#保存键盘钩子函数句柄
keyboard_hd = None
#保存鼠标钩子函数句柄
mouse_hd = None


class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [
        ('vkCode',c_int),
        ('scanCode', c_int),
        ('flags', c_int),
        ('time', c_int),
        ('dwExtraInfo', c_uint),
        ('',c_void_p)
    ]


class POINT(Structure):
    _fields_ = [
        ('x',c_long),
        ('y',c_long)
    ]


class MSLLHOOKSTRUCT(Structure):
    _fields_ = [
        ('pt',POINT),
        ('hwnd',c_int),
        ('wHitTestCode',c_uint),
        ('dwExtraInfo',c_uint),
    ]


def wait_for_msg():
    msg = wintypes.MSG()
    GetMessage(msg, 0, 0, 0)


def keyboard_pro(nCode, wParam, lParam):
    """
    函数功能：键盘钩子函数，当有按键按下时此函数被回调
    """
    if nCode == win32con.HC_ACTION:
        KBDLLHOOKSTRUCT_p = POINTER(KBDLLHOOKSTRUCT)
        param=cast(lParam,KBDLLHOOKSTRUCT_p)
        print(param.contents.vkCode)
    return CallNextHookEx(keyboard_hd, nCode, wParam, lParam)


def start_keyboard_hook():
    """
    函数功能：启动键盘监听
    """
    HOOKPROTYPE = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    pointer = HOOKPROTYPE(keyboard_pro)
    keyboard_hd = SetWindowsHookEx(
        win32con.WH_KEYBOARD_LL,
        pointer,
        GetModuleHandle(None),
        0)
    wait_for_msg()


def stop_keyboard_hook():
    """
    函数功能：停止键盘监听
    """
    UnhookWindowsHookEx(keyboard_hd)


def mouse_pro(nCode, wParam, lParam):
    """
    函数功能：鼠标钩子函数，当有鼠标事件，此函数被回调
    """
    if nCode == win32con.HC_ACTION:
        MSLLHOOKSTRUCT_p = POINTER(MSLLHOOKSTRUCT)
        param=cast(lParam,MSLLHOOKSTRUCT_p)
        #鼠标左键点击
        if wParam == win32con.WM_LBUTTONDOWN:
            print("左键点击，坐标：x:%d,y:%d" % (param.contents.pt.x,param.contents.pt.y))
        elif wParam == win32con.WM_LBUTTONUP:
            print("左键抬起，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
        elif wParam == win32con.WM_MOUSEMOVE:
            print("鼠标移动，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
        elif wParam == win32con.WM_RBUTTONDOWN:
            print("右键点击，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
        elif wParam == win32con.WM_RBUTTONUP:
            print("右键抬起，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
    return CallNextHookEx(mouse_hd, nCode, wParam, lParam)


def start_mouse_hook():
    """
    函数功能：启动鼠标监听
    """
    HOOKPROTYPE = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    pointer = HOOKPROTYPE(mouse_pro)
    mouse_hd = SetWindowsHookEx(
        win32con.WH_MOUSE_LL,
        pointer,
        GetModuleHandle(None),
        0)
    wait_for_msg()


def stop_mouse_hook():
    """
    函数功能：停止鼠标监听
    """
    UnhookWindowsHookEx(mouse_hd)


import HookApi

if __name__== '__main__':
    HookApi.start_keyboard_hook()