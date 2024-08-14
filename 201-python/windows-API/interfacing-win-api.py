from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD, DWORD, HANDLE, BOOL

MessageBoxA=windll.user32.MessageBoxA
MessageBox.argtypes=(HWND,LPCSTR,LPCSTR,UNIT)
MessageBoxA.restype=INT
print(MessageBoxA)
