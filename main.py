from turtle import goto
import pyvisa
import ctypes  # An included library with Python install.  

MB = ctypes.windll.user32.MessageBoxW
#Open comunication
rm = pyvisa.ResourceManager()
inst = rm.open_resource('TCPIP::10.1.14.123')
print(inst.query("*IDN?"))

R = MB(0, "Você deseja confirgurar o equipamento?", "Configuração", 1)

if R == 1:
    MB(0, "Configurando","Setting", 0)
else:
    MB(0, "FIM","Setting", 0)

#Config
inst.write("*RST")

inst.write(":INST:SEL SR")
inst.write(":CONF:TPIL")

inst.write("FREQ:STAR 10 MHz")
inst.write("FREQ:STOP 100 MHz")
inst.write("INIT:CONT ON")

inst.write("TPIL:AVER:COUN 10")

print("URRA")