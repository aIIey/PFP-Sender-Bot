# Open the file in read mode
with open('girl.txt', 'r') as file:
  # Read all the lines in the file
  lines = file.readlines()

# Ask the user for the word to replace 'girl' with
replacement_word = input("Pfp type? (girl, guy, banner, anime): ")

# Loop through all the lines in the file
for i, line in enumerate(lines):
  # Replace 'girl' with the user-specified word
  lines[i] = line.replace('girl', replacement_word)

# Open the file in write mode
with open('girl.txt', 'w') as file:
  # Write the modified lines back to the file
  file.writelines(lines)

print("Done!")
