import serial
ser = serial.Serial('/dev/ttyACM1', 9600)
cmd = 0
while True:
    command = input("Type something..: (Servo Angle 0~180)");
    if command =="bye":
        print("See You!...")
        break
    else:
#         if 0 <= int(command) <= 180 :
        cmd = int(command)
        ser.write(str(command).encode())
    print(ser.readline())
    
ser.close()