import pyvisa
import time
import ctypes  # An included library with Python install.  

MB = ctypes.windll.user32.MessageBoxW
#Open comunication
rm = pyvisa.ResourceManager()
inst = rm.open_resource('TCPIP::10.1.14.123')
print(inst.query("*IDN?"))

R = MB(0, "Você deseja confirgurar o equipamento?", "Configuração", 4)

if R == 6:
    MB(0, "Configurando","Setting", 0)
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
    print("URRA!")
    time.sleep(5)
else:
    MB(0, "FIM","Setting", 0)

