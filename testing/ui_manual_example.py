"""
A simple Tkinter example demonstrating colour change and state switching.
Only two buttons:
    toggle_status_btn - Turning ON or OFF the light bulb.
    change_colour_btn - Opens a window with a palette.
"""

import colorsys
import json
import time
from typing import NoReturn
from tkinter import Tk, Button, colorchooser
from tuya_bulb_control import Bulb

# "ebfc16d57ed374932cjqfk" #'ebe097c0407da32084kvtr'

bulb = Bulb(
    client_id="txejpdfda9iwmn5cg2es",
    secret_key="46d6072ffd724e0ba5ebeb5cc6b9dce9",
    device_id="ebe097c0407da32084kvtr",
    region_key="us",
)
# def change_colour() -> NoReturn:
# Get current HSV colour
current_colour = json.loads(bulb.current_value(
    "colour_data"))  # For Version 2 # new_colour_v2
print(current_colour)
# Conversion current HSV to RGB
current_colour = colorsys.hsv_to_rgb(
    h=current_colour["h"] / 360,
    s=current_colour["s"] / 1000,
    v=current_colour["v"] / 1000,
)
# Convert the current RGB to format 0-255
current_colour = tuple(map(lambda x: int(x * 255), current_colour))
print(current_colour)
# Get new RGB colour
# colorchooser.askcolor(color=current_colour)[0]

# "orange": [255, 127, 0], "yellow": [255, 200, 0], "green": [
rainbow = {"red": [0, 1000, 1000], }
#   0, 255, 0], "blue": [0, 0, 255], "indigo": [46, 43, 95], "violet": [139, 0, 255], "white": [255, 255, 255]}

for x in range(2):
    for i in rainbow:
        r = rainbow[i][0]
        g = rainbow[i][1]
        b = rainbow[i][2]
        time.sleep(2)
        print('    %s (%d,%d,%d)' % (i, r, g, b))
        new_colour = (r, g, b)
        # print(new_colour)
        # Convert RGB coordinates to int
        new_colour = tuple(map(lambda x: int(x), new_colour))
        print(new_colour)
        # Set colour ✨
        # For Version 2 # set_colour_v2(new_color)
        bulb.set_colour(new_colour)

"""def toggle_status(button) -> NoReturn:
    # Turn ON or OFF
    bulb.set_toggle()

    # Change button text
    button["text"] = "ON" if button["text"] == "OFF" else "OFF"


def init_ui() -> NoReturn:
    # Switch button
    toggle_status_btn = Button(
        text="ON"
        if not bulb.current_value("switch_led")
        else "OFF",  # Text depends on state
        width=20,
        command=lambda: toggle_status(toggle_status_btn),
    )
    # Colour selection button
    change_colour_btn = Button(
        text="Change colour", width=20, command=change_colour)

    # Positioning the buttons
    toggle_status_btn.pack(side="left", padx=5, pady=5, ipady=6)
    change_colour_btn.pack(side="right", padx=5, pady=5, ipady=6)


if __name__ == "__main__":
    tk = Tk()
    tk.title("Colour change example")
    init_ui()
    tk.mainloop()"""

"""# Colortemp Test
        LOGGER.info('\nColortemp Control Test (Warm to Cool)')
        for level in range(11):
            LOGGER.info('    Level: %d%%' % (level*10))
            d.set_colourtemp_percentage(level*10)
            time.sleep(1)

        # Test by Flipping through colors of rainbow - set_colour(r, g, b):
        LOGGER.info('\nColor Test - Cycle through rainbow')
        rainbow = {"red": [255, 0, 0], "orange": [255, 127, 0], "yellow": [255, 200, 0], "green": [
            0, 255, 0], "blue": [0, 0, 255], "indigo": [46, 43, 95], "violet": [139, 0, 255]}
        for x in range(2):
            for i in rainbow:
                r = rainbow[i][0]
                g = rainbow[i][1]
                b = rainbow[i][2]
                LOGGER.info('    %s (%d,%d,%d)' % (i, r, g, b))
                d.set_colour(r, g, b)
                time.sleep(2)
            LOGGER.info('')

        # Random Color Test
        d.turn_on()
        LOGGER.info('\nRandom Color Test')
        for x in range(10):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            LOGGER.info('    RGB (%d,%d,%d)' % (r, g, b))
            d.set_colour(r, g, b)
            time.sleep(2)"""
