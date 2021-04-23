import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(direction, text, shift):
  result = []
  new_position = 0

  if(direction=="encode"): #move upward
    for char in text:
      if char not in alphabet:
        result.append(char)

      else:

        position = alphabet.index(char) + shift
        if(position>len(alphabet)-1):
          new_position = position - len(alphabet)
          while(new_position>len(alphabet)-1):
            new_position -= len(alphabet)
          result.append(alphabet[new_position])
        else:
          result.append(alphabet[position])

  elif(direction == "decode"): #move downward
    for char in text:
      if char not in alphabet:
        result.append(char)

      else:

        position = alphabet.index(char) - shift
        if(position<0):
          new_position = position + len(alphabet)
          while new_position<0:
            new_position += len(alphabet)
          result.append(alphabet[new_position])
        else:
          result.append(alphabet[position])

  print(f"The {direction}d text is {''.join(result)}")

while True:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
      
  ceaser(direction, text, shift)

  again = input("\nWant to restart the Cipher Program? Say 'yes' if you want to try again or 'no' if you want to stop: ").lower()

  if(again) == "no":
    break
  elif(again) == "yes":
    continue