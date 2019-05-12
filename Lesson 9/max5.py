def max_sequence(seq):
    for i in range(0, 16):
        five_sum = sum(seq[i:i+5])
        if i == 0 or five_sum > max_sum:
            max_sum = five_sum
            index = i
        five_sum = 0
    return seq[index:index+5]
# print(max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5]))
if __name__ == '__main__':
    import doctest
    doctest.testmod()
