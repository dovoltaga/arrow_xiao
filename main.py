import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

class ArrowKeyboard:

    def __init__(self, rows_, cols_, keymaps_):
        self.LED_ON = False
        self.LED_OFF = True

        self.kbd = Keyboard(usb_hid.devices)
        self.rows = self.set_rows(rows_)
        self.cols = self.set_cols(cols_)
        self.keymaps = keymaps_

        self.led = DigitalInOut(board.D13)
        self.led.direction = Direction.OUTPUT

    def set_rows(self, row_pins):
        rows = []
        for row_pin in row_pins:
            row = DigitalInOut(row_pin)
            row.direction = Direction.OUTPUT
            row.value = False
            rows.append(row)
        return rows

    def set_cols(self, col_pins):
        cols = []
        for col_pin in col_pins:
            col = DigitalInOut(col_pin)
            col.direction = Direction.INPUT
            col.pull = Pull.UP
            cols.append(col)
        return cols

    def scan_matrix(self):
        aiKeyOn = []
        for idxRow, row in enumerate(self.rows):
            row.value = True
            for idxCol, col in enumerate(self.cols):
                if not col.value:
                    ary = [idxRow, idxCol]
                    aiKeyOn.append(ary)
            row.value = False
        return aiKeyOn

    def autoUDRL ( self ):
        self.led.value = self.LED_ON
        bLoop = True
        while bLoop:
            self.kbd.send(Keycode.UP_ARROW)
            time.sleep(1)
            self.led.value = self.LED_OFF
            self.kbd.send(Keycode.DOWN_ARROW)
            time.sleep(1)
            self.led.value = self.LED_ON

            self.kbd.send(Keycode.DOWN_ARROW)
            time.sleep(1)
            self.led.value = self.LED_OFF
            self.kbd.send(Keycode.UP_ARROW)
            time.sleep(1)
            self.led.value = self.LED_ON

            self.kbd.send(Keycode.LEFT_ARROW)
            time.sleep(1)
            self.led.value = self.LED_OFF
            self.kbd.send(Keycode.RIGHT_ARROW)
            time.sleep(1)
            self.led.value = self.LED_ON

            self.kbd.send(Keycode.RIGHT_ARROW)
            time.sleep(1)
            self.led.value = self.LED_OFF
            self.kbd.send(Keycode.LEFT_ARROW)
            time.sleep(1)
            self.led.value = self.LED_ON

            aiKeyOn = self.scan_matrix()
            if len(aiKeyOn)==0:
                time.sleep(12)
            else:
                bLoop = False
                self.led.value = self.LED_OFF
        return

    def main_loop(self):
        self.led.value = self.LED_OFF
        while True:
            aiKeyOn = self.scan_matrix()
            if len(aiKeyOn) == 3:
                self.autoUDRL()
            elif len(aiKeyOn) > 0:
                for ary in aiKeyOn:
                    self.kbd.send(self.keymaps[ary[0]][ary[1]])
                    self.led.value = self.LED_ON
                    time.sleep(0.1)
            else:
                self.led.value = self.LED_OFF
            #time.sleep(0.05)


row_pins = [board.D2, board.D3]
col_pins = [board.D4, board.D5, board.D6]

keymap = [
    [ Keycode.A,          Keycode.UP_ARROW,   Keycode.B           ],
    [ Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW ],
]

if __name__ == '__main__':
    print('hello arrow')
    kbd = ArrowKeyboard(row_pins, col_pins, keymap)
    kbd.main_loop()

