import serial
import sys
ser = serial.Serial('/dev/ttyACM0', 9600)
cmd = 0
while True:
    command = input("Type something..: (on/ off / bye )");
    if command =="on":
        print("The LED is on...")
#         cmd = 1
#         ser.write(format(cmd, 'b').encode())
        ser.write(b'1')
    elif command =="off":
        print("The LED is off...")
#         cmd = 0
#         ser.write(format(cmd, 'b').encode())
        ser.write(b'0')
    elif command =="bye":
        print("See You!...")
        break
    else:
        print("Sorry..type another thing..!")
#         sys.stdin.flush()
    print(ser.readline())
    
ser.close()
