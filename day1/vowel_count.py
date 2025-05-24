def vowel_count(word):
    word = word.lower()
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    total_vowel = 0
    vowel_occurance = {}


    for i in word:
        if i in vowel_set:
            total_vowel += 1
            if i in vowel_occurance:
                vowel_occurance[i] += 1
            else:
                vowel_occurance[i] = 1

    return total_vowel, vowel_occurance

print(vowel_count('python'))

    
