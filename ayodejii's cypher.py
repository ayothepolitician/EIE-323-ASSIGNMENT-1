import string

plaintext= "ayodeji"
#input any text you want in the 'plaintext'
shift = 10
#input any number of shifts you want in the 'shift' for the ceasar cypher

shift %= 26

alphabet= string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plaintext.translate(table)

print("your plaintext was: ",plaintext)

print("so your ceasar cypher is: ",encrypted)
