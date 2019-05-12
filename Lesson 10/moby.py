punct = str.maketrans('-', ' ', '.,?!;:')
new_line = str.maketrans({' ': '\n'})
with open('moby.txt', 'r') as input_file, open('moby_clean.txt', 'w') as output_file:
    for line in input_file:
        low_line = line.lower()
        low_line = low_line.translate(punct)
        output_file.write(low_line.translate(new_line))
