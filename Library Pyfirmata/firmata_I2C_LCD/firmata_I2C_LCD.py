from pydoc import text
from pyfirmata import Arduino, util, STRING_DATA
board = Arduino('COM7')
board.send_sysex( STRING_DATA, util.str_to_two_byte_iter('Hallo, ini berhasil!') )

def msg( text ):
    if text:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( text ) )
        print("berhasil")
print("selesai")
