# AutoWieIsWie
Automatically searches the KULeuven wie-is-wie for matches with your clip-board contents.


# Requirements
This program is written in Python, so you'll need python. I only tested it with Python3, i don't know if it works with earlier versions.
This program relies on tkinter, so you will need to have that installed:
```bash
sudo apt-get install python3-tk
```

# How to use it
Just run `python3 wie-is-wie.py` and the program will start running. It will check your clipboard content with wie-is-wie and output it to the terminal. If you copy something new, so when your clipboard content changes, it will automatically look that up as well and output it to the terminal.

# Optimizations
When your clipboard contains something that has no space in it, like a normal name would have, it will search the wie-is-wie with first-name and last-name as the content of your clipboard. If you wonder why this is, you don't know everything about wie-is-wie there is to know.

When your clipboard contains spaces, it will search for every possible combination. E.g. Your clipboard contains **"Mark Jan Peeters"**, the wie-is-wie will be searched for: 
* Mark Jan
* Mark Peeters
* Jan Mark
* Jan Peeters
* Peeters Mark
* Peeters Jan
