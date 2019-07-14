import tkinter
from tkinter import *
import crcmod
import crcmod.predefined
from binascii import unhexlify

def set_text(entryLable, text):
    entryLable.delete(0,END)
    entryLable.insert(0,text)
    return

root = Tk()
root.title('Modbus CRC16')
#Label(text='How many squares? (ex: 4x4, 5x3)').pack(side=TOP,padx=10,pady=10)
Label(text='Please insert your data in Hex?',anchor=W).pack(side=TOP)

entry = Entry(root, width=50)
entry.pack(side=TOP)
Label(text='Result in Hex',anchor=W).pack(side=TOP)
result = Entry(root, width=50)
result.pack(side=TOP)


def onok():
    x = entry.get()
    #print(x)
    s = unhexlify(x)
    crc16 = crcmod.predefined.Crc('modbus')
    crc16.update(s)
    #print (crc16.hexdigest())
    set_text(result, crc16.hexdigest())


Button(root, text='Give me!', command=onok).pack(side=LEFT)
Button(root, text='CLOSE', command=root.destroy).pack(side= RIGHT)

root.mainloop()