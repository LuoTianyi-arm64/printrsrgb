'''
import sys, os
sys.path.insert(0, os.path.abspath("src"))
from printrsrgb import printrgb
foreground_color = [102, 204, 255]
background_color = (255, 211, 250)
text = '天依最可爱了'
printrgb(text, foreground_color=foreground_color, background_color=background_color)
'''
import shutil
import core
def get_terminal_width() -> None:
    return shutil.get_terminal_size().columns
print("Terminal width(py):", get_terminal_width())
print("Terminal width(rs):", core.GetTerminalWidth())
import core
import time,sys
import printrsrgb
def main() -> None:
    argv = sys.argv
    ask  = ''
    if argv:
        pass
    if not sys.stdin.isatty():
        printrsrgb(sys.stdin.buffer.read().decode('utf-8'), rainbow = True,get_color = core.GetDefaultColor)

if __name__ == "__main__":
    main()
