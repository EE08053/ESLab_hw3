from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
import struct
import binascii

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device",dev.addr)
        elif isNewData:
            print("Received new data from",dev.addr)

class MyDelegate(DefaultDelegate):
    def __init__(self, hndl):
        DefaultDelegate.__init__(self)
        self.hndl = hndl

    def handleNotification(self, cHandle, data):
        print("Notification received")
        if (cHandle==self.hndl):
            val = binascii.b2a_hex(data)
            val = binascii.unhexlify(val)
            val = struct.unpack('f', val)[0]
            print str(val)

def enable_notify(ch):
        setup_data = b"\x01\x00"
        notify_handle = ch.getHandle() + 1
        res = dev.writeCharacteristic(notify_handle, setup_data, withResponse=True)
        print(res)

def enable_indication(ch):
        setup_data = b"\x02\x00"
        indicate_handle = ch.getHandle() + 1
        res = dev.writeCharacteristic(indicate_handle, setup_data, withResponse=True)
        print(res)

    
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(20.0)
n = 0
flag = 0
for dev in devices:
    if not flag :
        print("%d:Device %s(%s), RSSI=%d dB" % (n,dev.addr,dev.addrType,dev.rssi))
        n+=1
        for(adtype,desc,value) in dev.getScanData():
            print(" %s = %s"%(desc,value))
            if (desc == "Complete Local Name" and value=="Blood Pressure"):
                flag = 1

number = input("Enter your device number: ")
print(devices[number].addr)

print("Connecting...")
dev = Peripheral(devices[number].addr,'random')

print("Services...")
for svc in dev.services:
    print(str(svc))

#handle 59 62 65
try:
    BPService = dev.getServiceByUUID(UUID(0x1810))
    
    print("\ncharacteristic list : ")
    for ch in BPService.getCharacteristics():
        print(str(ch))
        print("properties: "+ ch.propertiesToString())
       
    print("\ncharacteristic data : ")
    
    for ch in BPService.getCharacteristics():
        print(str(ch))

        if (ch.supportsRead()):
            print("READ: "+ ch.read())

        elif ("WRITE" in ch.propertiesToString()):
            print("start writing")
            res = ch.write(bytes("QAQ\n"), withResponse = True)
            print(res)

        elif ("NOTIFY" in ch.propertiesToString()):
            print("start notifying")
            enable_notify(ch)
            while True:
                if dev.waitForNotifications(1.0):
                    print("notification success")
                    break
                else:
                    print("no notification")

        elif ("INDICATE" in ch.propertiesToString()):
            print("start indicating")
            enable_indication(ch)
            while True:
                if dev.waitForNotifications(1.0):
                    print("indication success")
                    break
                else:
                    print("no indication")


finally:
    dev.disconnect
print("finish")