from collections import Counter

def is_anagram(str1, str2):
    # Clean up the strings
    cleaned_str1 = str1.replace(" ", "").lower()
    cleaned_str2 = str2.replace(" ", "").lower()
    
    # Check if lengths are equal
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Use Counter to count frequency of characters
    counter1 = Counter(cleaned_str1)
    counter2 = Counter(cleaned_str2)
    
    # Compare counters
    if counter1 == counter2:
        return True
    else:
        return False

# Example usage:
word1 = "listen"
word2 = "silent"
print(f"Are '{word1}' and '{word2}' anagrams? {is_anagram(word1, word2)}")  # True

word3 = "triangle"
word4 = "integral"
print(f"Are '{word3}' and '{word4}' anagrams? {is_anagram(word3, word4)}")  # True

word5 = "hello"
word6 = "world"
print(f"Are '{word5}' and '{word6}' anagrams? {is_anagram(word5, word6)}")  # False
