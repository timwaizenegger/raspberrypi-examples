# Benoetigte Module werden importiert und eingerichtet
import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
# Hier wird der Eingangs-Pin deklariert, an dem der Sensor angeschlossen ist. Zusaetzlich wird auch der PullUP Widerstand am Eingang aktiviert
LED_PIN = 24
GPIO.setup(LED_PIN, GPIO.OUT, initial= GPIO.LOW)
  
print "LED-Test [druecken Sie STRG+C, um den Test zu beenden]"
 
# Hauptprogrammschleife
try:
        while True:
                print("LED 4 Sekunden an")
                GPIO.output(LED_PIN,GPIO.HIGH) #LED wird eingeschaltet
                time.sleep(4) #Wartemodus fuer 4 Sekunden
                print("LED 2 Sekunden aus") 
                GPIO.output(LED_PIN,GPIO.LOW) #LED wird ausgeschaltet
                time.sleep(2) #Wartemodus fuer weitere zwei Sekunden, in denen die LED Dann ausgeschaltet ist
  
# Aufraeumarbeiten nachdem das Programm beendet wurde
except KeyboardInterrupt:
        GPIO.cleanup()
