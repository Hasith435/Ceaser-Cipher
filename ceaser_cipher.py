input_txt = input('Enter the statement to cipher:')
shift_number = int(input('Enter shift number:'))
letter_split_input = [str(x) for x in input_txt]

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
shifting_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters_taken_out = []
final_outcome = []

for i in range(shift_number):
    letters_taken_out.append(shifting_alphabet[i])

for x in letters_taken_out:
    shifting_alphabet.remove(x)

shifting_alphabet.extend(letters_taken_out)

for m in input_txt:
    if m in alphabet:
        letter_index = alphabet.index(m)
        cipher_letter = shifting_alphabet[letter_index]
        final_outcome.append(cipher_letter)
    
    else:
        continue

encrypted_message = "".join(final_outcome)

print(f"encrypted message: {encrypted_message}")