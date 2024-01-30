def disemvowel_trolls(sentence: str) -> str:
    # just starting to remember
    vowels = "aeiouAEIOU"
    new_word = ""
    for i in range(len(sentence)):
        if sentence[i] not in vowels:
            new_word += sentence[i]

    return new_word


print(disemvowel_trolls("Delete all vowels!"))
