import pyvisa
import time
import ctypes 

MB = ctypes.windll.user32.MessageBoxW

#Open comunication
rm = pyvisa.ResourceManager()
inst = rm.open_resource('TCPIP::10.1.14.123')
if inst == "":
    MB(0,"Equipment disconnected! Try again!", "Connection",0)
    
#verify the communication
idn = inst.query("*IDN?")
if idn.find('N1996A'):
    MB(0,"Equipment connected!", "Connection",0)
else:
    MB(0, "Equipment not found!","Connection", 0)

#Configure the equipment
R = MB(0, "Do you want to configure the equipment?", "Configure", 4)
if R == 6:
    MB(0, "Setting","Setting", 0)
    #Config
    inst.write("*RST")
    time.sleep(5)
    inst.write(":INST:SEL SR")
    inst.write(":CONF:TPIL")
    time.sleep(5)
    inst.write("FREQ:STAR 10 MHz")
    inst.write("FREQ:STOP 100 MHz")
    inst.write("INIT:CONT ON")
    time.sleep(5)
    inst.write("TPIL:AVER:COUN 10")
    inst.write(":DISP:TPIL:WIND:TRAC:Y:RLEV -20")
    print("CONFIGURED!")
    time.sleep(5)
else:
    MB(0, "END","Configure", 0)

#Nomarlize the equpment
R = MB(0, "Do you want to normalize the equipment?", "Normalize", 4)

if R == 6:
        MB(0, "Connect the type N cable! (OUTPUT to INPUT)","Normalize", 0)
        inst.write("CALC:TPIL:NORM")
        inst.write(":INIT:CONT ON")
        MB(0, "PRESS==> LOCAL<FREQ<NORMALIZE<CONTINUE","Normalize", 0)
        MB(0, "Check the normalize!","Normalize", 0)
        time.sleep(30)
        print("NORMALIZED!")

#colect measure

R = MB(0, "Do you want to measuring now?", "Measuring", 4)

if R == 6:
        MB(0, "Connect the equipment under test! (OUTPUT to INPUT)","Measuring", 0)
        M = inst.query(":CALC:DATA?")
        M = M.split(",")
        print(float(M[1]))