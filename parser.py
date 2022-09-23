import re
import sys

text = "Patient presents today with several issues. Number Nine number n"

'''
  Capitalizes a word
  Input: String
  Output: Capitalized string
'''
def s_capitalize(s):
  if s == None:
    return None
  if len(s) == 1:
    return s.capitalize()
  else:
    return ''.join([s[0].capitalize(), s[1:]])

'''
  Parses a text
  Input: .txt file
  Output: parsed string
'''

def parse(filename):

  f = open(filename, "r") # open the file
  text = f.read().strip() # read the text and remove unnecessary whitespace

  # This removes the newlines for formatting purposes
  # Can comment out if not needed
  text = ' '.join( list(filter(None, text.split('\n'))) ) 

  bullets = re.split(" number next ", text, flags=re.IGNORECASE)
  init_text = bullets[0].split(' ')

  # handy dictionary for matching numbers one to nine
  numbers = {"one":1, "two":2, "three":3, "four":4, "five":5,
             "six":6, "seven":7, "eight":8, "nine":9}

  bullet_number = None
  split_idx = None

  for i in range(len(init_text)):
    word = init_text[i]
    if re.match(init_text[i], 'number', re.IGNORECASE) and i != len(init_text) - 1:

      for number in numbers.keys():
        if re.match(init_text[i+1], number, re.IGNORECASE):
          bullet_number = numbers[number]
          split_idx = i
          break

    if split_idx:
      break

  # If we haven't splitted the first text, then we don't have any bullet points
  if not split_idx:
    return bullets[0]

  first_paragraph = ' '.join(init_text[:split_idx])

  # Prevent user error when saying 'number n' and not saying anything else 
  if len(init_text) > split_idx+2:
    init_text[split_idx+2] = s_capitalize(init_text[split_idx+2])
    first_bullet = str(bullet_number) + '. ' + ' '.join(init_text[split_idx+2:])
  else:
    first_bullet = str(bullet_number) + '. '

  final_text = '\n'.join([first_paragraph, first_bullet])
  
  # loop over rest of the bullets, finalizing the text
  for bullet in bullets[1:]:
    bullet_number += 1
    bullet = s_capitalize(bullet)
    final_text += ''.join(['\n', str(bullet_number), '. ', bullet])
  
  return final_text

def main(args):
  if len(args) < 2:
    print("Usage: python3 parser.py <filename to parse (in .txt format)>")
    return

  else:
    filename = args[1]
    try:
      print(parse(filename))
      return 1
    except IOError:
      print ("Error: File does not appear to exist.")
      return 0


if __name__ == '__main__':
  main(sys.argv)
  