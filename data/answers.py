# Assign domains to answers (example, to be updated)
# Explicitly assign domains for each answer
answer_domains = {
    # Question 1
    (1, 1): [
        "Air",
        "Water",
        "Weather",
    ],  # Answer 1 of question 1 -> Air, Water, Weather
    (1, 2): ["Animal"],  # Answer 2 of question 1 -> Animal
    (1, 3): ["Chaos"],  # Answer 3 of question 1 -> Chaos
    (1, 4): ["Death"],  # Answer 4 of question 1 -> Death
    (1, 5): ["Destruction"],  # Answer 5 of question 1 -> Destruction
    (1, 6): ["Earth"],  # Answer 6 of question 1 -> Earth
    (1, 7): ["Evil"],  # Answer 7 of question 1 -> Evil
    # Question 2
    (2, 1): ["Fire"],  # Answer 1 of question 2 -> Fire
    (2, 2): ["Good"],  # Answer 2 of question 2 -> Good
    (2, 3): ["Healing"],  # Answer 3 of question 2 -> Healing
    (2, 4): ["Knowledge"],  # Answer 4 of question 2 -> Knowledge
    (2, 5): ["Law"],  # Answer 5 of question 2 -> Law
    (2, 6): ["Luck"],  # Answer 6 of question 2 -> Luck
    (2, 7): ["Magic"],  # Answer 7 of question 2 -> Magic
    # Question 3
    (3, 1): ["Plant"],  # Answer 1 of question 3 -> Plant
    (3, 2): ["Protection"],  # Answer 2 of question 3 -> Protection
    (3, 3): ["Strength"],  # Answer 3 of question 3 -> Strength
    (3, 4): ["Sun"],  # Answer 4 of question 3 -> Sun
    (3, 5): ["Travel"],  # Answer 5 of question 3 -> Travel
    (3, 6): ["Trickery"],  # Answer 6 of question 3 -> Trickery
    (3, 7): ["War"],  # Answer 7 of question 3 -> War
    # Question 4
    (4, 1): ["Water", "Air", "Weather"],  # Question 4, Answer 1 -> Water, Air, Weather
    (4, 2): ["Celerity"],  # Question 4, Answer 2 -> Celerity
    (4, 3): ["Cold"],  # Question 4, Answer 3 -> Cold
    (4, 4): ["Community"],  # Question 4, Answer 4 -> Community
    (4, 5): ["Competition"],  # Question 4, Answer 5 -> Competition
    (4, 6): ["Creation"],  # Question 4, Answer 6 -> Creation
    (4, 7): ["Domination"],  # Question 4, Answer 7 -> Domination
    # Question 5
    (5, 1): ["Dream"],  # Question 5, Answer 1 -> Dream
    (5, 2): ["Force"],  # Question 5, Answer 2 -> Force
    (5, 3): ["Glory"],  # Question 5, Answer 3 -> Glory
    (5, 4): ["Inquisition"],  # Question 5, Answer 4 -> Inquisition
    (5, 5): ["Liberation"],  # Question 5, Answer 5 -> Liberation
    (5, 6): ["Madness"],  # Question 5, Answer 6 -> Madness
    (5, 7): ["Mind"],  # Question 5, Answer 7 -> Mind
    # Question 6
    (6, 1): ["Mysticism"],  # Question 6, Answer 1 -> Mysticism
    (6, 2): ["Oracle"],  # Question 6, Answer 2 -> Oracle
    (6, 3): ["Pact", "Domination"],  # Question 6, Answer 3 -> Pact, Domination
    (6, 4): ["Pestilence"],  # Question 6, Answer 4 -> Pestilence
    (6, 5): ["Purification"],  # Question 6, Answer 5 -> Purification
    (6, 6): ["Summoner"],  # Question 6, Answer 6 -> Summoner
    (6, 7): ["Weather", "Air", "Water"],  # Question 6, Answer 7 -> Weather, Air, Water
    # Add mappings for other questions
    # Question 7
    (7, 1): ["Air"],  # Question 7, Answer 1 -> Air
    (7, 2): ["Oracle", "Dream"],  # Question 7, Answer 2 -> Oracle, Dream
    (7, 3): ["Glory"],  # Question 7, Answer 3 -> Glory
    (7, 4): ["Community"],  # Question 7, Answer 4 -> Community
    (7, 5): ["Travel"],  # Question 7, Answer 5 -> Travel
    (7, 6): ["Luck", "Good"],  # Question 7, Answer 6 -> Luck, Good
    (7, 7): ["Magic"],  # Question 7, Answer 7 -> Magic
    # Question 8
    (8, 1): ["Fire"],  # Question 8, Answer 1 -> Fire
    (8, 2): ["Animal"],  # Question 8, Answer 2 -> Animal
    (8, 3): ["Pact", "Protection"],  # Question 8, Answer 3 -> Pact, Protection
    (8, 4): ["Inquisition"],  # Question 8, Answer 4 -> Inquisition
    (8, 5): ["Competition"],  # Question 8, Answer 5 -> Competition
    (8, 6): ["Trickery"],  # Question 8, Answer 6 -> Trickery
    (8, 7): ["War", "Mysticism"],  # Question 8, Answer 7 -> War, Mysticism
    # Question 9
    (9, 1): ["Plant"],  # Question 9, Answer 1 -> Plant
    (9, 2): ["Good", "Luck"],  # Question 9, Answer 2 -> Good, Luck
    (9, 3): ["Chaos", "Destruction"],  # Question 9, Answer 3 -> Chaos, Destruction
    (9, 4): ["Pestilence"],  # Question 9, Answer 4 -> Pestilence
    (9, 5): ["Liberation"],  # Question 9, Answer 5 -> Liberation
    (9, 6): ["Creation"],  # Question 9, Answer 6 -> Creation
    (9, 7): ["Domination"],  # Question 9, Answer 7 -> Domination
    # Question 10
    (10, 1): ["Water", "Weather"],  # Question 10, Answer 1 -> Water, Weather
    (10, 2): ["Protection", "Pact"],  # Question 10, Answer 2 -> Protection, Pact
    (10, 3): ["Healing"],  # Question 10, Answer 3 -> Healing
    (10, 4): ["Death"],  # Question 10, Answer 4 -> Death
    (10, 5): ["Purification"],  # Question 10, Answer 5 -> Purification
    (10, 6): ["Madness"],  # Question 10, Answer 6 -> Madness
    (10, 7): ["Mind", "Knowledge"],  # Question 10, Answer 7 -> Mind, Knowledge
    # Question 11
    (11, 1): ["Dream", "Oracle"],  # Question 11, Answer 1 -> Dream, Oracle
    (11, 2): ["Celerity"],  # Question 11, Answer 2 -> Celerity
    (11, 3): ["Strength"],  # Question 11, Answer 3 -> Strength
    (11, 4): ["Knowledge", "Mind"],  # Question 11, Answer 4 -> Knowledge, Mind
    (11, 5): ["Destruction", "Chaos"],  # Question 11, Answer 5 -> Destruction, Chaos
    (11, 6): ["Summoner"],  # Question 11, Answer 6 -> Summoner
    (11, 7): ["Weather", "Water"],  # Question 11, Answer 7 -> Weather, Water
    # Question 12
    (12, 1): ["Mysticism", "War"],  # Question 12, Answer 1 -> Mysticism, War
    (12, 2): ["Force"],  # Question 12, Answer 2 -> Force
    (12, 3): ["Cold"],  # Question 12, Answer 3 -> Cold
    (12, 4): ["Sun"],  # Question 12, Answer 4 -> Sun
    (12, 5): ["Law"],  # Question 12, Answer 5 -> Law
    (12, 6): ["Earth"],  # Question 12, Answer 6 -> Earth
    (12, 7): ["Evil"],  # Question 12, Answer 7 -> Evil
    # Question 13
    (13, 1): ["Air"],  # Question 13, Answer 1 -> Air
    (13, 2): ["Celerity"],  # Question 13, Answer 2 -> Celerity
    (13, 3): ["Chaos"],  # Question 13, Answer 3 -> Chaos
    (13, 4): [
        "Community",
        "Competition",
    ],  # Question 13, Answer 4 -> Community, Competition
    (13, 5): [
        "Destruction",
        "Pestilence",
    ],  # Question 13, Answer 5 -> Destruction, Pestilence
    (13, 6): ["Creation"],  # Question 13, Answer 6 -> Creation
    (13, 7): ["Domination"],  # Question 13, Answer 7 -> Domination
    # Question 14
    (14, 1): ["Fire"],  # Question 14, Answer 1 -> Fire
    (14, 2): ["Force"],  # Question 14, Answer 2 -> Force
    (14, 3): ["Healing"],  # Question 14, Answer 3 -> Healing
    (14, 4): ["Inquisition"],  # Question 14, Answer 4 -> Inquisition
    (14, 5): ["Law"],  # Question 14, Answer 5 -> Law
    (14, 6): ["Madness", "Liberation"],  # Question 14, Answer 6 -> Madness, Liberation
    (14, 7): ["Mind"],  # Question 14, Answer 7 -> Mind
    # Question 15
    (15, 1): ["Plant"],  # Question 15, Answer 1 -> Plant
    (15, 2): ["Oracle"],  # Question 15, Answer 2 -> Oracle
    (15, 3): ["Strength", "War"],  # Question 15, Answer 3 -> Strength, War
    (15, 4): [
        "Pestilence",
        "Destruction",
    ],  # Question 15, Answer 4 -> Pestilence, Destruction
    (15, 5): ["Travel"],  # Question 15, Answer 5 -> Travel
    (15, 6): ["Summoner"],  # Question 15, Answer 6 -> Summoner
    (15, 7): ["Weather"],  # Question 15, Answer 7 -> Weather
    # Question 16
    (16, 1): ["Water"],  # Question 16, Answer 1 -> Water
    (16, 2): ["Animal"],  # Question 16, Answer 2 -> Animal
    (16, 3): ["Cold"],  # Question 16, Answer 3 -> Cold
    (16, 4): ["Death"],  # Question 16, Answer 4 -> Death
    (16, 5): [
        "Competition",
        "Community",
    ],  # Question 16, Answer 5 -> Competition, Community
    (16, 6): ["Earth"],  # Question 16, Answer 6 -> Earth
    (16, 7): ["Evil"],  # Question 16, Answer 7 -> Evil
    # Question 17
    (17, 1): ["Dream"],  # Question 17, Answer 1 -> Dream
    (17, 2): ["Good"],  # Question 17, Answer 2 -> Good
    (17, 3): ["Glory", "Sun"],  # Question 17, Answer 3 -> Glory, Sun
    (17, 4): ["Knowledge"],  # Question 17, Answer 4 -> Knowledge
    (17, 5): ["Liberation", "Madness"],  # Question 17, Answer 5 -> Liberation, Madness
    (17, 6): ["Luck", "Protection"],  # Question 17, Answer 6 -> Luck, Protection
    (17, 7): ["Magic"],  # Question 17, Answer 7 -> Magic
    # Question 18
    (18, 1): ["Mysticism"],  # Question 18, Answer 1 -> Mysticism
    (18, 2): ["Protection", "Luck"],  # Question 18, Answer 2 -> Protection, Luck
    (18, 3): ["Pact"],  # Question 18, Answer 3 -> Pact
    (18, 4): ["Sun", "Glory"],  # Question 18, Answer 4 -> Sun, Glory
    (18, 5): ["Purification"],  # Question 18, Answer 5 -> Purification
    (18, 6): ["Trickery"],  # Question 18, Answer 6 -> Trickery
    (18, 7): ["War", "Strength"],  # Question 18, Answer 7 -> War, Strength
    # Question 19
    (19, 1): ["Air"],  # Question 19, Answer 1 -> Air
    (19, 2): ["Good", "Glory"],  # Question 19, Answer 2 -> Good, Glory
    (19, 3): [
        "Strength",
        "Protection",
    ],  # Question 19, Answer 3 -> Strength, Protection
    (19, 4): ["Community"],  # Question 19, Answer 4 -> Community
    (19, 5): ["Liberation", "Luck"],  # Question 19, Answer 5 -> Liberation, Luck
    (19, 6): ["Summoner"],  # Question 19, Answer 6 -> Summoner
    (19, 7): ["Weather", "Cold"],  # Question 19, Answer 7 -> Weather, Cold
    # Question 20
    (20, 1): ["Fire"],  # Question 20, Answer 1 -> Fire
    (20, 2): [
        "Protection",
        "Strength",
    ],  # Question 20, Answer 2 -> Protection, Strength
    (20, 3): ["Cold", "Weather"],  # Question 20, Answer 3 -> Cold, Weather
    (20, 4): ["Inquisition", "Mind"],  # Question 20, Answer 4 -> Inquisition, Mind
    (20, 5): ["Purification"],  # Question 20, Answer 5 -> Purification
    (20, 6): ["Earth"],  # Question 20, Answer 6 -> Earth
    (20, 7): ["Evil"],  # Question 20, Answer 7 -> Evil
    # Question 21
    (21, 1): ["Plant"],  # Question 21, Answer 1 -> Plant
    (21, 2): ["Celerity"],  # Question 21, Answer 2 -> Celerity
    (21, 3): ["Glory", "Good"],  # Question 21, Answer 3 -> Glory, Good
    (21, 4): ["Pestilence"],  # Question 21, Answer 4 -> Pestilence
    (21, 5): ["Destruction"],  # Question 21, Answer 5 -> Destruction
    (21, 6): ["Luck", "Liberation"],  # Question 21, Answer 6 -> Luck, Liberation
    (21, 7): ["Magic"],
    # Question 22
    (22, 1): ["Water"],  # Question 22, Answer 1 -> Water
    (22, 2): ["Force"],  # Question 22, Answer 2 -> Force
    (22, 3): ["Pact", "Knowledge"],  # Question 22, Answer 3 -> Pact, Knowledge
    (22, 4): ["Death"],  # Question 22, Answer 4 -> Death
    (22, 5): ["Law"],  # Question 22, Answer 5 -> Law
    (22, 6): ["Trickery", "Madness"],  # Question 22, Answer 6 -> Trickery, Madness
    (22, 7): ["War", "Community"],  # Question 22, Answer 7 -> War, Community
    # Question 23
    (23, 1): ["Dream"],  # Question 23, Answer 1 -> Dream
    (23, 2): ["Oracle"],  # Question 23, Answer 2 -> Oracle
    (23, 3): ["Chaos"],  # Question 23, Answer 3 -> Chaos
    (23, 4): ["Knowledge", "Pact"],  # Question 23, Answer 4 -> Knowledge, Pact
    (23, 5): ["Travel"],  # Question 23, Answer 5 -> Travel
    (23, 6): ["Creation"],  # Question 23, Answer 6 -> Creation
    (23, 7): ["Domination"],  # Question 23, Answer 7 -> Domination
    # Question 24
    (24, 1): ["Mysticism"],  # Question 24, Answer 1 -> Mysticism
    (24, 2): ["Animal"],  # Question 24, Answer 2 -> Animal
    (24, 3): ["Healing"],  # Question 24, Answer 3 -> Healing
    (24, 4): ["Sun"],  # Question 24, Answer 4 -> Sun
    (24, 5): ["Competition", "War"],  # Question 24, Answer 5 -> Competition, War
    (24, 6): ["Madness", "Trickery"],  # Question 24, Answer 6 -> Madness, Trickery
    (24, 7): ["Mind", "Inquisition"],  # Question 24, Answer 7 -> Mind, Inquisition
    # Question 25
    (25, 1): ["Air"],  # Question 25, Answer 1 -> Air
    (25, 2): ["Protection", "Magic"],  # Question 25, Answer 2 -> Protection, Magic
    (25, 3): ["Glory"],  # Question 25, Answer 3 -> Glory
    (25, 4): ["Death"],  # Question 25, Answer 4 -> Death
    (25, 5): ["Travel"],  # Question 25, Answer 5 -> Travel
    (25, 6): ["Madness"],  # Question 25, Answer 6 -> Madness
    (25, 7): ["Mind"],  # Question 25, Answer 7 -> Mind
    # Question 26
    (26, 1): ["Fire"],  # Question 26, Answer 1 -> Fire
    (26, 2): ["Celerity"],  # Question 26, Answer 2 -> Celerity
    (26, 3): ["Pact"],  # Question 26, Answer 3 -> Pact
    (26, 4): [
        "Knowledge",
        "Inquisition",
    ],  # Question 26, Answer 4 -> Knowledge, Inquisition
    (26, 5): [
        "Competition",
        "Strength",
        "Mysticism",
    ],  # Question 26, Answer 5 -> Competition, Strength, Mysticism
    (26, 6): ["Summoner"],  # Question 26, Answer 6 -> Summoner
    (26, 7): ["Weather"],  # Question 26, Answer 7 -> Weather
    # Question 27
    (27, 1): ["Plant"],  # Question 27, Answer 1 -> Plant
    (27, 2): ["Force"],  # Question 27, Answer 2 -> Force
    (27, 3): ["Chaos"],  # Question 27, Answer 3 -> Chaos
    (27, 4): ["Sun", "War"],  # Question 27, Answer 4 -> Sun, War
    (27, 5): ["Liberation", "Luck"],  # Question 27, Answer 5 -> Liberation, Luck
    (27, 6): ["Earth"],  # Question 27, Answer 6 -> Earth
    (27, 7): ["Evil"],  # Question 27, Answer 7 -> Evil
    # Question 28
    (28, 1): ["Water"],  # Question 28, Answer 1 -> Water
    (28, 2): ["Oracle"],  # Question 28, Answer 2 -> Oracle
    (28, 3): ["Healing"],  # Question 28, Answer 3 -> Healing
    (28, 4): ["Community"],  # Question 28, Answer 4 -> Community
    (28, 5): ["Purification"],  # Question 28, Answer 5 -> Purification
    (28, 6): ["Luck", "Liberation"],  # Question 28, Answer 6 -> Luck, Liberation
    (28, 7): ["Magic", "Protection"],  # Question 28, Answer 7 -> Magic, Protection
    # Question 29
    (29, 1): ["Dream"],  # Question 29, Answer 1 -> Dream
    (29, 2): ["Animal"],  # Question 29, Answer 2 -> Animal
    (29, 3): [
        "Strength",
        "Competition",
        "Mysticism",
    ],  # Question 29, Answer 3 -> Strength, Competition, Mysticism
    (29, 4): [
        "Inquisition",
        "Knowledge",
    ],  # Question 29, Answer 4 -> Inquisition, Knowledge
    (29, 5): ["Destruction"],  # Question 29, Answer 5 -> Destruction
    (29, 6): ["Trickery"],  # Question 29, Answer 6 -> Trickery
    (29, 7): ["War", "Sun"],  # Question 29, Answer 7 -> War, Sun
    # Question 30
    (30, 1): [
        "Mysticism",
        "Competition",
        "Strength",
    ],  # Question 30, Answer 1 -> Mysticism, Competition, Strength
    (30, 2): ["Good"],  # Question 30, Answer 2 -> Good
    (30, 3): ["Cold"],  # Question 30, Answer 3 -> Cold
    (30, 4): ["Pestilence"],  # Question 30, Answer 4 -> Pestilence
    (30, 5): ["Law"],  # Question 30, Answer 5 -> Law
    (30, 6): ["Creation"],  # Question 30, Answer 6 -> Creation
    (30, 7): ["Domination"],  # Question 30, Answer 7 -> Domination
    # Question 31
    (31, 1): ["Air"],  # Question 31, Answer 1 -> Air
    (31, 2): ["Force"],  # Question 31, Answer 2 -> Force
    (31, 3): ["Strength", "Earth"],  # Question 31, Answer 3 -> Strength, Earth
    (31, 4): ["Death", "Evil"],  # Question 31, Answer 4 -> Death, Evil
    (31, 5): ["Liberation"],  # Question 31, Answer 5 -> Liberation
    (31, 6): ["Trickery", "Luck"],  # Question 31, Answer 6 -> Trickery, Luck
    (31, 7): ["War"],  # Question 31, Answer 7 -> War
    # Question 32
    (32, 1): ["Fire"],  # Question 32, Answer 1 -> Fire
    (32, 2): ["Oracle"],  # Question 32, Answer 2 -> Oracle
    (32, 3): ["Cold"],  # Question 32, Answer 3 -> Cold
    (32, 4): ["Knowledge", "Travel"],  # Question 32, Answer 4 -> Knowledge, Travel
    (32, 5): ["Purification"],  # Question 32, Answer 5 -> Purification
    (32, 6): ["Creation"],  # Question 32, Answer 6 -> Creation
    (32, 7): [
        "Domination",
        "Inquisition",
    ],  # Question 32, Answer 7 -> Domination, Inquisition
    # Question 33
    (33, 1): ["Dream"],  # Question 33, Answer 1 -> Dream
    (33, 2): ["Protection", "Magic"],  # Question 33, Answer 2 -> Protection, Magic
    (33, 3): ["Chaos"],  # Question 33, Answer 3 -> Chaos
    (33, 4): [
        "Inquisition",
        "Domination",
    ],  # Question 33, Answer 4 -> Inquisition, Domination
    (33, 5): ["Travel", "Knowledge"],  # Question 33, Answer 5 -> Travel, Knowledge
    (33, 6): ["Earth", "Strength"],  # Question 33, Answer 6 -> Earth, Strength
    (33, 7): ["Evil", "Death"],  # Question 33, Answer 7 -> Evil, Death
    # Question 34
    (34, 1): ["Water"],  # Question 34, Answer 1 -> Water
    (34, 2): ["Good"],  # Question 34, Answer 2 -> Good
    (34, 3): ["Pact"],  # Question 34, Answer 3 -> Pact
    (34, 4): ["Community"],  # Question 34, Answer 4 -> Community
    (34, 5): ["Law"],  # Question 34, Answer 5 -> Law
    (34, 6): ["Summoner"],  # Question 34, Answer 6 -> Summoner
    (34, 7): ["Weather"],  # Question 34, Answer 7 -> Weather
    # Question 35
    (35, 1): ["Plant"],  # Question 35, Answer 1 -> Plant
    (35, 2): ["Animal"],  # Question 35, Answer 2 -> Animal
    (35, 3): ["Glory"],  # Question 35, Answer 3 -> Glory
    (35, 4): ["Sun"],  # Question 35, Answer 4 -> Sun
    (35, 5): ["Destruction"],  # Question 35, Answer 5 -> Destruction
    (35, 6): ["Madness"],  # Question 35, Answer 6 -> Madness
    (35, 7): ["Mind"],  # Question 35, Answer 7 -> Mind
    # Question 36
    (36, 1): ["Mysticism"],  # Question 36, Answer 1 -> Mysticism
    (36, 2): ["Celerity"],  # Question 36, Answer 2 -> Celerity
    (36, 3): ["Healing"],  # Question 36, Answer 3 -> Healing
    (36, 4): ["Pestilence"],  # Question 36, Answer 4 -> Pestilence
    (36, 5): ["Competition"],  # Question 36, Answer 5 -> Competition
    (36, 6): ["Luck", "Trickery"],  # Question 36, Answer 6 -> Luck, Trickery
    (36, 7): ["Magic", "Protection"],  # Question 36, Answer 7 -> Magic, Protection
}
