

import crcmod
import crcmod.predefined



def main():
    crc16_modbus = crcmod.predefined.mkCrcFun('modbus')
    result = crc16_modbus((bytearray((49, 50, 51, 52, 53, 54, 55, 56, 57)))
    print({}.format(resulat))

if __name__ == "__main__": main()