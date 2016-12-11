import time
import RPi.GPIO as IO

# IO.setwarnings(False)
IO.setmode(IO.BCM)

HexDigits = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d,
             0x07, 0x7f, 0x6f, 0x77, 0x7c, 0x39, 0x5e, 0x79, 0x71]

ADDR_AUTO = 0x40
ADDR_FIXED = 0x44
STARTADDR = 0xC0
BRIGHT_DARKEST = 0
BRIGHT_TYPICAL = 2
BRIGHT_HIGHEST = 7


class TM1637:
    __doublePoint = False
    __Clkpin = 0
    __Datapin = 0
    __brightness = BRIGHT_TYPICAL
    __currentData = [0, 0, 0, 0]

    def __init__(self, pinClock, pinData, brightness):
        self.__Clkpin = pinClock
        self.__Datapin = pinData
        self.__brightness = brightness
        IO.setup(self.__Clkpin, IO.OUT)
        IO.setup(self.__Datapin, IO.OUT)

    def Clear(self):
        b = self.__brightness
        point = self.__doublePoint
        self.__brightness = 0
        self.__doublePoint = False
        data = [0x7F, 0x7F, 0x7F, 0x7F]
        self.Show(data)
        # Restore previous settings:
        self.__brightness = b
        self.__doublePoint = point

    def ShowInt(self, i):
        s = str(i)
        self.Clear()
        for i in range(0, len(s)):
            self.Show1(i, int(s[i]))

    def Show(self, data):
        """Update all four digits"""
        for i in range(0, 4):
            self.__currentData[i] = data[i]

        self.start()
        self.writeByte(ADDR_AUTO)
        self.br()
        self.writeByte(STARTADDR)
        for i in range(0, 4):
            self.writeByte(self.coding(data[i]))
            self.br()
        self.writeByte(0x88 + self.__brightness)
        self.stop()

    def Show1(self, DigitNumber, data):
        """Update one digit of display (i.e. 0-3)"""
        if(DigitNumber < 0 or DigitNumber > 3):
            return  # error

        self.__currentData[DigitNumber] = data

        self.start()
        self.writeByte(ADDR_FIXED)
        self.br()
        self.writeByte(STARTADDR | DigitNumber)
        self.writeByte(self.coding(data))
        self.br()
        self.writeByte(0x88 + self.__brightness)
        self.stop()

    def Setbrightness(self, brightness):
        """brightness 0...7"""
        if(brightness > 7):
            brightness = 7
        elif(brightness < 0):
            brightness = 0

        if(self.__brightness != brightness):
            self.__brightness = brightness
            self.Show(self.__currentData)

    def ShowDoublepoint(self, on):
        """Show or hide double point divider"""
        if(self.__doublePoint != on):
            self.__doublePoint = on
            self.Show(self.__currentData)

    def writeByte(self, data):
        for i in range(0, 8):
            IO.output(self.__Clkpin, IO.LOW)
            if(data & 0x01):
                IO.output(self.__Datapin, IO.HIGH)
            else:
                IO.output(self.__Datapin, IO.LOW)
            data = data >> 1
            IO.output(self.__Clkpin, IO.HIGH)

        # wait for ACK
        IO.output(self.__Clkpin, IO.LOW)
        IO.output(self.__Datapin, IO.HIGH)
        IO.output(self.__Clkpin, IO.HIGH)
        IO.setup(self.__Datapin, IO.IN)

        while(IO.input(self.__Datapin)):
            time.sleep(0.001)
            if(IO.input(self.__Datapin)):
                IO.setup(self.__Datapin, IO.OUT)
                IO.output(self.__Datapin, IO.LOW)
                IO.setup(self.__Datapin, IO.IN)
        IO.setup(self.__Datapin, IO.OUT)

    def start(self):
        """send start signal to TM1637"""
        IO.output(self.__Clkpin, IO.HIGH)
        IO.output(self.__Datapin, IO.HIGH)
        IO.output(self.__Datapin, IO.LOW)
        IO.output(self.__Clkpin, IO.LOW)

    def stop(self):
        IO.output(self.__Clkpin, IO.LOW)
        IO.output(self.__Datapin, IO.LOW)
        IO.output(self.__Clkpin, IO.HIGH)
        IO.output(self.__Datapin, IO.HIGH)

    def br(self):
        """terse break"""
        self.stop()
        self.start()

    def coding(self, data):
        if(self.__doublePoint):
            pointData = 0x80
        else:
            pointData = 0

        if(data == 0x7F):
            data = 0
        else:
            data = HexDigits[data] + pointData
        return data


if __name__ == "main":
    Display = TM1637(23, 24, BRIGHT_IO.HIGHEST)

    Display.Clear()

    anzeige = [8, 8, 8, 8]
    Display.Show(anzeige)
    print "8888  - Taste bitte"
    scrap = raw_input()

    anzeige = [1, 2, 3, 4]
    Display.Show(anzeige)
    print "1234  - Taste bitte"
    scrap = raw_input()

    Display.Show1(1, 5)
    Display.Show1(2, 4)

    print "1544  - Taste bitte"
    scrap = raw_input()

    Display.Show1(0, 1)
    Display.Show1(3, 0)

    print "1540  - Taste bitte"
    scrap = raw_input()

    Display.ShowDoublepoint(True)
    Display.Setbrightness(4)

    print "15:40  heller - Taste bitte"
    scrap = raw_input()

    Display.Clear()

    print "Display abgeschaltet"
