'''
# Write a function to determine if two words are anagrams of each other.
'''
def is_anagram(str1, str2):
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())

    return str1 == str2

print(is_anagram('Creative', 'Reactive') == True)
print(is_anagram("foefet", "toffee") == True)
print(is_anagram("Buckethead", "DeathCubeK") == True)
print(is_anagram("Twoo", "WooT") == True)
print(is_anagram("dumble", "bumble") == False)
