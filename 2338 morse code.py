t = int(input())
morse_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-': 'ä', '.--.-': 'å', '----': 'Ch', '..-..': 'é', '--.--': 'ñ', '---.': 'ö', '..--': 'ü'}

def translate_morse(code):
    code = code.replace('===', '-')
    code = code.replace('=', '*')
    code = code.replace('.....', ' ')
    code = code.replace('...', ',')
    code = code.replace('.', '')
    code = code.replace('*', '.')
    return code

for _ in range(t):
    code = translate_morse(input())
    msg = []
    for c in code.split(','):
        if ' ' in c:
            submsg = []
            for i in c.split():
                submsg.append(morse_code[i])
            msg.append(' '.join(submsg))
        else:
            msg.append(morse_code[c])
    print(''.join(msg).lower())
