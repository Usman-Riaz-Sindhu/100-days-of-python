def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_score = 0
    for letter in "true":
        true_score += combined_names.count(letter)

    love_score = 0
    for letter in "love":
        love_score += combined_names.count(letter)

    print(str(true_score) + str(love_score))


calculate_love_score("Kanye West", "Kim Kardashian")