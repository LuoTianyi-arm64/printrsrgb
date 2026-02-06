import types
import random
from typing import Literal

import core

class printrsrgb:
    def __init__(self):
        self.angle = 0

    def __call__(
        self,
        *values: object,
        foreground_color: list | tuple | None = None,
        background_color: list | tuple | None = None,
        basic_color: dict | None = None,
        sep: str = " ",
        rainbow: bool = False,
        angle_mode: Literal["inner", "init", "random"] = "random",
        end: str = "\n",
        file: object | None = None,
        get_color: types.FunctionType | None = None,
        flush: Literal[False] = False,
        swap_fbc: bool = False,
    ) -> None:
        get_color = core.GetrDefaultColor if get_color is None else get_color
        if not rainbow:
            colored_text = ""
            if foreground_color or background_color:
                esc = []
                if foreground_color:
                    esc.append(f'38;2;{";".join(map(str, foreground_color))}')
                if background_color:
                    esc.append(f'48;2;{";".join(map(str, background_color))}')
                color_code = ";".join(esc)
                if swap_fbc:
                    colored_text = (
                        f"\033[7m\033[{color_code}m{sep.join(map(str, values))}\033[0m"
                    )
                else:
                    colored_text = (
                        f"\033[{color_code}m{sep.join(map(str, values))}\033[0m"
                    )
            elif basic_color:
                esc = []
                if "background_color" in basic_color:
                    if (
                        color.index(
                            basic_color.get("background_color", "black").lower()
                        )
                        < 8
                    ):
                        esc.append(
                            f'4{color.index(basic_color.get("background_color","black").lower())}'
                        )
                    else:
                        esc.append(
                            f'10{color.index(basic_color.get("background_color","black").lower()) - 8}'
                        )
                if "foreground_color" in basic_color:
                    if (
                        color.index(
                            basic_color.get("foreground_color", "white").lower()
                        )
                        < 8
                    ):
                        esc.append(
                            f'3{color.index(basic_color.get("foreground_color","white").lower())}'
                        )
                    else:
                        esc.append(
                            f'9{color.index(basic_color.get("foreground_color","white").lower()) - 8}'
                        )
                colored_text = (
                    f'\033[{";".join(esc)}m{sep.join(map(str, values))}\033[0m'
                )
            print(colored_text, sep=sep, end=end, file=file, flush=flush)
        else:
            if foreground_color or background_color:
                print(
                    "\033[38;2;255;0;0mError,You can't print with rainbow and other color angle_mode in the same time.\033[0m"
                )
            elif basic_color:
                print(
                    "\033[38;2;255;0;0mError,You can't print with rainbow and other basic color mode in the same time.\033[0m"
                )
            else:
                text = f"{sep.join(map(str, values))}"
                if angle_mode == "inner":
                    x, y, k = (0, 0, 0)
                    temp_string = ""
                    escapt_char_index = 0
                    escape_character = 1
                    for current_char in text:
                        escapt_char_index += 1
                        if current_char == "":
                            temp_string += current_char
                            k = 1
                        elif k == 1:
                            if current_char == "[":
                                temp_string += current_char
                                k = 2
                                try:
                                    if (
                                        text[escapt_char_index : escapt_char_index + 3]
                                        in [
                                            "30m",
                                            "31m",
                                            "32m",
                                            "33m",
                                            "34m",
                                            "35m",
                                            "36m",
                                            "37m",
                                            "90m",
                                            "91m",
                                            "92m",
                                            "93m",
                                            "94m",
                                            "95m",
                                            "96m",
                                            "97m",
                                            "40m",
                                            "41m",
                                            "42m",
                                            "43m",
                                            "44m",
                                            "45m",
                                            "46m",
                                            "47m",
                                        ]
                                    ) or (
                                        text[escapt_char_index : escapt_char_index + 4]
                                        in [
                                            "100m",
                                            "101m",
                                            "102m",
                                            "103m",
                                            "104m",
                                            "105m",
                                            "106m",
                                            "107m",
                                        ]
                                    ):
                                        escape_character = 0
                                    else:
                                        escape_character = 1
                                except:
                                    pass
                            else:
                                temp_string = current_char
                                x += 1
                                if x == core.GetTerminalWidth():
                                    x = 0
                                    y += 1
                                if escape_character:
                                    printrsrgb(
                                        current_char,
                                        foreground_color=get_color(
                                            self.angle + x * 5 + y * 7
                                        ),
                                        end="",
                                        file=file,
                                        swap_fbc=swap_fbc,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                                k = 0
                        elif k > 1:
                            if 64 <= ord(current_char) <= 126:
                                temp_string += current_char
                                if escape_character:
                                    printrsrgb(
                                        temp_string,
                                        foreground_color=get_color(
                                            self.angle + x * 5 + y * 7
                                        ),
                                        end="",
                                        file=file,
                                        swap_fbc=swap_fbc,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                                temp_string = ""
                                k = 0
                            else:
                                temp_string += current_char
                        elif current_char != "\n":
                            if current_char != " ":
                                if escape_character:
                                    printrsrgb(
                                        current_char,
                                        foreground_color=get_color(
                                            self.angle + x * 5 + y * 7
                                        ),
                                        end="",
                                        file=file,
                                        swap_fbc=swap_fbc,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                            else:
                                if escape_character:
                                    printrsrgb(
                                        current_char,
                                        foreground_color=get_color(
                                            self.angle + x * 5 + y * 7
                                        ),
                                        end="",
                                        file=file,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                            x += 1
                            if x == core.GetTerminalWidth():
                                x = 0
                                y += 1
                        else:
                            x = 1
                            y += 1
                            print("", file=file)
                    self.angle += y * 7 + 14
                elif angle_mode == "init":
                    x, y, k = (0, 0, 0)
                    temp_string = ""
                    escapt_char_index = 0
                    escape_character = 1
                    for current_char in text:
                        escapt_char_index += 1
                        if current_char == "":
                            temp_string += current_char
                            k = 1
                        elif k == 1:
                            if current_char == "[":
                                temp_string += current_char
                                k = 2
                                try:
                                    if (
                                        text[escapt_char_index : escapt_char_index + 3]
                                        in [
                                            "30m",
                                            "31m",
                                            "32m",
                                            "33m",
                                            "34m",
                                            "35m",
                                            "36m",
                                            "37m",
                                            "90m",
                                            "91m",
                                            "92m",
                                            "93m",
                                            "94m",
                                            "95m",
                                            "96m",
                                            "97m",
                                            "40m",
                                            "41m",
                                            "42m",
                                            "43m",
                                            "44m",
                                            "45m",
                                            "46m",
                                            "47m",
                                        ]
                                    ) or (
                                        text[escapt_char_index : escapt_char_index + 4]
                                        in [
                                            "100m",
                                            "101m",
                                            "102m",
                                            "103m",
                                            "104m",
                                            "105m",
                                            "106m",
                                            "107m",
                                        ]
                                    ):
                                        escape_character = 0
                                    else:
                                        escape_character = 1
                                except:
                                    pass
                            else:
                                temp_string = current_char
                                x += 1
                                if x == core.GetTerminalWidth():
                                    x = 0
                                    y += 1
                                if escape_character:
                                    printrsrgb(
                                        current_char,
                                        foreground_color=get_color(x * 5 + y * 7),
                                        end="",
                                        file=file,
                                        swap_fbc=swap_fbc,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                                k = 0
                        elif k > 1:
                            if 64 <= ord(current_char) <= 126:
                                temp_string += current_char
                                if escape_character:
                                    printrsrgb(
                                        temp_string,
                                        foreground_color=get_color(x * 5 + y * 7),
                                        end="",
                                        file=file,
                                        swap_fbc=swap_fbc,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                                temp_string = ""
                                k = 0
                            else:
                                temp_string += current_char
                        elif current_char != "\n":
                            if current_char != " ":
                                if escape_character:
                                    printrsrgb(
                                        current_char,
                                        foreground_color=get_color(x * 5 + y * 7),
                                        end="",
                                        file=file,
                                        swap_fbc=swap_fbc,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                            else:
                                if escape_character:
                                    printrsrgb(
                                        current_char,
                                        foreground_color=get_color(x * 5 + y * 7),
                                        end="",
                                        file=file,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                            x += 1
                            if x == get_terminal_width():
                                x = 0
                                y += 1
                        else:
                            x = 1
                            y += 1
                            print("", file=file)
                    self.angle += y * 7 + 14
                else:
                    x, y, k = (0, 0, 0)
                    angle = random.randint(0, 359)
                    temp_string = ""
                    escapt_char_index = 0
                    escape_character = 1
                    for current_char in text:
                        escapt_char_index += 1
                        if current_char == "":
                            temp_string += current_char
                            k = 1
                        elif k == 1:
                            if current_char == "[":
                                temp_string += current_char
                                k = 2
                                try:
                                    if (
                                        text[escapt_char_index : escapt_char_index + 3]
                                        in [
                                            "30m",
                                            "31m",
                                            "32m",
                                            "33m",
                                            "34m",
                                            "35m",
                                            "36m",
                                            "37m",
                                            "90m",
                                            "91m",
                                            "92m",
                                            "93m",
                                            "94m",
                                            "95m",
                                            "96m",
                                            "97m",
                                            "40m",
                                            "41m",
                                            "42m",
                                            "43m",
                                            "44m",
                                            "45m",
                                            "46m",
                                            "47m",
                                        ]
                                    ) or (
                                        text[escapt_char_index : escapt_char_index + 4]
                                        in [
                                            "100m",
                                            "101m",
                                            "102m",
                                            "103m",
                                            "104m",
                                            "105m",
                                            "106m",
                                            "107m",
                                        ]
                                    ):
                                        escape_character = 0
                                    else:
                                        escape_character = 1
                                except:
                                    pass
                            else:
                                temp_string = current_char
                                x += 1
                                if x == get_terminal_width():
                                    x = 0
                                    y += 1
                                if escape_character:
                                    printrsrgb(
                                        current_char,
                                        foreground_color=get_color(
                                            angle + x * 5 + y * 7
                                        ),
                                        end="",
                                        file=file,
                                        swap_fbc=swap_fbc,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                                k = 0
                        elif k > 1:
                            if 64 <= ord(current_char) <= 126:
                                temp_string += current_char
                                if escape_character:
                                    printrsrgb(
                                        temp_string,
                                        foreground_color=get_color(
                                            angle + x * 5 + y * 7
                                        ),
                                        end="",
                                        file=file,
                                        swap_fbc=swap_fbc,
                                    )
                                else:
                                    print(temp_string, end="", file=file)
                                temp_string = ""
                                k = 0
                            else:
                                temp_string += current_char
                        elif current_char != "\n":
                            if current_char != " ":
                                if escape_character:
                                    printrsrgb(
                                        current_char,
                                        foreground_color=get_color(
                                            angle + x * 5 + y * 7
                                        ),
                                        end="",
                                        file=file,
                                        swap_fbc=swap_fbc,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                            else:
                                if escape_character:
                                    printrsrgb(
                                        current_char,
                                        foreground_color=get_color(
                                            angle + x * 5 + y * 7
                                        ),
                                        end="",
                                        file=file,
                                    )
                                else:
                                    print(current_char, end="", file=file)
                            x += 1
                            if x == get_terminal_width():
                                x = 0
                                y += 1
                        else:
                            x = 1
                            y += 1
                            print("", file=file)
                print(end, end="", file=file)


printrsrgb = printrsrgb()
