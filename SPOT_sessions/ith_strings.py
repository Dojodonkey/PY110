# Given a string and an integer i, write a method that splits the string up into a sentence of strings,
#  where each string in the sentence contains a character of the argued string and every ith character after it:

def fragment(sentence, i):
    sentence = ''.join([char for char in sentence if char.isalpha()])
    result_list = []

    for j in range(0, len(sentence)):
        word = ''
        for k in range(j, len(sentence), i):
            word += sentence[k]
        result_list.append(word)

    return ' '.join(result_list)


print(fragment("mary had a little lamb", 3)) # == "mydila ahatem raltlb ydila hatem altlb dila atem ltlb ila tem tlb la em lb a m b")