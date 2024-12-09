import RPi.GPIO as GPIO

GPIO.setwarnings(False)

in1 = 17
in2 = 27
en_a = 4

# use broadcom GPIO numbers instead of board pi numbs
GPIO.setmode(GPIO.BCM)

#setup output pins
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en_a, GPIO.OUT)

power_a = GPIO.PWM(en_a, 50)
power_a.start(25)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)

while(True):
    user_input = input()

    if user_input == 'w':
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)

    elif user_input == 's':
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
    
    elif user_input == 'e':
        GPIO.cleanup()
        print("GPIO clean up")
        break