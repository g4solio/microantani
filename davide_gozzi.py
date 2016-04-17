from microbit import *
code = {
        '-----': '0',  '.----': '1',  '..---': '',
        '...--': '3',  '....-': '4',  '.....': '5',
        '-....': '6',  '--...': '7',  '---..': '8',
        '----.': '9'
        }
            a=''

while(button_a.get_presses()+button_b.get_presses()<5):
    if(button_a.is_pressed()):
        a=a+'.'
    else(butto_b.is_pressed()):
        a=a+'-'


b=code[a]
display.scroll(b)
