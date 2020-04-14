
user_input = input("Please type a sentence, word or phrase. RULES: No Periods, No Numbers, and No Symbols. Whatcha got? ")

def alpha_repeat(word_or_phrase):
    for character in word_or_phrase:
        if character.isdigit():
            print("Please no numbers")
            return 
    for character in word_or_phrase:
        if not character.isalnum():
            if character != " ":
                print('Please no symbols')
                return 
    alphabet = ["a", "b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    string = word_or_phrase.lower()
    print(f"okay,here we go......")
    print(string)
    counter = 0
    while counter <26:
       newstr = string.replace(alphabet[counter], "")
       counter += 1
       if newstr != string:
            string = newstr
            print(newstr)
       





alpha_repeat(user_input)
