from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT

MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT)
MessageBoxA.restype = INT
result = MessageBoxA(None, b"Hello, World!", b"This is a message box", 0)

print(result)

