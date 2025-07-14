import board
import busio

#kmk stuff
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.scanners.keypad import MatrixScanner

# initializing the keyboard
keyboard = KMKKeyboard()

# macro setup
macros = Macros()
keyboard.modules.append(macros)


# pin setup
PINS = [board.GPIO26, board.GPIO27, board.GPIO28, board.GPIO29, board.GPIO4, board.GPIO5, board.GPIO0]


# display setup
bus = busio.I2C(board.GP_SCL, board.GP_SDA)
driver = SSD1306(i2c=bus, device_address=0x3C)

display = Display(
    display=driver,
    width=128,
    height=32,
    flip = False,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.8
)

# display action
display.entries = [
        TextEntry(text="Huii", x=64, y=16, x_anchor="M", y_anchor="M"),
]

keyboard.matrix = MatrixScanner(
    rows=(board.GPIO4, board.GPIO5,),
    cols=(board.GPIO26, board.GPIO27, board.GPIO28, board.GPIO29, board.GPIO0),
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.1, KC.2, KC.3,KC.4, KC.5,
     KC.6, KC.7, KC.8, KC.9, KC.0]
]
   

# starting kmk
if __name__ == '__main__':
    keyboard.go()