def enumerate(file1, file2):
    try:
        with open(file1, 'r') as input_file, open(file2, 'w') as output_file:
            num = 1
            for line in input_file:
                output_file.write(str(num))
                output_file.write(' ')
                output_file.write(line)
                num += 1
    except Exception as err:
        print(err)

