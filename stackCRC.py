

import crcmod.predefined
from binascii import unhexlify


s = unhexlify('070300130002')

crc16 = crcmod.predefined.Crc('modbus')
crc16.update(s)
print (crc16.hexdigest())