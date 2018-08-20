# Runescape Controller support

This package is intended to provide support for the Dualshock 4 controller to play runescape

### Setup

This requires pygame and pyautoGUI.
If you're using a dualshock 4, set up ds4windows: http://ds4windows.com/

```sh
$ pip install Pygame
$ pip install pyautogui
$ python ds4rs.py
```
### Usage
Upon loading, move your cursor to the center of your minimap and press the options button. Then move it to the edge, and and press the button again.
Pressing the Share button and then any of the remappable buttons (front buttons and L1/R1) will set that button to the current cursor location.
R2 and L2 are left and right click (they are switched)

Oh also if you want to control the camera, you can do it directly in ds4windows, just set the right stick to control the arrow keys.

### other info

Feel free to Contribute your own additions to this code if you want. 
If Mod Mark comes to your house and takes your first born child, don't come crying back to me.