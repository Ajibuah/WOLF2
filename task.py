import random


word_list = ["Abjure","Future","Picnic","Airline","Gigantic","Publish","Bandit","Goofy","Banquet",
"Recount","Binoculars","Grandnieces","Redoubtable","Bible","Book","Ruler","Higher","Builder","Prison","Computer",
"Lucky","Charger","Numbers","Keys","Bottle","Connection","Comb","Nest","Panic""Heat","Luxury","Pareidolia","Government",
"Riposte","Sanctimony","Cacophony","Betrayal","Bully","Celibate","Cliche","Cooniac","Disappear",
"Disposition","Demons","Acronym","Ambiguity","Analogy","Abjure","Picnic","Board"," Indulge","Ring", "Bookworm",
"Inflatable","Sales" ,"Clerk", "Future","Butter", "Scotch","Inimical","Snap","Camera","Interim","Shell","fish","Trace",
"Analyze", "Infer"," Evaluate"," Formulate", "Describe", "Support","Explain","Summarize", "Compare", "Contrast",
"Predict","Acquiesce","Acronym","Ambiguity","Analogy","Andragogy""Antithesis","Antonym","Articulate","Assonance",
"Benchmarking","Brainstorming","Circumspect","Cognition""Collaborate","Correlation","Cumulative""Curriculum",
"Development""Dialect","Diction","Didactic","Divergent","Eloquence","Emergent","Empathy","Enigma","Epitome"]

random_index = random.randint(0, len(word_list) - 1)
random_word = word_list[random_index]
hidden_word = random_word[0] + '*' * (len(random_word) - 2) + random_word[-1]
guessed_correctly = False
while not guessed_correctly:
    print("Guess the word:", hidden_word)
    guess = input("Enter a letter or the full word guess: ").lower()
    if guess == random_word:
        guessed_correctly = True
        hidden_word_list = list(hidden_word)
        for i in range(1, len(random_word) - 1):
            if random_word[i] == guess:
                hidden_word_list[i] = guess
        hidden_word = ''.join(hidden_word_list)

        if hidden_word == random_word:
            guessed_correctly = True
print("Congratulations! You guessed the word:", random_word)


