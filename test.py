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
import sys, os
sys.path.insert(0, os.path.abspath("core"))
import core as core
def get_terminal_width() -> None:
    return shutil.get_terminal_size().columns
print("Terminal width(py):", get_terminal_width())
print("Terminal width(rs):", core.GetTerminalWidth())