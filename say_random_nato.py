#!/usr/bin/env python3

"""
Script that speaks a random number of characters in nato alphabet.
Mainly used for training to understand a longer sequence of nato words.
Script tests the user if everything was understood correctly.

The script uses the Mac OSX 'say' command for text to speech translation.

MIT License

Author: Christof Dallermassl
"""

import os
import random
import argparse

nato = {
'a': 'Alfa',
'b': 'Bravo',
'c': 'Charlie',
'd': 'Delta',
'e': 'Echo',
'f': 'Foxtrot',
'g': 'Golf',
'h': 'Hotel',
'i': 'India',
'j': 'Juliett',
'k': 'Kilo',
'l': 'Lima',
'm': 'Mike',
'n': 'November',
'o': 'Oscar',
'p': 'Papa',
'q': 'Quebec',
'r': 'Romeo',
's': 'Sierra',
't': 'Tango',
'u': 'Uniform',
'v': 'Victor',
'w': 'Whiskey',
'x': 'X-ray',
'y': 'Yankee',
'z': 'Zulu',
'1': 'One',
'2': 'Two',
'3': 'Three',
'4': 'Four',
'5': 'Five',
'6': 'Six',
'7': 'Seven',
'8': 'Eight',
'9': 'Nine',
'0': 'Zero',
}

all_letters = ''.join(x for x in nato.keys())

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', dest='length', type=int, default=8, help='Length of word to be spoken')
parser.add_argument('-s', '--silence', dest='silence', type=int, default=0, help='Silence in milliseconds between words')
parser.add_argument('-n', '--notest', dest='test', action="store_false", default=True, help='Do not test the user for the spoken characters')
args = parser.parse_args()

def sayRandomNato(letters, length):
    word = ''
    words = ''
    for _ in range (length):
        letter = random.choice(letters)
        word = word + letter
        words = words + '[[slnc ' + str(args.silence) + ']]' + nato[letter]
    command = 'say ' + words
    os.system(command)
    return word
    

if __name__ == '__main__':
    word = sayRandomNato(all_letters, args.length)
    if args.test:
        input = input("Type word:")
        if word == input:
            print("correct: %s" % word)
        else:
            print('wrong! %s should be %s ' % (input, word))
    else:
        print("word was: %s" % word)
