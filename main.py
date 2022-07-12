import pyvisa
import time
import ctypes  # An included library with Python install.  

MB = ctypes.windll.user32.MessageBoxW
#Open comunication
rm = pyvisa.ResourceManager()
inst = rm.open_resource('TCPIP::10.1.14.123')
print(inst.query("*IDN?"))

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
    print("URRA!")
    time.sleep(5)
else:
    MB(0, "END","Configure", 0)


R = MB(0, "Do you want to normalize the equipment?", "Normalize", 4)

if R == 6:
        inst.write("CALC:TPIL:NORM")
        MB(0, "Connect the type N cable! (OUTPUT to INPUT)","Normalize", 0)
        time.sleep(30)
