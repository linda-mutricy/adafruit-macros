# Adafruit MacroPad RP2040
This is custom code for an Adafruit MacroPad based off of the official tutorial. It should make your life easier as you program and do basic work tasks.

I made this for myself, so the keyboard shortcuts are pretty focused on commonly-used operations in Chrome, Slack, and Visual Studio Code, but you can easily modify it for whatever you need. 

## Source References for Keyboard Shortcuts
- [Slack](https://slack.com/help/articles/201374536-Slack-keyboard-shortcuts)
- [Chrome](https://support.google.com/chrome/answer/157179?hl=en&co=GENIE.Platform%3DDesktop)
- [Visual Studio Code](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

## Latest Enhancements
I needed a sleep mode, since the LEDs were so distracting. I cloned the Adafruit Sleep Mode code [in this repo](https://github.com/M-Eldin/Adafruit-MacroPad-RP2040-Sleep), which works as expected. 

To implement your own Sleep Mode, you'd need these files from `lib`: 

```
adafruit_displayio_sh1107_wrapper.py
autoscreen.py
```

You'd also need to modify the main `code.py` file. It should take only a few minutes. I wish I'd done this sooner!
