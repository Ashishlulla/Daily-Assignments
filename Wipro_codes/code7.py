
a = input()
new_string = ""
vowels = "AEIOUaeiou"
lower_vowels = ["a", "e", "i", "o", "u"]
upper_vowels = ["A", "E", "I", "O", "U"]
for i in a:
    if i in vowels:
        if i.islower():
            if i == "u":
                new_string+="a"
            else:
                index_i = lower_vowels.index(i)
                new_string+=lower_vowels[index_i+1]
        else:
            if i == "U":
                new_string+="A"
            else:
                index_i = lower_vowels.index(i)
                new_string+=lower_vowels[index_i+1]
    else:
        new_string+=i

print(new_string)
        
        

