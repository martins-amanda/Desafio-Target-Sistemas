text = input("Digite uma string para inverter: ")

reverse_text = ''

for character in text:
    reverse_text = character + reverse_text

print(f"String invertida: {reverse_text}")