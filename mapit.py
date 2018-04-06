import webbrowser
import sys
import pyperclip

if(len(sys.argv)>1):
    add = ' '.join(sys.argv[1:])
else:
    add = pyperclip.paste()
webbrowser.open("https://www.google.com/maps/place/" + add)
