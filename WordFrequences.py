def word_frequency(sentence):
    # Initialize an empty dictionary to store word frequencies
    frequency = {}
    
    # Split the sentence into words
    words = sentence.split()
    
    # Count frequencies of each word
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

# Test the function
sentence = "the quick brown fox jumps over the lazy dog"
print(word_frequency(sentence))  
# Output should be {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}