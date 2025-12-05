TEST = 'Ho-Hooo Ho-Hooo-Ho-Ho Ho-Ho-Ho-Hooo' # = ALV

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

MORSE_CODE_REVERSED = {value:key for key,value in MORSE_CODE.items()}

with open('knowit/2025/5/input.txt', 'r') as f:
    letters = f.readline().strip().split(' ')

decrypted = ''

for l in letters:
    code = ''.join(['.' if s == 'Ho' else '-' for s in l.split('-')])
    decrypted += MORSE_CODE_REVERSED[code]

print(decrypted)