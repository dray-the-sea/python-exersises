"""
In all chaotic beauty lies a wounded work of art.
Beautiful but torn, wreaking havoc on my heart.
Camouflaged by insecurities, blinded by it all.
I love the way you sit there and barely notice me at all.

Source: https://www.familyfriendpoems.com/poems/other/short/

1. splice the string into sentences
2. find the first word of every sentence
3. find the last word of every sentence
4. find every word that starts with a "b" 

"""

poem = "In all chaotic beauty lies a wounded work of art. Beautiful but torn, wreaking havoc on my heart. Camouflaged by insecurities, blinded by it all. I love the way you sit there and barely notice me at all."

# 1 https://www.w3schools.com/python/ref_string_split.asp
sentences = poem.split(". ")

print(sentences)

# 2 print first word in each sentence

print("\n FIRST WORDS ")
print(sentences[0].split(" ")[0])
print(sentences[1].split(" ")[0])
print(sentences[2].split(" ")[0])
print(sentences[3].split(" ")[0])

# 3 print last word in each sentence

print("\n LAST WORDS ")
print(sentences[0].split(" ")[-1])
print(sentences[1].split(" ")[-1])
print(sentences[2].split(" ")[-1])
print(sentences[3].split(" ")[-1])


# or, 2 and 3 with a loop
for sentence in sentences:
    print(f"in the sentence {sentence}..." )
    words = sentence.split(" ")
    print(f"  first word is {words[0]}")
    print(f"  last word word is {words[-1]}") 
