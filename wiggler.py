import kivy
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from plyer import filechooser

import pyautogui
import threading
import keyboard
import time                                               #to do when esc is pressed set button name again to start before break and clicking should be one continues click rather than 100 mini clicks

#prevent kivy from closing program when esc is pressed
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')

kivy.require('2.3.0')

class MyRoot(BoxLayout):
    """functions go here """

    def __init__(self):
        super(MyRoot, self).__init__()

    def wiggler(self):
        """
        Toggle mouse wiggle functionality. Moves mouse in small increments
        until stopped by ESC key (close swhole  program) or stop button press.
        """
        def wiggle_mouse():
            time.sleep(1)
            while not self.stop_thread:
                pyautogui.moveRel(50, 0, duration=0.5)
                pyautogui.moveRel(-50, 0, duration=0.5)
                pyautogui.click()
                pyautogui.moveRel(0, 50, duration=0.5)
                pyautogui.moveRel(0, -50, duration=0.5)
                time.sleep(0.1)
                if keyboard.is_pressed('esc'):
                    self.ids.wiggle_button.text = "Start Wiggler"
                    break

        if not hasattr(self, 'wiggling'):
            self.wiggling = False

        if not self.wiggling:
            self.ids.wiggle_button.text = "Stop Wiggler"
            self.stop_thread = False
            wiggle_thread = threading.Thread(target=wiggle_mouse)
            wiggle_thread.daemon = True
            wiggle_thread.start()
            self.wiggling = True
        else:
            self.ids.wiggle_button.text = "Start Wiggler"
            self.stop_thread = True
            self.wiggling = False

    def auto_click(self):
        """
        Toggle auto click functionality. Performs left mouse clicks
        until stopped by ESC key (close whole program) or stop button press.
        """
        def click_mouse():
            time.sleep(1)
            while not self.stop_thread:
                pyautogui.click()
                time.sleep(0.1)
                if keyboard.is_pressed('esc'):
                    self.ids.auto_click_button.text = "Start Clicking"
                    break

        if not hasattr(self, 'clicking'):
            self.clicking = False

        if not self.clicking:
            self.ids.auto_click_button.text = "Stop Clicking"
            self.stop_thread = False
            click_thread = threading.Thread(target=click_mouse)
            click_thread.daemon = True
            click_thread.start()
            self.clicking = True
        else:
            self.ids.auto_click_button.text = "Start Clicking"
            self.stop_thread = True
            self.clicking = False

    def hold_click(self):

        def hold_mouse():
            time.sleep(1)
            while not self.stop_thread:
                pyautogui.mouseDown()
                if keyboard.is_pressed('esc'):
                    pyautogui.mouseUp()
                    self.ids.hold_click_button.text = "Hold Click"
                    break
            pyautogui.mouseUp()

        if not hasattr(self, 'holding'):
            self.holding = False

        if not self.holding:
            self.ids.hold_click_button.text = "Stop Holding"
            self.stop_thread = False
            hold_thread = threading.Thread(target=hold_mouse)
            hold_thread.daemon = True
            hold_thread.start()
            self.holding = True
        else:
            self.ids.hold_click_button.text = "Hold Click"
            self.stop_thread = True
            self.holding = False
            pyautogui.mouseUp()

class wiggle(App):
    """app gets build here"""
    def build(self):
        return MyRoot()

if __name__ == "__main__":
    rz_image  = wiggle()
    Window.size = (400, 240)
    rz_image.run()
