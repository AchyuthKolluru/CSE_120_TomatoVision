import win32api
import win32con as con
import winnt as nt

PyHKEY = win32api.RegOpenKeyEx(con.HKEY_CURRENT_USER,'Control Panel\\Accessibility',0,0x20006) 
win32api.RegSetValueEx(PyHKEY, 'MessageDuration', 0, nt.REG_DWORD, 0x0000012c)
win32api.Beep(500, 3000)
