import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP26,
    board.GP27,
    board.GP28,
)

keyboard.row_pins = (
    board.GP29,
    board.GP0,
    board.GP4,
)

keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.NO,
        KC.C,
        KC.D,
        KC.E,
        KC.F,
        KC.G,
        KC.H,
    ]
]

encoder = EncoderHandler()
encoder.pins = ((board.GP2, board.GP1, board.GP29),)

encoder.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]

keyboard.extensions.append(encoder)

rgb = RGB(
    pixel_pin=board.GP3,
    num_pixels=8,
    val_limit=50,
)

keyboard.extensions.append(rgb)

displayio.release_displays()

i2c = busio.I2C(board.GP7, board.GP6)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

splash = displayio.Group()
label_text = label.Label(terminalio.FONT, text="HACKPAD", color=0xFFFFFF)
label_text.x = 40
label_text.y = 16
splash.append(label_text)
display.show(splash)

if __name__ == "__main__":
    keyboard.go()
