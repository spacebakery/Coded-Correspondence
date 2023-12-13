# Caesar decoder funciton
def caesar_decode(message, offset):
  alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
  decoded_message = ""
  for char in message:
    if char not in alphabet:
      decoded_message += char
    else:
      index = alphabet.find(char)
      decoded_message += alphabet[index + offset]
  return decoded_message


# Caesar encoder funciton
def caesar_encode(message, offset):
  alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
  encoded_message = ""
  for char in message:
    if char not in alphabet:
      encoded_message += char
    else:
      index = alphabet.find(char)
      encoded_message += alphabet[index - offset]
  return encoded_message

