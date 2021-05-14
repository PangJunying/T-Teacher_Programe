#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# words2morse

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

# dict of morse2words
dict2 = dict(zip(char_to_dots.values(),char_to_dots.keys()))

def encode():
  words = input("Input a sentence you want to endoce,NO PUNCTUATION:").strip().upper()
  for letter in words:
    if letter == ' ':
      print('/', end=' ')
    else:
      print(char_to_dots[letter], end=' ')
  print()

def decode():
  codes = input("Input Morse code you want to decode,ONLY MORSE CODE:").strip().split(" ")
  for sign in codes:
    if sign == '/':
      print(' ', end='')
    else:
      print(dict2[sign], end='')
  print()


if __name__ == '__main__':
  while 1:
    choice = input("Encode(Words to Morse codes) or Decode(Morse codes to Words).Plase input [0/1]")

    if choice == '0':
      encode()
    elif choice == '1':
      decode()
    else:
      break
