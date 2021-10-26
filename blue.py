from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
 
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device",dev.addr)
        elif isNewData:
            print("Received new data from",dev.addr)

# p = Peripheral("60:ab:67:dd:98:37", "public")
p = Peripheral("B4:FA:48:04:6C:E0", "public")
services = p.getServices()
for svc in services:
    print(str(svc))
    print('\n')

# scanner = Scanner().withDelegate(ScanDelegate())
# devices = scanner.scan(30.0)
# n = 0
# number = n
# for dev in devices:
#     if dev.addr == "60:ab:67:dd:98:37":
#         print("device found\n")
#         number = n
#         break
#     # print("%d:Device %s(%s), RSSI=%d dB" % (n,dev.addr,dev.addrType,dev.rssi))
#     n+=1
# p = Peripheral(devices[number].addr)
# for svc in p.services:
#     print(str(svc))

#     for(adtype,desc,value) in dev.getScanData():
#         print(" %s = %s"%(desc,value))
# number = input("Enter your device number: ")
# print("Device",number)
# print(devices[number].addr)
 
# print("Connecting...")
# dev = Peripheral(devices[number].addr,'random')
 
# print("Services...")
# for svc in dev.services:
#    print(str(svc))
#     print(str(svc))
 

 
# t   testService = dev.getServiceByUUID(UUID(0xfff0))
#     for ch in testService.getCharacteristics():
#         print(str(ch))
 
#     ch = dev.getCharacteristics(uuid=UUID(0xfff1))[0]
#     if(ch.supportsRead()):
#         print(ch.read())
 
# finally:

