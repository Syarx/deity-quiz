import itertools
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict
import os

# Constants
NUM_QUESTIONS = 39
NUM_ANSWERS = 7
DOMAINS = [
    "Air",
    "Animal",
    "Chaos",
    "Death",
    "Destruction",
    "Earth",
    "Evil",
    "Fire",
    "Good",
    "Healing",
    "Knowledge",
    "Law",
    "Luck",
    "Magic",
    "Plant",
    "Protection",
    "Strength",
    "Sun",
    "Travel",
    "Trickery",
    "War",
    "Water",
    "Celerity",
    "Cold",
    "Community",
    "Competition",
    "Creation",
    "Domination",
    "Dream",
    "Force",
    "Glory",
    "Inquisition",
    "Liberation",
    "Madness",
    "Mind",
    "Mysticism",
    "Oracle",
    "Pact",
    "Pestilence",
    "Purification",
    "Summoner",
    "Weather",
]

# Initialize points for domains
domain_points = {domain: 0 for domain in DOMAINS}

# Custom point rules (example)
custom_points = {
    (1, 1): 2,
    (4, 1): 2,
    (6, 7): 2,
    (4, 7): 3,
    (6, 3): 3,  # Answers giving extra points ENA
    (7, 2): 3,
    (7, 6): 3,
    (8, 3): 3,
    (8, 7): 3,
    (9, 2): 3,
    (9, 3): 3,
    (10, 1): 3,
    (10, 2): 3,
    (10, 7): 3,
    (11, 1): 3,
    (11, 4): 3,
    (11, 5): 3,
    (11, 7): 3,
    (12, 1): 3,  # Answers giving extra points DYO
    (13, 4): 3,
    (13, 5): 3,
    (14, 6): 3,
    (15, 3): 3,
    (15, 4): 3,
    (16, 5): 3,
    (17, 3): 3,
    (17, 5): 3,
    (17, 6): 3,
    (18, 2): 3,
    (18, 4): 3,
    (18, 7): 3,  # Answers giving extra points TRIA
    (19, 2): 3,
    (19, 3): 3,
    (19, 5): 3,
    (19, 7): 3,
    (20, 2): 3,
    (20, 3): 3,
    (20, 4): 3,
    (21, 3): 3,
    (21, 6): 3,
    (22, 3): 3,
    (22, 6): 3,
    (22, 7): 3,
    (23, 4): 3,
    (24, 5): 3,
    (24, 6): 3,
    (24, 7): 3,  # Answers giving extra points TESSERA
    (25, 2): 3,
    (26, 4): 3,
    (26, 5): 2,
    (27, 4): 3,
    (27, 5): 3,
    (28, 6): 3,
    (28, 7): 3,
    (29, 3): 2,
    (29, 4): 3,
    (29, 7): 3,
    (30, 1): 2,  # Answers giving extra points PENTE
    (31, 3): 3,
    (31, 4): 3,
    (31, 6): 3,
    (32, 4): 3,
    (32, 7): 3,
    (33, 2): 3,
    (33, 4): 3,
    (33, 5): 3,
    (33, 6): 3,
    (33, 7): 3,
    (36, 6): 3,
    (36, 7): 3,  # Answers giving extra points EXI
    (37, 1): 4,
    (37, 2): 4,
    (37, 3): 4,
    (37, 4): 4,
    (37, 5): 4,
    (37, 6): 4,
    (37, 7): 4,
    (38, 1): 2,
    (38, 2): 2,
    (38, 3): 0,
    (38, 4): 2,
    (38, 5): 2,
    (38, 6): 2,
    (38, 7): 2,
    (38, 8): 2,
    (38, 9): 2,
    (38, 10): 2,
    (39, 1): 5,
    (39, 2): 5,
    (39, 3): 5,
    (39, 4): 5,
    (39, 5): 5,
    (39, 6): 5,
    (39, 7): 5,
    (39, 8): 5,
    (39, 9): 5,
}

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

gods_by_domains = {
    "Bahamut": ["Air", "Cold", "Good", "Luck", "Protection"],
    "Boccob": ["Knowledge", "Magic", "Mind", "Oracle", "Trickery"],
    "Corellon Larethian": ["Chaos", "Community", "Good", "Protection", "War"],
    "Ehlonna": ["Animal", "Celerity", "Good", "Plant", "Sun"],
    "Erythnul": ["Chaos", "Evil", "Madness", "Trickery", "War"],
    "Fharlanghn": ["Celerity", "Luck", "Protection", "Travel", "Weather"],
    "Garl Glittergold": ["Community", "Creation", "Good", "Protection", "Trickery"],
    "Gruumsh": ["Chaos", "Domination", "Evil", "Strength", "War"],
    "Heironeous": ["Glory", "Good", "Inquisition", "Law", "War"],
    "Hextor": ["Destruction", "Domination", "Evil", "Law", "War"],
    "Kord": ["Chaos", "Competition", "Good", "Luck", "Strength"],
    "Kurtulmak": ["Evil", "Law", "Luck", "Trickery"],
    "Lolth": ["Chaos", "Destruction", "Evil", "Trickery"],
    "Moradin": ["Creation", "Earth", "Good", "Law", "Protection"],
    "Nerull": ["Death", "Evil", "Pestilence", "Trickery"],
    "Obad-Hai": ["Air", "Animal", "Earth", "Fire", "Plant", "Water", "Weather"],
    "Olidammara": ["Celerity", "Chaos", "Luck", "Mind", "Trickery"],
    "Pelor": ["Glory", "Good", "Healing", "Purification", "Strength", "Sun"],
    "St. Cuthbert": ["Destruction", "Domination", "Law", "Protection", "Strength"],
    "Tiamat": ["Destruction", "Evil", "Law", "Trickery"],
    "Vecna": ["Evil", "Knowledge", "Madness", "Magic"],
    "Wee Jas": ["Death", "Domination", "Law", "Magic", "Mind"],
    "Yondalla": ["Community", "Creation", "Good", "Law", "Protection"],
}

gods_by_race = {
    "Bahamut": [],
    "Boccob": [],
    "Corellon Larethian": ["Elf", "Half-elf"],
    "Ehlonna": ["Elf", "Half-elf", "Gnome", "Halfling"],
    "Erythnul": [],
    "Fharlanghn": [],
    "Garl Glittergold": ["Gnome"],
    "Gruumsh": ["Half-orc"],
    "Heironeous": ["Human"],
    "Hextor": [],
    "Kord": [],
    "Kurtulmak": [],
    "Lolth": [],
    "Moradin": ["Dwarf"],
    "Nerull": [],
    "Obad-Hai": [],
    "Olidammara": [],
    "Pelor": ["Human"],
    "St. Cuthbert": [],
    "Tiamat": [],
    "Vecna": [],
    "Wee Jas": [],
    "Yondalla": ["Halfling"],
}

gods_by_class = {
    "Bahamut": [],
    "Boccob": ["Sorcerer", "Wizard"],
    "Corellon Larethian": [],
    "Ehlonna": ["Ranger"],
    "Erythnul": ["Barbarian", "Fighter", "Rogue"],
    "Fharlanghn": ["Bard"],
    "Garl Glittergold": [],
    "Gruumsh": [],
    "Heironeous": ["Fighter", "Monk", "Paladin"],
    "Hextor": ["Fighter", "Monk"],
    "Kord": ["Barbarian", "Fighter"],
    "Kurtulmak": [],
    "Lolth": [],
    "Moradin": [],
    "Nerull": ["Rogue"],
    "Obad-Hai": ["Barbarian", "Druid", "Ranger"],
    "Olidammara": ["Bard", "Rogue"],
    "Pelor": ["Bard"],
    "St. Cuthbert": ["Fighter", "Monk"],
    "Tiamat": [],
    "Vecna": ["Rogue", "Sorcerer", "Wizard"],
    "Wee Jas": ["Sorcerer", "Wizard"],
    "Yondalla": [],
}

gods_by_alignment = {
    "Bahamut": "Lawful Good",
    "Boccob": "True Neutral",
    "Corellon Larethian": "Chaotic Good",
    "Ehlonna": "Neutral Good",
    "Erythnul": "Chaotic Evil",
    "Fharlanghn": "True Neutral",
    "Garl Glittergold": "Neutral Good",
    "Gruumsh": "Chaotic Evil",
    "Heironeous": "Lawful Good",
    "Hextor": "Lawful Evil",
    "Kord": "Chaotic Good",
    "Kurtulmak": "Lawful Evil",
    "Lolth": "Chaotic Evil",
    "Moradin": "Lawful Good",
    "Nerull": "Neutral Evil",
    "Obad-Hai": "True Neutral",
    "Olidammara": "Chaotic Neutral",
    "Pelor": "Neutral Good",
    "St. Cuthbert": "Lawful Neutral",
    "Tiamat": "Lawful Evil",
    "Vecna": "Neutral Evil",
    "Wee Jas": "Lawful Neutral",
    "Yondalla": "Lawful Good",
}

gods_by_title = {
    "Bahamut": "the God of good dragons",
    "Boccob": "the God of magic",
    "Corellon Larethian": "the god of elfs",
    "Ehlonna": "the God of good people living in the forest",
    "Erythnul": "the God of slaughter",
    "Fharlanghn": "the God of the roads",
    "Garl Glittergold": "the God of gnomes",
    "Gruumsh": "the God of orcs",
    "Heironeous": "the God of justice",
    "Hextor": "the God of Conflict",
    "Kord": "the God of athleticism",
    "Kurtulmak": "the God of kobolds",
    "Lolth": "the God of the drows",
    "Moradin": "the God of the dwarfs",
    "Nerull": "the God of death",
    "Obad-Hai": "the God of the forest",
    "Olidammara": "the God of celebration",
    "Pelor": "the God of the sun",
    "St. Cuthbert": "the God of order",
    "Tiamat": "the God of evil dragons",
    "Vecna": "the God of secrets",
    "Wee Jas": "the God of afterlife",
    "Yondalla": "the God of halflings",
}

questions = [
    "A caravan is stranded in the wilderness after their path was blocked by a group of aggressive creatures—some wild animals and others trained beasts. The caravan is guarded by mercenaries who are suspicious of outsiders and align strongly with either good or law. The caravan must continue on its way, but violence could escalate the situation, and the players want to resolve it without direct combat.",
    """The party is exploring an ancient, cursed ruin where a valuable artifact is hidden. The ruins are plagued by malevolent spirits, trapped souls, and physical traps designed to protect the artifact. The party needs to find the artifact and escape, but they face several challenges along the way:

• Hostile spirits and animated guardians attack on sight.
• There are paths and maybe even the artifact hidden behind a secret door.
• The traps react unpredictably, including shooting projectiles.
• The artifact is cursed to track anyone carrying it, potentially summoning more danger.""",
    "The party is helping a small village fend off a band of raiders who are attacking to steal supplies. The raiders are better equipped than the villagers, but the villagers have set a trap to ambush them in a nearby forest. The party must either delay, confuse, or weaken the raiders to turn the tide in the villagers’ favor.",
    """A caravan of refugees is attempting to cross a harsh desert to escape pursuing slavers. The slavers are closing in, and the caravan faces multiple challenges:

• The intense heat is sapping the refugees’ strength.
• The caravan’s water supply is running low.
• Some refugees are panicking and threatening to scatter.
• The slavers are closing the distance, and a direct confrontation would likely end in disaster.
The party must ensure the caravan escapes safely.""",
    "The party arrives at a remote monastery to seek ancient knowledge, only to find the monks acting strangely. Some appear hostile and others apathetic, but none will speak plainly about what is happening. The monastery is rumored to guard a hidden crypt containing powerful undead, and the party must uncover the truth while avoiding unnecessary bloodshed and dealing with potential danger.",
    "The party has been tasked with retrieving a stolen relic from a band of thieves who are holed up in an abandoned temple. The temple is filled with magical wards and traps, and the thieves are guarding the relic in a hidden chamber. The party must recover the relic without damaging it and deal with the thieves, who are suspicious and on high alert.",
    "The party has been hired to recover a sacred artifact stolen by a band of mercenaries and hidden in their fortified desert camp. The artifact is needed for a critical religious ritual, but the mercenaries are expecting pursuit and have set up defensive measures, including traps, ranged attackers, and magical wards. The party must find and retrieve the artifact while avoiding unnecessary bloodshed and ensuring its sanctity remains intact.",
    "The party is mediating a tense dispute between two rival farming communities over access to a magical spring, believed to bring bountiful harvests. The spring is located in a forested area, but the dispute is escalating toward violence, with both sides preparing to fight. Complicating matters, a dangerous beast has recently been sighted near the spring, threatening anyone who approaches. The party must resolve the conflict peacefully, protect the communities, and ensure the beast doesn’t disrupt the fragile truce.",
    "The party is trying to infiltrate a heavily guarded noble’s estate during a grand banquet to retrieve incriminating evidence hidden in a locked vault. The estate is protected by armed guards, magical wards, and nosy guests. The party must navigate the estate stealthily, avoid raising suspicion, and deal with potential combat if their cover is blown, all while retrieving the evidence undamaged.",
    "A small village is under attack by a zealous cult attempting to capture villagers for a dark ritual. The cult’s leader is a charismatic orator who is sowing fear and confusion, convincing some villagers to willingly join the ritual. The cultists are targeting key villagers, including the mayor and healer, to weaken the village’s defenses. The party must protect the villagers, stop the cult’s plans, and confront the leader without causing unnecessary harm to those who have been swayed.",
    "A merchant’s priceless heirloom, a magical sapphire, has been stolen and hidden inside a fortified hideout of a thieves' guild in a bustling city. The hideout is filled with traps, alert guards, and cleverly concealed rooms. The party must retrieve the sapphire without alerting the entire guild, all while navigating both physical and magical obstacles designed to deter intruders.",
    "The party is tasked with breaking a cursed artifact that has fallen into the hands of a powerful good warlord. The artifact is causing the warlord to become increasingly violent, making him a danger to his own people and the surrounding region. The artifact is protected by a series of magical defenses within a well-guarded temple, and the warlord himself is heavily armored and surrounded by loyal guards. The party must neutralize the artifact’s influence on the warlord, secure it, and deal with the temple’s magical defenses and the warlord’s forces without causing unnecessary bloodshed.",
    "A small frontier town is on the brink of collapse under the iron-fisted rule of a tyrannical magistrate, who uses extreme laws and fear to maintain control. The townsfolk are starving due to heavy taxes, morale is low, and any dissent is punished harshly by the magistrate’s enforcers. The party must undermine the magistrate’s authority, restore hope to the townsfolk, and convince them to rise up peacefully against the unjust regime without causing widespread chaos or bloodshed.",
    "A secluded monastery has been overrun by chaotic elemental spirits that have broken free from a sacred relic kept in the temple. The spirits are causing havoc, injuring monks, and destroying the temple’s infrastructure. Meanwhile, a small faction of monks, affected by the spirits’ influence, have turned aggressive and are sabotaging attempts to restore order. The party must protect the remaining monks, subdue the corrupted ones, and banish the spirits while safeguarding the relic.",
    "A once-thriving farming village is suffering from a devastating drought caused by the wrath of a storm spirit angered by the villagers cutting down an ancient grove. Crops have withered, animals are dying, and the villagers are desperate for aid. Meanwhile, a faction of villagers has taken up arms against the spirit, planning to destroy its sacred shrine, which could worsen the situation. The party must restore balance to the land, calm the storm spirit, and prevent the villagers from further antagonizing it.",
    "A coastal town is plagued by attacks from a massive sea creature controlled by a rival faction of underwater raiders. The creature has been sinking fishing boats and destroying docks, crippling the town’s livelihood. The underwater raiders have fortified themselves in an undersea cave, where they keep the creature under magical control. The party must stop the sea creature’s rampage, infiltrate the raiders’ lair, and neutralize their operation without causing harm to innocent sea life.",
    "A haunted manor on the outskirts of town has become a source of terror. Strange lights and sounds have driven away all who enter, and several villagers who dared to investigate have gone missing. The party is hired to explore the manor, uncover the cause of the disturbances, and rescue any survivors. Inside, they find the manor is controlled by a malevolent spirit and its minions, including enchanted constructs and corrupted wildlife, all while a powerful curse disrupts attempts to dispel the spirit.",
    "A holy relic has been stolen from a temple by an unknown thief, and its absence has caused divine protections around the surrounding region to weaken, leaving the area vulnerable to fiends and undead. The party is tasked with recovering the relic, which has been hidden in a crypt guarded by traps, undead sentinels, and demonic wards. To complicate matters, the crypt is shrouded in divinatory magic that makes detecting the relic or identifying its location impossible without careful investigation and divine guidance.",
    """A once-peaceful mountain village is under siege by an icebound frost giant and its minions, who claim the villagers desecrated their sacred glacier. The giant has blocked all mountain passes with ice storms, making escape impossible, and has taken hostages to force the villagers to return the "stolen artifact." The artifact, however, is a misunderstanding—a gift given to the village by a now-deceased elder. The party must negotiate with the frost giant, rescue the hostages, and prevent the village from being destroyed by the raging storms and attacks.""",
    """A remote fortress ruled by a tyrannical baron has become a prison for dissenters and a site of dark rituals. The baron has declared himself the chosen of a deity and holds sway over the region through fear and deception. A rebel group seeks to overthrow him but is divided by suspicion, as a spy is feeding information to the baron. The party must infiltrate the fortress, expose the spy, disrupt the baron’s forces, and either confront or undermine his rule before the baron completes a ritual to summon an abyssal creature to solidify his dominion.""",
    "A cursed grove at the heart of a dense forest has become a dangerous zone where the plants themselves attack anyone who ventures nearby. A powerful druid, corrupted by a mysterious artifact buried beneath the grove, has enslaved the forest's flora and fauna to guard the artifact. Local villagers, once protected by the druid, are now being harassed by aggressive plants, and a group of children has gone missing after wandering into the grove. The party must venture into the forest, rescue the children, and neutralize the corrupted druid without further enraging the forest.",
    "A town by the river is facing a catastrophic flood after a nearby dam, constructed by a reclusive cult, was sabotaged. The dam, once a symbol of prosperity, has been turned into a powerful magical trap by the cult, causing the water level to rise uncontrollably. The town is on the brink of being submerged, and the cult plans to use the flood to drown the town and its people as part of a dark ritual to awaken an ancient water deity. The party must navigate the flooded town, find the cultists, and stop the ritual before the waters completely overwhelm the town.",
    "A powerful necromancer has taken control of an ancient library hidden beneath a mountain, and is using its vast collection of forbidden knowledge to develop a curse that could bring the world to its knees. The necromancer has captured a group of scholars who were studying the library's secrets, forcing them to assist in completing the ritual that will release the curse. The party must infiltrate the library, find the necromancer, free the scholars, and stop the ritual before the curse is completed. However, the necromancer is extremely paranoid and has placed traps, magical protections, and underlings in place to deter any intruders.",
    "A ruthless band of marauding cultists has taken over a strategic fortress, using it as a base to launch raids on nearby villages. The leader of the cult, a former paladin turned fanatic, has claimed the fortress as his stronghold and is preparing to perform a blood ritual to summon a powerful demon. The cultists have fortified the stronghold with traps, and their leader is protected by a powerful magical aura. The party must infiltrate the fortress, defeat the cultists, and stop the blood ritual before the demon is summoned, but they must also confront the leader, who wields divine power and commands his followers with unyielding authority.",
    "A remote mountain monastery that protects an ancient, sacred relic has come under siege by a ruthless warlord and their army. The warlord seeks the relic, believing it will grant them divine power. The monastery’s monks have managed to hold off the attackers using their defenses, but their numbers are dwindling, and the siege has caused significant destruction. The party is tasked with breaking the siege, protecting the relic, and ensuring the warlord cannot claim it for their own.",
    "The coastal town of Seacrest Haven is under attack by a marauding pirate fleet, led by a fearsome captain who wields a magical artifact capable of summoning destructive storms. The pirates are using the artifact to besiege the town, prevent reinforcements from arriving, and pillage the surrounding area. The artifact’s power is tied to an ancient druidic grove located inland, where the captain has hidden a portion of his forces. The party must defend the town, locate the grove, and disable the artifact before the pirates destroy the region.",
    """The once-harmonious valley is now torn apart by two warring factions: the Order of the Silver Flame, a zealously lawful group, and the Wildwood Pact, a chaotic good druidic circle. Both sides claim to protect the valley, but their battle has devastated the land and threatened the ancient Crystal Nexus, a magical focus buried beneath the valley that stabilizes the region’s natural and arcane balance. Worse, both groups are unwittingly empowering a malicious entity sealed in the Nexus with their magical conflict, and its awakening would unleash catastrophe.
The party must quell the conflict, secure the Nexus, and restore balance before the valley collapses into ruin.""",
    "An isolated mountain city is under the grip of a magical curse that has left its people trapped in a state of dreamlike lethargy. The curse was cast by a vengeful frost spirit, Eira, after the city disturbed her sacred glacier to mine rare ice crystals. To make matters worse, a deadly blizzard conjured by Eira has encased the city in ice, cutting it off from the outside world. The party must navigate the storm, appease or defeat Eira, and lift the curse before the city succumbs to the freezing conditions.",
    "The once-prosperous town of Willowshade has fallen into despair after its mayor, Ellis, fell under the sway of a malevolent forest spirit. The spirit uses Ellis as a puppet to spread fear and chaos in the surrounding areas, encouraging the town’s descent into paranoia and self-destruction. The spirit is concealed in the heart of an ancient, mist-filled forest, protected by illusions and magical wards. The party must root out the spirit, free Ellis from its control, and prevent the destruction of Willowshade and the surrounding lands.",
    "The grand temple of Zalthar the Unerring, a beacon of harmony in the city of Ethoril, has become a battleground for chaos and corruption. A rogue priest named Verik Callan has summoned two powerful outsiders: a Herald of Chaos and a Herald of Malevolence. These entities have turned the temple into a war zone, each vying for control over the sacred site and twisting it to their purpose. The temple’s clergy and citizens are trapped in the chaos, caught in a web of conflicting compulsions and destructive energy. The party must defeat or banish both entities, restore peace to the temple, and ensure the safety of the survivors.",
    "The once-thriving mountain fortress of Karvand Keep has been overrun by a powerful lich, who has enslaved the spirits of the fortress’s ancient defenders and raised their corpses as undead sentinels. The lich has sealed himself in the keep’s central chamber, where he is preparing a massive ritual to unleash a devastating magical plague on the surrounding kingdoms. The keep is filled with traps, undead minions, and magical wards that make direct assault almost impossible. The party must navigate the keep, deal with the lich’s forces, and stop the ritual before it’s too late.",
    "The remote volcanic island of Ashspire, once home to a peaceful monastery dedicated to the deity of fire and renewal, has been overtaken by a vengeful fire elemental lord, Zarvok. Zarvok seeks to erupt the island’s dormant volcano, spreading destruction across the nearby coastal cities. The monks of the monastery attempted to stop him but were either killed or captured. The elemental lord’s lair is deep within the volcano, protected by dangerous lava flows, hostile fire elementals, and ancient traps tied to the island’s volcanic magic. The party must stop Zarvok before he triggers the eruption, rescue any surviving monks, and restore balance to the island.",
    "In the sprawling city of Karthas, the sacred vault of the Emerald Covenant, an ancient order of scholars and mystics, has been compromised. The vault houses an artifact that binds the spiritual energies of the city, protecting it from planar breaches and magical corruption. A rogue mage named Darian Vayne has stolen the artifact and hidden it within the city’s labyrinthine undercrofts. Without the artifact, the city is succumbing to waves of magical instability—random portals opening, objects animating on their own, and citizens falling prey to chaotic magical effects. The party must recover the artifact, return it to the vault, and stabilize the city before it is entirely overrun.",
    "The floating city of Zephyra, a marvel of arcane engineering, is on the brink of disaster. A renegade wizard, Mordavi, has tampered with the city's weather-control mechanisms to create an unending storm that threatens to destabilize the city's levitation crystals. As the storms grow worse, the city risks plummeting into the ocean below, dooming its tens of thousands of inhabitants. Mordavix has fortified himself in the central spire, protected by elementals and arcane wards, while the storms rage uncontrollably around the city. The party must navigate the chaos, confront Mordavix, and stabilize the weather before the city falls.",
    "In an ancient forest filled with powerful fey magic and long-forgotten secrets, an evil druid named Talvorn has unleashed a corrupting plague upon the land. The plague has warped the very plants and creatures of the forest, turning them into monstrous versions of themselves, now attacking travelers and consuming the land’s magic. At the center of the corruption stands The Heart of the Vale, a sacred tree imbued with ancient fey power, now slowly withering under Talvorn’s influence. The party must stop him, cleanse the Heart of the Vale, and restore the forest before it becomes completely consumed by the plague.",
    "The Temple of the Moon, a sacred site dedicated to a long-forgotten goddess, has been overtaken by a powerful and malevolent creature: Varolath, an ancient lycanthrope who once served as the goddess's protector. Corrupted by a dark curse, Varolath has turned the temple into a lair of monstrous creatures, preying on anyone who dares enter. To make matters worse, the temple's celestial guardians have been driven mad, and a blood moon is rising, amplifying the beast’s power. The party has been tasked with entering the temple, confronting Varolath, and breaking the curse before the blood moon reaches its peak and the creature becomes unstoppable.",
    "What is your race?",
    "What are your class/es?",
    "What is your alignment?",
]

answers = {
    (
        1,
        1,
    ): "1. Create a fog to obscure the area, allowing the caravan to slip away unnoticed while the creatures and mercenaries lose sight of their targets.",
    (
        1,
        2,
    ): "2. Calm the wild creatures blocking the path, making it safe for the caravan to pass through without harm.",
    (
        1,
        3,
    ): "3. If the mercenaries are heavily aligned with law, cast a spell that protects you against hostile magic or physical interference from them during negotiation or escape.",
    (
        1,
        4,
    ): "4. Target one of the mercenaries or a leading beast to frighten them, scattering the opposition and opening the path.",
    (
        1,
        5,
    ): "5. If peaceful methods fail, use a slight touch as a quick strike to incapacitate a key creature or mercenary and intimidate the rest.",
    (
        1,
        6,
    ): "6. Use enchanted stones to take down a key creature from a distance without putting yourself in direct harm.",
    (
        1,
        7,
    ): "7. Cast this if the mercenaries are good-aligned and using magical abilities to try and enforce their will on the caravan or the players.",
    (
        2,
        1,
    ): "1. Shoot fire to clear away hostile spirits, animated constructs, or overgrown vegetation that blocks progress. Also useful for quickly disarming certain traps or barriers.",
    (
        2,
        2,
    ): "2. Protect the party from attacks by malevolent spirits and animated constructs that are aligned with evil, ensuring safer passage.",
    (
        2,
        3,
    ): "3. Heal injuries sustained from traps or combat encounters, keeping the party in good shape to continue exploring the ruin.",
    (
        2,
        4,
    ): "4. Locate the hidden passages or compartments where the artifact might be stored, bypassing long searches or brute force attempts.",
    (
        2,
        5,
    ): "5. Protect against chaotic traps or spirits if the dangers align with chaos instead of evil. It ensures safety from unpredictable magical effects.",
    (
        2,
        6,
    ): "6. Protect yourself from the ruin’s projectile traps, such as darts or arrows, by making them less likely to hit.",
    (
        2,
        7,
    ): "7. Mask the artifact's cursed properties temporarily to prevent it from summoning additional dangers while the party carries it out of the ruins.",
    (
        3,
        1,
    ): "1. Grow the vegetation in the forest to trap or slow the raiders, preventing them from reaching the village quickly and giving the villagers time to prepare or attack.",
    (
        3,
        2,
    ): "2. Cast a protective spell on a key villager, like the leader or a healer, to ensure they are protected during the battle, even if surrounded by enemies.",
    (
        3,
        3,
    ): "3. Make a strong villager or a party member grow larger to intimidate the raiders and give the villagers a powerful combatant to turn the tide of battle.",
    (
        3,
        4,
    ): "4. Protect villagers who are hiding in harsh conditions (e.g., intense heat or cold) during the attack, ensuring they can endure until the danger passes.",
    (
        3,
        5,
    ): "5. Give a scout or messenger extra speed to warn the villagers of the raiders’ approach or to outmaneuver the enemy in the forest.",
    (
        3,
        6,
    ): "6. Pretend to be one of the raiders or their leader to confuse or mislead the group, potentially buying time or turning them against one another.",
    (
        3,
        7,
    ): "7. Enhance a villager's or party member’s weapon to ensure they can bypass the raiders’ armor or magical defenses, making the ambush more effective.",
    (
        4,
        1,
    ): "1. Create a thick fog that hides the caravan’s movements, confusing the slavers and allowing the refugees to slip away unnoticed.",
    (
        4,
        2,
    ): "2. Swiftly scout ahead or deliver critical supplies faster, ensuring the caravan stays on track and avoids dangerous terrain.",
    (
        4,
        3,
    ): "3. Confront the slavers’ scouts or advance parties with a magical touch that deals damage and potentially weakens their resolve.",
    (
        4,
        4,
    ): "4. Bolster the caravan’s morale and fighting ability, giving them the courage to face challenges or a slaver skirmish.",
    (
        4,
        5,
    ): "5. Calm panicking refugees so they don’t scatter and attract attention, keeping the group together and focused on survival.",
    (
        4,
        6,
    ): "6. Replenish the caravan’s water supply to ensure everyone survives the desert heat. This is essential for avoiding dehydration and exhaustion.",
    (
        4,
        7,
    ): """7. Issue a magical command to a slaver scout or leader, such as "Flee" or "Fall," to disrupt their pursuit or sow chaos among them.""",
    (
        5,
        1,
    ): "1. Bring the hostile monks to magical sleep in order to render them unconscious without causing harm, allowing the party to bypass them or interrogate them later.",
    (
        5,
        2,
    ): "2. Protect yourself or an ally from harm in case the monks or hidden undead become violent, ensuring survivability in combat.",
    (
        5,
        3,
    ): "3. If undead creatures are found in the crypt or elsewhere in the monastery, cast a spell to deal damage and destroy them.",
    (
        5,
        4,
    ): "4. Determine if the strange behavior of the monks stems from chaotic influence, such as possession or an external entity.",
    (
        5,
        5,
    ): "5. Use a divination to assess whether entering the crypt or interacting with the monks will lead to immediate danger, helping the party plan their next steps.",
    (
        5,
        6,
    ): "6. Cast this to disorient hostile monks or undead, disrupting their actions and giving the party time to escape or gain the upper hand.",
    (
        5,
        7,
    ): "7. Read the ancient texts or cryptic writings in the monastery, uncovering the secrets of what is happening and learning how to resolve the situation.",
    (
        6,
        1,
    ): "1. Bolster your combat abilities when facing the thieves in direct confrontation, giving yourself a boost to strike them down quickly and efficiently.",
    (
        6,
        2,
    ): "2. Analyze the magical wards on the relic or traps in the temple to understand how they work and disable or bypass them without triggering harm.",
    (
        6,
        3,
    ): """3. Issue a one-word command to a thief, such as "Drop," to force them to release the relic or their weapon, creating an opening for the party to act.""",
    (
        6,
        4,
    ): "4. Intimidate a thief or multiple thieves by cursing them with a sense of dread, lowering their morale and making them more likely to flee or surrender.",
    (
        6,
        5,
    ): "5. Illuminate dark areas of the temple and intimidate thieves by appearing as a divine avenger, potentially deterring a fight.",
    (
        6,
        6,
    ): "6. Send a raven to scout ahead, spy on the thieves’ positions, or retrieve a small key or item needed to unlock the hidden chamber.",
    (
        6,
        7,
    ): "7. Create a fog to obscure vision in the temple, allowing the party to slip past guards, confuse the thieves, or stage an ambush on their terms.",
    (
        7,
        1,
    ): "1. Erect a wall of wind to block the mercenaries’ ranged attacks, allowing the party to approach the camp safely or escape with the artifact.",
    (
        7,
        2,
    ): "2. Use divination magic to learn whether a specific course of action—such as storming the camp directly or sneaking in at night—will bring good or ill results, helping the party plan effectively.",
    (
        7,
        3,
    ): "3. Empower a weapon to ensure it can bypass any magical defenses or resistances protecting the artifact or used by the mercenaries.",
    (
        7,
        4,
    ): "4. Keep track of party members’ health and condition, ensuring that no one is left behind or lost in the chaos of infiltrating the camp.",
    (
        7,
        5,
    ): "5. Pinpoint the artifact’s exact location within the camp, saving time and avoiding unnecessary risk searching through the mercenaries’ belongings.",
    (
        7,
        6,
    ): "6. Bolster an ally’s courage and vitality before a critical action, such as a stealthy infiltration, negotiation with the mercenaries, or combat to secure the artifact.",
    (
        7,
        7,
    ): "7. Analyze the artifact once it is recovered to confirm its authenticity and ensure it hasn’t been tampered with or cursed by the mercenaries.",
    (
        8,
        1,
    ): "1. Use a flame to scare off the beast if it threatens the negotiations or illuminate the forest at night to safely approach the spring.",
    (
        8,
        2,
    ): "2. Temporarily incapacitate the beast, preventing it from attacking while the party deals with the dispute or escorts villagers to safety.",
    (
        8,
        3,
    ): "3. Protect a vulnerable negotiator to ensure their safety if tensions rise and violence breaks out. This can prevent a fatal escalation.",
    (
        8,
        4,
    ): "4. Ensure honest dialogue during negotiations, forcing both sides to reveal their true intentions and eliminating deceit or manipulative tactics.",
    (
        8,
        5,
    ): "5. Bolster a party member’s combat abilities if the beast becomes an active threat or one side of the dispute turns violent, ensuring a swift resolution.",
    (
        8,
        6,
    ): "6. Sneak past the arguing factions to investigate the spring directly, uncovering evidence (e.g., who first claimed it or magical tampering) without drawing attention.",
    (
        8,
        7,
    ): "7. Summon a divine weapon to fight the beast or intimidate hostile parties into standing down without needing to risk the lives of villagers or negotiators.",
    (
        9,
        1,
    ): "1. Boost the defense against guards or traps of a party member acting as a distraction or infiltrating a dangerous area.",
    (
        9,
        2,
    ): "2. Grant an ally extra health and courage before they undertake a critical task, such as picking a lock, confronting a guard, or sneaking into the vault.",
    (
        9,
        3,
    ): "3. Destroy the lock or a reinforced door leading to the vault, allowing access to the evidence if stealthier methods fail. You can also use magic to break a chandelier or similar object to create a distraction.",
    (
        9,
        4,
    ): "4. Release a swarm of insects or rats to cause chaos among the guards or banquet guests, drawing attention away from the party’s movements.",
    (
        9,
        5,
    ): "5. Hide the party’s true intentions from a magical ward or a suspicious guest who can sense motives or alignment.",
    (
        9,
        6,
    ): "6. Create an illusion of a guard, noble, or other person to mislead guards, distract guests, or cover the party’s movements.",
    (
        9,
        7,
    ): "7. Captivate the attention of the banquet guests or guards, ensuring they are too focused on the performer to notice the party sneaking around.",
    (
        10,
        1,
    ): "1. Create a dense fog to obscure the cultists’ vision, allowing villagers to escape safely or giving the party a chance to regroup and ambush the enemy.",
    (
        10,
        2,
    ): "2. Protect a key villager, such as the healer or mayor, by absorbing some of the damage they might take during the attack, keeping them alive.",
    (
        10,
        3,
    ): "3. Heal injured villagers or allies to keep them fighting fit or ensure critical individuals can escape or resist the cult’s magic.",
    (
        10,
        4,
    ): "4. Cast a spell on a fallen cultist to gain temporary strength and bolster yourself for a critical confrontation with the cult leader or their strongest followers.",
    (
        10,
        5,
    ): "5. Deliver divine punishment to a cultist or the leader after being harmed, showcasing your divine power to intimidate or subdue enemies.",
    (
        10,
        6,
    ): "6. Disrupt the cult leader’s speeches or plans by confusing their mind, breaking their influence over the villagers and weakening their leadership.",
    (
        10,
        7,
    ): "7. Probe the minds of villagers or cultists to uncover the cult’s plans, identify their true motives, or locate where the ritual is taking place.",
    (
        11,
        1,
    ): "1. Determine whether attempting a particular route into the hideout or engaging with specific thieves will bring good or ill outcomes, helping the party plan their approach.",
    (
        11,
        2,
    ): "2. Enhance the agility and stealth of a party member tasked with sneaking through the hideout, bypassing traps and avoiding detection by guards.",
    (
        11,
        3,
    ): "3. Bolster the physical power of a party member who needs to force open a hidden door, lift a heavy obstacle, or engage in close combat with guards.",
    (
        11,
        4,
    ): "4. Probe the minds of captured thieves or guards, discovering the location of the sapphire or identifying the safest path through the hideout.",
    (
        11,
        5,
    ): "5. Destroy a locked chest, a reinforced door, or a structural support to create a distraction or gain access to the sapphire’s hiding spot.",
    (
        11,
        6,
    ): "6. Send a bee to scout inaccessible areas, distract guards, or deliver stings to incapacitate enemies without lethal force.",
    (
        11,
        7,
    ): "7. Cover the party’s movements with a thick fog, allowing them to evade detection, escape a dangerous area, or create confusion among the guards.",
    (
        12,
        1,
    ): "1. Summon a divine weapon to fight alongside the party, distracting the warlord's guards or attacking the warlord himself while the party works to neutralize the artifact.",
    (
        12,
        2,
    ): "2. Shoot unnoticeable small arrows to the warlord's vulnerable spots or disable any defensive wards protecting the artifact, ensuring that no magical protections stand in the way.",
    (
        12,
        3,
    ): "3. Chill the warlord's armor or weapon, causing him pain and discomfort, weakening his combat effectiveness or forcing him to remove it, creating an opening for the party.",
    (
        12,
        4,
    ): "4. Heat the warlord’s armor or weapon to an unbearable degree, further disabling his combat abilities and reducing his capacity to fight back, potentially making him surrender.",
    (
        12,
        5,
    ): "5. Calm the warlord's rage and aggression, easing his violent behavior and helping him to regain his composure, making it easier to reason with him or restrain him.",
    (
        12,
        6,
    ): "6. Use this to collapse or open a hidden compartment where the cursed artifact might be stored, allowing the party to access it without triggering further traps or alarms.",
    (
        12,
        7,
    ): "7. Weaken any protective wards around the artifact or the temple, lowering its magical defenses and making it easier to handle the artifact without triggering harmful effects.",
    (
        13,
        1,
    ): "1. Slip into the magistrate’s heavily guarded manor to gather evidence of corruption or plant incriminating documents that reveal the magistrate’s tyranny.",
    (
        13,
        2,
    ): "2. Protect a key townsperson, such as a spokesperson or resistance leader, from harm during a public speech or confrontation with the enforcers, ensuring their survival.",
    (
        13,
        3,
    ): "3. Create a safe zone for the townsfolk, repelling the magistrate’s lawful enforcers or negating magical effects used to control the population.",
    (
        13,
        4,
    ): "4. Bolster the courage and resolve of the townsfolk while subtly weakening the resolve of the enforcers, tipping the balance in favor of peaceful resistance.",
    (
        13,
        5,
    ): "5. Inflict the magistrate with a debilitating illness, weakening their grip on power and undermining their ability to lead or intimidate the townsfolk.",
    (
        13,
        6,
    ): "6. Provide much-needed sustenance to the starving townsfolk, improving their morale and giving them the strength to stand up to the magistrate’s oppression.",
    (
        13,
        7,
    ): "7. Try to Convince the magistrate to step down peacefully or persuade key enforcers to abandon their loyalty, creating cracks in the regime’s foundation.",
    (
        14,
        1,
    ): "1. Protect the monks or party members from elemental damage (fire, lightning, etc.) caused by the chaotic spirits, ensuring their survival during the conflict.",
    (
        14,
        2,
    ): "2. Push back the spirits, knock corrupted monks away from critical areas, or break open a path to the relic if obstacles block the way.",
    (
        14,
        3,
    ): "3. Heal injured monks or party members during the chaos, ensuring they can survive and assist in restoring order.",
    (
        14,
        4,
    ): "4. Probe the minds of the corrupted monks to understand their motives, reveal the extent of the spirits’ influence, or find out how to calm or banish the spirits.",
    (
        14,
        5,
    ): "5. Create a protected zone to shield the monks or the relic from the spirits’ attacks, giving the party a safe base to operate from.",
    (
        14,
        6,
    ): "6. Bolster an ally’s combat effectiveness to quickly subdue a powerful spirit or break through the defenses of the corrupted monks in a key moment.",
    (
        14,
        7,
    ): "7. Enable the party to coordinate telepathically while navigating the chaotic temple, sharing critical information instantly to outmaneuver the spirits and corrupted monks.",
    (
        15,
        1,
    ): "1. Revitalize the village’s withering crops, showing the villagers that harmony with nature can provide for their needs and reduce the desperation fueling their aggression.",
    (
        15,
        2,
    ): "2. Seek guidance from higher powers to determine how to appease the storm spirit, repair the grove, or prevent future disasters.",
    (
        15,
        3,
    ): "3. Enhance the armor of a party member or ally tasked with mediating or defending the shrine, preparing them for any potential conflict with aggressive villagers or wild weather effects.",
    (
        15,
        4,
    ): "4. Weaken a particularly stubborn or aggressive villager leader planning to destroy the shrine, dissuading them from escalating the conflict.",
    (
        15,
        5,
    ): "5. Reach the storm spirit’s shrine or sacred grove, which is now surrounded by treacherous terrain due to storms and floods, allowing the party to offer reparations or negotiate.",
    (
        15,
        6,
    ): "6. Summon a Hippogriff to create a harmless distraction, diverting the angry villagers away from the shrine or giving the party time to act.",
    (
        15,
        7,
    ): "7. Demonstrate the power of nature by calling down lightning to show the villagers the storm spirit’s might, intimidating them into ceasing their attack or using it to target specific aggressors non-lethally.",
    (
        16,
        1,
    ): "1. Allow the entire party to dive underwater and explore the sea creature’s territory or infiltrate the raiders’ submerged cave undetected.",
    (
        16,
        2,
    ): "2. Take control of the sea creature, overriding the raiders’ influence to stop its attacks and potentially turn it against its former masters.",
    (
        16,
        3,
    ): "3. Disrupt the raiders’ movements by creating a storm in their underwater cave, causing chaos and hindering their visibility and coordination.",
    (
        16,
        4,
    ): "4. Raise skeletal guardians from shipwrecks or underwater remains to assist in combating the raiders or defending the town against further attacks.",
    (
        16,
        5,
    ): "5. Bolster the party’s abilities and weaken the raiders, ensuring a successful infiltration or giving the group an edge in underwater combat.",
    (
        16,
        6,
    ): "6. Seal off dangerous tunnels in the raiders’ lair, create barriers to protect the sea creature from harm, or craft a way to block their escape routes.",
    (
        16,
        7,
    ): "7. Protect the party from potential divine magic the raiders might use after uncovering that the raiders want to scare of the town people because they used an evil artifact to become wealthy.",
    (
        17,
        1,
    ): "1. Put enchanted constructs or corrupted wildlife to sleep, neutralizing threats without destroying them, especially if they are innocent creatures under the spirit’s control.",
    (
        17,
        2,
    ): "2. Protect the party from the malevolent spirit’s influence, such as possession, fear effects, or mind-control attempts, while exploring the manor.",
    (
        17,
        3,
    ): "3. Use a spell to target and damage the malevolent spirit or its undead minions, exploiting their vulnerability to radiant energy.",
    (
        17,
        4,
    ): "4. Spy on specific areas of the manor to locate survivors, identify hidden threats, or eavesdrop on the spirit’s plans to better prepare for encounters.",
    (
        17,
        5,
    ): "5. Enhance a party member’s combat capabilities when facing particularly dangerous enemies, ensuring they can overpower the spirit’s constructs or minions in a critical moment.",
    (
        17,
        6,
    ): "6. Shield the party from elemental damage caused by traps or magical effects in the manor, such as fiery wards or lightning-based curses.",
    (
        17,
        7,
    ): "7. Break the curses on villagers found alive, deactivate dangerous magical traps, or weaken the spirit’s control over the manor, making it easier to confront and banish.",
    (
        18,
        1,
    ): "1. Channel divine energy to inspire awe and bolster the party’s ability to resist the demonic influence in the crypt. The spell may also help in negotiations with neutral or holy entities encountered along the way.",
    (
        18,
        2,
    ): "2. Shield the party from traps or attacks in the crypt that deal elemental damage, such as fiery glyphs or lightning-charged runes.",
    (
        18,
        3,
    ): "3. Interrogate the spirit of a deceased guardian or intruder within the crypt to gain information about the relic’s hiding place, the traps’ nature, or the thief’s motives.",
    (
        18,
        4,
    ): "4. Destroy undead sentinels or damage fiendish guardians protecting the relic, using radiant energy to deal significant damage to these dark forces.",
    (
        18,
        5,
    ): "5. Strengthen the party’s combat effectiveness and skill checks while weakening their enemies, ensuring an edge during crucial encounters in the crypt.",
    (
        18,
        6,
    ): "6. Protect the party from being tracked or observed by the demonic wards or any fiendish agents keeping an eye on the crypt, allowing for a stealthier approach.",
    (
        18,
        7,
    ): "7. Enhance the armor of the party’s frontline members, ensuring their durability in combat against the crypt’s physical and magical defenses.",
    (
        19,
        1,
    ): "1. Use magic to traverse the mountain terrain and bypass icy obstructions or crevasses created by the frost giant’s storms, allowing the party to reach the hostages or confront the giant directly.",
    (
        19,
        2,
    ): "2. Use strong magic to subdue the frost giant’s evil-aligned minions, such as trolls or dark fey, who are aiding in the siege.",
    (
        19,
        3,
    ): "3. Protect key party members or villagers from the frost giant’s magical attacks, such as icy enchantments or frost spells, ensuring they remain effective in the rescue.",
    (
        19,
        4,
    ): "4. Communicate directly with the frost giant, bypassing language barriers to negotiate peace or explain the true origins of the artifact, avoiding unnecessary bloodshed.",
    (
        19,
        5,
    ): "5. Enable the party to navigate through snowdrifts, icy restraints, or magical freezing effects without hindrance, ensuring they can act decisively in combat or rescue efforts.",
    (
        19,
        6,
    ): "6. Call upon a Mephit to aid in distracting the giant, protecting the villagers, or reinforcing the party during critical combat encounters.",
    (
        19,
        7,
    ): "7. Counteract the frost giant’s weather manipulation or create a controlled area of ice to neutralize its minions by making terrain hazardous to them.",
    (
        20,
        1,
    ): "1. Create magical barriers to cut off reinforcements within the fortress, defend the rebels during a skirmish, or destroy siege equipment controlled by the baron’s forces.",
    (
        20,
        2,
    ): "2. Protect the party or a key rebel leader from harmful spells cast by the baron or his ritualists, ensuring their safety during critical moments.",
    (
        20,
        3,
    ): "3. Disrupt the fortress’s defenses or scatter guards stationed on battlements, providing the rebels or party with a tactical advantage.",
    (
        20,
        4,
    ): "4. Identify the spy within the rebel group by confronting suspects and exposing the traitor, restoring trust and preventing further sabotage.",
    (
        20,
        5,
    ): "5. Use the divine force of a spell to condemn the baron’s followers, weakening their resolve and possibly turning some away from his cause.",
    (
        20,
        6,
    ): "6. Block key escape routes within the fortress or create deadly traps to delay the baron’s retreat and hinder his forces during an assault.",
    (
        20,
        7,
    ): "7. Target Paladin enforcers, exploiting their good alignment to deal significant damage and disrupt their preparations for the summoning.",
    (
        21,
        1,
    ): "1. Take control of the aggressive plants, halting their attacks or using them to clear paths and protect the party while navigating the grove.",
    (
        21,
        2,
    ): "2. Enhance the party’s speed and reflexes to evade attacks from the animated plants, dodge environmental hazards, or quickly rescue the children.",
    (
        21,
        3,
    ): "3. Target with a powerful spell the corrupted druid, who is now evil-aligned due to the artifact’s influence, and any evil-aligned creatures guarding the artifact.",
    (
        21,
        4,
    ): "4. Use a spell to affect the food of the druid’s animal allies or guardians killing them in the process, turning that way the tide in combat against overwhelming numbers.",
    (
        21,
        5,
    ): "5. Deliver a decisive strike to the druid or corrupted forest creatures in close combat, neutralizing major threats quickly.",
    (
        21,
        6,
    ): "6. Protect party members from the entangling vines and roots controlled by the druid, ensuring they can move freely through the grove.",
    (
        21,
        7,
    ): "7. Empower a non-spellcasting ally, such as a fighter, with specific spells, allowing them to contribute in vital moments.",
    (
        22,
        1,
    ): "1. Use a spell to redirect or temporarily halt the floodwaters, buying time to reach the cult’s hidden ritual site or prevent the town from being completely submerged.",
    (
        22,
        2,
    ): "2. Protect key individuals, such as innocent civilians or the party’s spellcasters, from the rising waters or combat hazards while traversing dangerous areas of the town.",
    (
        22,
        3,
    ): "3. Gain insight into the cult’s plans, find the location of the ritual site, or learn the precise steps needed to stop the ritual, using divine guidance.",
    (
        22,
        4,
    ): "4. Shield the party or any civilians from death effects caused by the magical flood, such as drowning or curse-based death magic employed by the cultists.",
    (
        22,
        5,
    ): "5. Unleash divine judgment on the cultists, weakening their resolve, dealing damage, and disrupting their rituals. This could help to destabilize their control over the dam’s magic.",
    (
        22,
        6,
    ): "6. Disorient the cultists who are conducting the ritual or any defenders they have stationed at the dam, causing chaos and making it easier for the party to stop the ritual.",
    (
        22,
        7,
    ): "7. Empower a party member, especially a melee combatant, to deal devastating blows to the cultists, stop the ritual, or break any magical wards around the dam.",
    (
        23,
        1,
    ): "1. Create a terrifying illusion that preys on the necromancer’s greatest fears, either distracting them or weakening their resolve while the party advances.",
    (
        23,
        2,
    ): "2. Locate the necromancer within the vast underground library, bypassing any illusions or concealments they’ve used to hide their whereabouts.",
    (
        23,
        3,
    ): "3. Disrupt the necromancer’s summoned undead or magical guardians, dealing significant damage and possibly stunning or disorienting them, giving the party an edge in combat.",
    (
        23,
        4,
    ): "4. Seek divine guidance on the best course of action, uncover hidden traps, or find out where the scholars are held and how to safely disable any wards or curses the necromancer has placed.",
    (
        23,
        5,
    ): "5. Teleport past magical barriers or into rooms that are otherwise unreachable, such as the necromancer's private chambers or the hidden vaults containing the forbidden knowledge.",
    (
        23,
        6,
    ): "6. Create tools, objects, or materials needed to solve environmental puzzles, repair damaged magical wards, or craft makeshift weapons or items to aid in the rescue and final confrontation.",
    (
        23,
        7,
    ): "7. Take control of one of the necromancer’s underlings, potentially turning them against their master or using them to open paths that would otherwise be blocked to the party.",
    (
        24,
        1,
    ): "1. Empower a party member’s weapon with divine power, granting them the ability to deal devastating damage to the cult leader and his followers, cutting through magical protections.",
    (
        24,
        2,
    ): "2. Call upon the fierce prehistoric creatures to aid in combat, providing distractions, flanking opportunities, or even forcing the cultists to retreat from powerful threats.",
    (
        24,
        3,
    ): "3. Heal grievous injuries sustained during the infiltration, ensuring that key party members are at full strength to face the cult leader and his elite defenders.",
    (
        24,
        4,
    ): "4. Protect the party from fire-based attacks, and potentially deal damage to nearby enemies, especially the cultists who rely on fire spells or traps to defend the fortress.",
    (
        24,
        5,
    ): "5. Enhance a party member's combat abilities, boosting their strength, attack rolls, and effectiveness in battle against the cult leader and his inner circle.",
    (
        24,
        6,
    ): "6. Disrupt the cultists’ ranks, causing confusion and chaos within their lines. This can break their focus, cause them to turn on each other, or create an opening for the party to strike.",
    (
        24,
        7,
    ): "7. Expose falsehoods or uncover hidden motives from the cult leader or his lieutenants, perhaps learning the true nature of the ritual or discovering a weakness in the cult’s plan that can be exploited.",
    (
        25,
        1,
    ): "1. Create a massive windstorm to disrupt the warlord’s forces, scattering archers, disabling siege engines, and making the terrain difficult for the attackers to traverse.",
    (
        25,
        2,
    ): "2. Protect key allies or monks from the warlord’s spellcasters, ensuring they can continue to fight without succumbing to magical attacks.",
    (
        25,
        3,
    ): "3. Arm a party member with a divine weapon capable of cutting through the warlord’s most powerful lieutenants or defending the sacred relic from direct threats.",
    (
        25,
        4,
    ): "4. Use this spell against the warlord or one of their most dangerous champions, eliminating a key threat to the monastery’s survival in a decisive strike.",
    (
        25,
        5,
    ): "5. Evacuate injured monks or civilians from the monastery to a safe location or transport the relic away from the besieged location to deny it to the warlord.",
    (
        25,
        6,
    ): "6. Confuse and disrupt the warlord’s forces by targeting commanders or groups of soldiers, sowing chaos in their ranks and reducing their coordination.",
    (
        25,
        7,
    ): "7. Establish instant communication between the party and the monks or within the party itself, enabling swift coordination during the chaotic defense or counteroffensive.",
    (
        26,
        1,
    ): "1. Protect against the pirates’ physical and fire-based attacks during the town’s defense, dealing damage to melee attackers and surviving longer in battle.",
    (
        26,
        2,
    ): "2. Quickly travel through the druidic grove to outmaneuver the captain’s forces, bypass traps, and reach the artifact before the pirates realize the party is there.",
    (
        26,
        3,
    ): "3. Bolster the durability of a key party member or an important NPC defender in the town, ensuring they can survive critical moments in the siege.",
    (
        26,
        4,
    ): "4. Reveal hidden enemies or illusions created by Ragnar’s sorcerers, as well as locating the exact position of the artifact within the grove if it is concealed.",
    (
        26,
        5,
    ): "5. Enhance your size, strength, and defenses, turning you into a formidable force capable of taking on Ragnar or his elite crew in direct combat.",
    (
        26,
        6,
    ): "6. Call forth a sea cat to attack the pirates’ ships, disrupt their boarding parties, or aid in the underwater retrieval of treasure or stolen supplies.",
    (
        26,
        7,
    ): "7. Neutralize the captain or his lieutenants by preventing their movement, cutting off their ability to command their forces effectively or escape with the artifact.",
    (
        27,
        1,
    ): "1. Use a spell to block advancing forces from either side, creating natural barriers that limit damage to the valley and give the party time to negotiate.",
    (
        27,
        2,
    ): "2. Erect an impenetrable barrier to protect the Crystal Nexus from either side’s attacks or to separate key leaders from their forces during critical moments.",
    (
        27,
        3,
    ): "3. Target the Silver Flame’s divine casters or disrupt their enchantments, weakening their magical hold over the battlefield and balancing the conflict.",
    (
        27,
        4,
    ): "4. Strike a decisive blow against key groups of combatants or destroy corrupted creatures drawn to the Nexus by the entity’s growing power.",
    (
        27,
        5,
    ): "5. Free key leaders or individuals from curses, compulsions, or enchantments that the sealed entity may have used to manipulate the conflict.",
    (
        27,
        6,
    ): "6. Seal off dangerous areas near the Nexus or block further access to the entity’s resting place until the conflict can be resolved.",
    (
        27,
        7,
    ): "7. Target the Wildwood Pact’s summoners or neutralize protective enchantments they’ve placed around their forces, balancing the scales of the battle.",
    (
        28,
        1,
    ): "1. Turn the spirit’s own weapon against her forces, using a spell to break apart her icy constructs or clear paths through the thick snow blocking the city’s escape routes.",
    (
        28,
        2,
    ): "2. Ask the gods or higher powers for guidance on how to end the curse, whether by finding Eira’s lair, understanding her grievances, or identifying the artifact binding her power.",
    (
        28,
        3,
    ): "3. Heal the city’s afflicted citizens, alleviating the physical toll of the curse and giving the party allies to assist in their quest.",
    (
        28,
        4,
    ): "4. Communicate directly with Eira or her elemental minions, enabling negotiation to discover whether she can be appeased instead of defeated.",
    (
        28,
        5,
    ): "5. Purify the city of harmful magical blizzards or mists conjured by Eira, ensuring that the cursed lethargy doesn’t worsen for the survivors.",
    (
        28,
        6,
    ): "6. Lift the curse afflicting the citizens of the city or dispel powerful wards protecting Eira’s glacier sanctum.",
    (
        28,
        7,
    ): "7. Protect the party from Eira’s icy magical attacks or shield an ally crucial to breaking the curse.",
    (
        29,
        1,
    ): "1. Target Ellis or a key lieutenant of the spirit with vivid nightmares to disrupt their rest and weaken their resolve, sowing doubt or slowing their plans.",
    (
        29,
        2,
    ): "2. Gather critical information about the spirit’s location, its defenses, and the layout of the forest, allowing the party to navigate the mists effectively.",
    (
        29,
        3,
    ): "3. Enhance yourself with divine power, preparing you to confront the spirit in its physical form or to endure the hazards of the cursed forest.",
    (
        29,
        4,
    ): "4. Pierce the illusions and magical disguises concealing the spirit’s lair or its minions, ensuring that the party can locate and confront the spirit directly.",
    (
        29,
        5,
    ): "5. Damage the spirit’s corrupted plant minions during combat, clearing the way for the party to reach the heart of its domain.",
    (
        29,
        6,
    ): "6. Protect the party or Willowshade from the spirit’s ability to scry and prepare for their movements, enabling them to plan an effective counterattack.",
    (
        29,
        7,
    ): "7. Deliver divine retribution on the sprit and its corrupted surroundings, destroying its physical manifestations and purging its influence from the forest.",
    (
        30,
        1,
    ): "1. Empower yourself to stand against the otherworldly might of the two Heralds, leveling the playing field in physical combat.",
    (
        30,
        2,
    ): "2. Banish the Herald of Malevolence back to its plane or strip it of protective enchantments, weakening its influence in the temple.",
    (
        30,
        3,
    ): "3. Temporarily separate combatants, protect civilians trapped in the chaos, or create barriers to restrict the movement of enemies.",
    (
        30,
        4,
    ): "4. Summon swarms of rats to overwhelm minions or disrupt Verik Callan’s control over the temple’s infrastructure, creating chaos that the party can exploit.",
    (
        30,
        5,
    ): "5. Banish the Herald of Chaos or counter its magic, eliminating a significant threat and restoring balance to the temple.",
    (
        30,
        6,
    ): "6. Construct temporary barricades, tools, or even a replica of a sacred artifact to aid in negotiations or battles within the temple.",
    (
        30,
        7,
    ): "7. Issue a powerful magical command to a group of combatants or worshippers, compelling them to halt their actions, flee, or follow a specific directive.",
    (
        31,
        1,
    ): "1. Clear groups of undead minions with lightning or attack multiple enchanted constructs guarding the keep simultaneously, weakening the lich’s defenses.",
    (
        31,
        2,
    ): "2. Create a protective zone to prevent waves of undead from overwhelming the party while they regroup, plan, or concentrate on disarming traps.",
    (
        31,
        3,
    ): "3. Protect the party’s melee combatants from the physical attacks of the lich’s undead warriors, reducing their damage output and ensuring survivability.",
    (
        31,
        4,
    ): "4. Raise an undead servant to infiltrate the fortress, act as a spy, or even fight against the lich’s forces, exploiting the lich’s reliance on undead.",
    (
        31,
        5,
    ): "5. Remove the lich’s magical wards, disable traps, or counter his protective enchantments during the final confrontation.",
    (
        31,
        6,
    ): "6. Use a spell to create an illusory decoy, allowing the party to evade undead patrols or distract the lich while they sabotage the ritual.",
    (
        31,
        7,
    ): "7. Set up a deadly defensive perimeter to cut off reinforcements during the final battle or to destroy undead minions as they approach.",
    (
        32,
        1,
    ): "1. Use explosive fire acorns or berries to destroy barriers, deal significant damage to Zarvok and his minions, or create traps for approaching enemies.",
    (
        32,
        2,
    ): "2. Learn critical details about Zarvok’s weaknesses, the ancient monastery’s defenses, or the key to calming the volcano’s fury, providing the party with crucial insights.",
    (
        32,
        3,
    ): "3. Counter the fire elementals’ heat-based attacks, freeze magma flows temporarily, or weaken Zarvok by exploiting his vulnerability to cold damage.",
    (
        32,
        4,
    ): "4. Navigate through the treacherous volcanic tunnels and traps to reach Zarvok’s inner sanctum efficiently, avoiding unnecessary dangers.",
    (
        32,
        5,
    ): "5. Enhance a party member with divine fire, allowing them to resist heat damage and fight effectively in the elemental lord’s fiery domain.",
    (
        32,
        6,
    ): "6. Bolster the party’s morale, grant immunity to fear, and increase their resilience to Zarvok’s fiery attacks and the oppressive heat of the volcano.",
    (
        32,
        7,
    ): "7. Compel a captured servant of Zarvok, or even one of the surviving monks under his sway, to assist the party or provide vital information about Zarvok’s plans.",
    (
        33,
        1,
    ): "1. Receive visions that reveal the artifact’s location within the undercrofts, including key details about Darian’s defenses and traps.",
    (
        33,
        2,
    ): "2. Neutralize the chaotic magical effects in a specific area, allowing the party to traverse unstable sections of the undercrofts or confront Darian without his magical arsenal.",
    (
        33,
        3,
    ): "3. Turn nearby mundane objects into allies to fight off magical creatures or navigate the dangerous undercrofts without directly exposing the party to threats.",
    (
        33,
        4,
    ): "4. Compel an informant, a captured henchman of Darian, or even a reluctant city official to provide assistance or reveal critical information about Darian’s plans and the vault.",
    (
        33,
        5,
    ): "5. Efficiently navigate the labyrinthine undercrofts, bypassing traps and hazards to reach the artifact quickly.",
    (
        33,
        6,
    ): "6. Protect the party from physical attacks by rogue constructs, magical creatures, or collapsing parts of the undercroft during their exploration.",
    (
        33,
        7,
    ): "7. Animate a powerful undead servant to act as a guardian, guide, or combat ally while delving into the perilous undercrofts.",
    (
        34,
        1,
    ): "1. Neutralize Mordavix’s summoned elementals or delay reinforcements by creating a debilitating area that slows enemies and deals ongoing damage.",
    (
        34,
        2,
    ): "2. Defeat Mordavix’s weaker minions or banish summoned creatures with a single divine utterance, clearing a path to the central spire.",
    (
        34,
        3,
    ): "3. Protect an ally from death, ensuring they can survive the dangers of the storm-ridden city and the climactic confrontation with Mordavix.",
    (
        34,
        4,
    ): "4. Create a safe teleportation point for civilians or key party members to escape to if the situation becomes too dangerous.",
    (
        34,
        5,
    ): "5. Paralyze or outright banish Mordavix’s chaotic or evil allies, turning the tide of the battle in the party’s favor.",
    (
        34,
        6,
    ): "6. Dispatch an invisible creature to bypass the storm and Mordavix’s defenses, potentially stealing a key artifact or sabotaging his plans.",
    (
        34,
        7,
    ): "7. Take control of the storm, calming its worst effects temporarily, buying the party precious time to act without the city’s levitation crystals failing.",
    (
        35,
        1,
    ): "1. Use a spell to temporarily calm or manipulate the corrupted plants in the area, preventing them from attacking or restricting movement or even manipulate plant-based traps set by Talvorn.",
    (
        35,
        2,
    ): "2. Call upon an ancient sea creature to help clear the land of Talvorn’s summoned monsters or to engage in combat with the druid’s powerful allies, especially those in or near bodies of water. ",
    (
        35,
        3,
    ): "3. Empower yourself with divine grace, providing you with enhanced charisma and leadership abilities to rally the remaining fey and creatures of the forest.",
    (
        35,
        4,
    ): "4. Use a huge light burst to deal massive radiant damage to Talvorn and his monstrous minions, purging the corruption and wounding the druid’s allies. It could also heal the corrupted land around the Heart of the Vale.",
    (
        35,
        5,
    ): "5. Trigger a powerful earthquake to disrupt Talvorn’s ritual, shake his defenses, and create openings for the party to advance or destroy his hideouts. The tremors could destabilize his magical wards or bring down parts of the corrupted forest around him.",
    (
        35,
        6,
    ): "6. Use a spell to drive Talvorn’s followers mad or incapacitate his minions, breaking their concentration or loyalty long enough to break his hold over them. This spell could also disorient the creatures in the forest and disrupt their attacks.",
    (
        35,
        7,
    ): "7. Protect key members of the party from Talvorn’s attempts to influence their minds or plant illusions, ensuring they remain focused and immune to his mental manipulation. It could also block any psychic defenses Talvorn might have set up.",
    (
        36,
        1,
    ): "1. Use a spell to channel the divine power of the goddess, invoking her presence to bolster your resolve and courage, making you stronger. The Visage can also intimidate Varolath’s minions, granting the party an edge in their confrontation with the beast.",
    (
        36,
        2,
    ): "2. Transform the party into mist-like forms to bypass the temple's dangerous traps and patrolling lycanthropes. This spell allows for quick movement, enabling the party to avoid detection or make a surprise attack on Varolath.",
    (
        36,
        3,
    ): "3. Restore the party’s health after fighting through Varolath’s monstrous minions or recovering from the temple's cursed environment. This can be used to counter the debilitating effects of the blood moon's influence, allowing the party to endure longer against Varolath’s attacks.",
    (
        36,
        4,
    ): "4. Curse Varolath with the very lycanthropy he has so ruthlessly used to empower himself. This curse could prevent him from fully controlling his beast form, making him vulnerable to attacks.",
    (
        36,
        5,
    ): "5. Call upon divine power to strengthen a chosen ally in the battle against Varolath. This pact could give them divine resilience, allowing them to fight through the curse's influence and resist Varolath’s powerful lycanthropic abilities.",
    (
        36,
        6,
    ): "6. Create an illusion of the party, allowing them to deceive Varolath and his minions or create distractions. This can help the party enter the temple unnoticed or confuse Varolath, giving them a tactical advantage in their battle.",
    (
        36,
        7,
    ): "7. Use a powerful field to negate Varolath’s magical abilities, weakening his supernatural enhancements. The antimagic field can disrupt the blood moon’s effect on him, rendering him more vulnerable and preventing him from using any magical protections or lycanthropic enhancements.",
    (37, 1): "Human",
    (37, 2): "Dwarf",
    (37, 3): "Elf",
    (37, 4): "Gnome",
    (37, 5): "Half-elf",
    (37, 6): "Half-orc",
    (37, 7): "Hafling",
    (38, 1): "Barbarian",
    (38, 2): "Bard",
    (38, 3): "Cleric",
    (38, 4): "Druid",
    (38, 5): "Fighter",
    (38, 6): "Monk",
    (38, 7): "Paladin",
    (38, 8): "Ranger",
    (38, 9): "Rogue",
    (38, 10): "Arcane Spellcaster",
    (39, 1): "Lawful Good",
    (39, 2): "Neutral Good",
    (39, 3): "Chaotic Good",
    (39, 4): "Lawful Neutral",
    (39, 5): "True Neutral",
    (39, 6): "Chaotic Neutral",
    (39, 7): "Lawful Evil",
    (39, 8): "Neutral Evil",
    (39, 9): "Chaotic Evil",
}


# ready
class QuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Application")
        self.root.geometry("1600x960")

        self.extra_answers = []
        self.answer = []
        self.row = 2
        self.col = 0
        self.current_question = 1
        self.first_choice = None
        self.second_choice = None

        # Main question window
        self.question_frame = tk.Frame(self.root, width=1500, height=900)
        self.question_frame.grid(row=0, column=0, padx=40, pady=10, sticky="nsew")

        self.question_title = tk.Label(
            self.question_frame,
            text=f"Question {self.current_question}",
            font=("Arial", 24),
            anchor="center",
        )
        self.question_title.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
        self.question_label = tk.Label(
            self.question_frame,
            text=questions[self.current_question - 1],
            font=("Arial", 20),
            wraplength=1450,
            anchor="w",
            justify="left",
        )
        self.question_label.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")

        self.answer_buttons = []
        for key, value in answers.items():
            if key[0] == self.current_question:
                button = tk.Button(
                    self.question_frame,
                    text=value,
                    font=("Arial", 14),
                    width=65,
                    height=4,
                    wraplength=650,
                    anchor="center",
                    bg="SystemButtonFace",
                    command=lambda i=key[1]: self.select_answer(i),
                )
                button.grid(row=self.row, column=self.col, padx=5, pady=5, sticky="w")
                self.row += 1
                if self.row == 6:
                    self.row = 2
                    self.col = 1
                self.answer_buttons.append(button)

        self.next_button = tk.Button(
            self.question_frame,
            text="Next",
            bg="light gray",
            width=20,
            height=2,
            state=tk.DISABLED,
            command=self.next_question,
        )
        self.next_button.grid(row=7, column=0, columnspan=2, pady=(15, 10))

        self.root.mainloop()

    def select_answer(self, answer_index):
        if self.first_choice is None:
            self.first_choice = answer_index
            self.answer_buttons[answer_index - 1].configure(bg="green")
            self.next_button.configure(state=tk.NORMAL, bg="yellow")
        elif self.first_choice == answer_index:
            if self.second_choice is not None:
                self.first_choice = self.second_choice
                self.second_choice = None
                self.answer_buttons[answer_index - 1].configure(bg="SystemButtonFace")
            else:
                self.first_choice = None
                self.answer_buttons[answer_index - 1].configure(bg="SystemButtonFace")
                self.next_button.configure(state=tk.DISABLED, bg="SystemButtonFace")
        elif self.second_choice == answer_index:
            self.second_choice = None
            self.answer_buttons[answer_index - 1].configure(bg="SystemButtonFace")
        elif self.first_choice is not None and self.second_choice is None:
            self.second_choice = answer_index
            self.answer_buttons[answer_index - 1].configure(bg="green")
        elif self.first_choice != answer_index and self.second_choice != answer_index:
            print("Error")

    def calculate_points(self, first_choice, second_choice):
        self.answer.append([first_choice, second_choice])
        first_points = custom_points.get((self.current_question, first_choice), 6) * 2
        if second_choice is not None:
            second_points = custom_points.get((self.current_question, second_choice), 6)

        if self.current_question < 37:
            # Distribute points to multiple domains for the first choice
            first_domains = answer_domains[(self.current_question, first_choice)]
            for domain in first_domains:
                domain_points[domain] += first_points

            # Distribute points to multiple domains for the second choice
            if second_choice is not None:
                second_domains = answer_domains[(self.current_question, second_choice)]
                for domain in second_domains:
                    domain_points[domain] += second_points

        else:
            if self.current_question > 36:
                temp = answers[(self.current_question, first_choice)]
            self.extra_answers.append({temp: int(first_points / 2)})
        # self.update_graph()

    def update_graph(self):
        self.ax.clear()
        self.ax.bar(domain_points.keys(), domain_points.values(), color="skyblue")
        self.ax.set_xticklabels(domain_points.keys(), rotation=90)
        self.ax.set_title("Domain Points")
        self.figure.tight_layout()
        self.bar_chart.draw()

    def next_question(self):
        self.calculate_points(self.first_choice, self.second_choice)
        if self.current_question == NUM_QUESTIONS:
            self.show_final_results()
            return

        self.current_question += 1
        self.first_choice = None
        self.second_choice = None
        self.question_title.configure(text=f"Question {self.current_question}")
        self.question_label.configure(text=questions[self.current_question - 1])
        self.next_button.configure(state=tk.DISABLED, bg="SystemButtonFace")

        if self.current_question == 38:
            for i in range(3):
                button = tk.Button(
                    self.question_frame,
                    text="",
                    font=("Arial", 14),
                    width=65,
                    height=4,
                    wraplength=650,
                    anchor="center",
                    bg="SystemButtonFace",
                    command=lambda i=i: self.select_answer(8 + i),
                )
                if i == 0:
                    self.row = 6
                    self.col = 0
                button.grid(row=self.row, column=self.col, padx=5, pady=5, sticky="w")
                self.row += 1
                if self.row == 7:
                    self.row = 5
                    self.col = 1
                self.answer_buttons.append(button)
        if self.current_question == 39:
            self.answer_buttons[9].destroy()
            self.answer_buttons.pop()

        for i, button in enumerate(self.answer_buttons):
            button.configure(
                text=answers[self.current_question, i + 1],
                bg="SystemButtonFace",
            )

    def get_god_title(self, god_name):
        return gods_by_title.get(god_name, "God not found")

    def show_frame_2(self, sorted_gods):
        self.question_frame.destroy()

        first_three = list(itertools.islice(sorted_gods.items(), 3))

        self.question_frame = tk.Frame(self.root, width=1500, height=250)
        self.question_frame.pack(side=tk.TOP, padx=5, pady=10)

        for i, (god, value) in enumerate(first_three):
            if (
                i == 0
                and first_three[0][1] == first_three[1][1]
                and first_three[0][1] == first_three[2][1]
            ):
                self.question_title = tk.Label(
                    self.question_frame,
                    text=f"Your preferred Gods are {first_three[0][0]}, {first_three[1][0]} and {first_three[2][0]}. They are {self.get_god_title(first_three[0][0])}, {self.get_god_title(first_three[1][0])} and {self.get_god_title(first_three[2][0])}",
                    font=("Arial", 24),
                    wraplength=1000,
                    anchor="w",
                    justify="left",
                )
                self.question_title.pack(pady=20)
            if (
                i == 0
                and first_three[0][1] == first_three[1][1]
                and first_three[0][1] != first_three[2][1]
            ):
                self.question_title = tk.Label(
                    self.question_frame,
                    text=f"Your preferred Gods are {first_three[0][0]} and {first_three[1][0]}. They are {self.get_god_title(first_three[0][0])}, {self.get_god_title(first_three[1][0])} and {self.get_god_title(first_three[2][0])}",
                    font=("Arial", 24),
                    wraplength=1400,
                    anchor="w",
                    justify="left",
                )
                self.question_title.pack(pady=20)
            if i == 0 and first_three[0][1] != first_three[1][1]:
                self.question_title = tk.Label(
                    self.question_frame,
                    text=f"Your preferred God is {self.get_god_title(first_three[0][0])}, {first_three[0][0]},",
                    font=("Arial", 24),
                    wraplength=1400,
                    anchor="w",
                    justify="left",
                )
                self.question_title.pack(pady=(20, 0))
            if i == 1 and first_three[0][1] != first_three[1][1]:
                self.question_title = tk.Label(
                    self.question_frame,
                    text=f"other good choices for you are {self.get_god_title(first_three[1][0])}, {first_three[1][0]} and {self.get_god_title(first_three[2][0])}, {first_three[2][0]}",
                    font=("Arial", 22),
                    wraplength=1400,
                    anchor="w",
                    justify="left",
                )
                self.question_title.pack(pady=(5, 20))

        # Domain points graph window
        self.graph_frame = tk.Frame(self.root, width=1500, height=700)
        self.graph_frame.pack(side=tk.BOTTOM, padx=5, pady=5)

        self.figure, self.ax = plt.subplots(figsize=(12, 6))
        self.bar_chart = FigureCanvasTkAgg(self.figure, self.graph_frame)
        self.bar_chart.get_tk_widget().pack()
        self.update_graph()

    def show_final_results(self):
        desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop", "answers.txt")
        god_points = {}
        domain_dict = {}
        grouped_value = defaultdict(list)

        for key, value in domain_points.items():
            grouped_value[value].append(key)

        sorted_grouped_dict = dict(
            sorted(grouped_value.items(), key=lambda item: item[0], reverse=True)
        )

        # messagebox.showinfo("Final Results", f"Top Domain(s):\\n{result_text}")
        largest_seven = list(sorted_grouped_dict.items())[:6]

        final_domains = str(largest_seven)

        updated_values = [10, 7, 5, 3, 2, 1]

        for i in range(len(largest_seven)):
            value, keys = largest_seven[i]
            largest_seven[i] = updated_values[i], keys

        for points, domains in largest_seven:
            for domain in domains:
                domain_dict[domain] = points

        for god, domains in gods_by_domains.items():
            total_points = 0
            for domain in domains:
                if domain in domain_dict:
                    total_points += domain_dict[domain]
            god_points[god] = total_points

        sorted_god_points = dict(
            sorted(god_points.items(), key=lambda item: item[1], reverse=True)
        )

        for i, entry in enumerate(self.extra_answers):
            for god, points in entry.items():
                if i == 0:
                    for god_name, races in gods_by_race.items():
                        if god in races:
                            sorted_god_points[god_name] += points
                elif i == 1:
                    for god_name, classes in gods_by_class.items():
                        if god in classes:
                            sorted_god_points[god_name] += points
                elif i == 2:
                    for god_name, alignment in gods_by_alignment.items():
                        if god == alignment:
                            sorted_god_points[god_name] += points

        sorted_god_points = dict(
            sorted(sorted_god_points.items(), key=lambda item: item[1], reverse=True)
        )

        with open(desktop_path, "w") as file:
            file.write(str(self.answer) + "\n")
            file.write(final_domains + "\n")
            file.write(str(sorted_god_points))

        self.show_frame_2(
            sorted_god_points,
        )

        # self.root.destroy()


if __name__ == "__main__":
    QuizApp()
