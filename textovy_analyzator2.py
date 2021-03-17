#TITLE: A SIMPLE TEXT ANALYZER

#1. SETTING UP VARIABLES 
TEXTS = ["""
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.""",

"""At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.""",

"""The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present."""
]

registered_users = {'bob': 123, 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'} 
oddelovac = 40 * "-"

#2. LOGGING IN
#enter the user's login and password
user_id = input("Please enter your ID: ")
user_password = input("And now your password: ")
print(oddelovac)

#check id, password. If not in registered users, exit the program
if user_id in str(registered_users.keys()) and user_password == str(registered_users[user_id]):
        print(f"Welcome back {user_id.title()}!")
else:
    print("Sorry, you are not a registered user or your ID/password is incorrect. The program will be terminated...")
    exit()

#3. TEXTS CHOOSING. IF NOT IN GIVEN RANGE, EXIT THE PROGRAM
i = int(input(f"Please enter the number of the text you want to analyze (from 1 to {len(TEXTS)}): "))
if i not in range(1, len(TEXTS)+1) :
    print("Sorry, you chose a different text number. The program will be terminated...")
    exit()
else:
    print("Ok, let's continue!")
print(oddelovac)

#4. TEXT ANALYSIS
#text splitting
texts_database = {}
texts_database.setdefault(f"text{i}", TEXTS[i-1])
splitted_text = texts_database[f"text{i}"].split(" ")

#text stripping and words count
stripped_text = []
for word in splitted_text:
    stripped_word = word.strip("\n ,.:;")
    stripped_text.append(stripped_word)

words_count = len(stripped_text)

#titlecase words count
#uppercase and lowercase words count
#number count

titlecase_words = []
uppercase_words = []
lowercase_words = []
numbers = []

for word in stripped_text:
    if word[0].isupper() and word[0].isalpha():
        titlecase_words.append(word)
        titlecase_words_count = (len(titlecase_words))

    if word.isupper():
        uppercase_words.append(word)
        uppercase_words_count = (len(uppercase_words))
        
    if word.islower():
        lowercase_words.append(word)       
        lowercase_words_count = (len(lowercase_words))

    if word.isdigit():
        numbers.append(word)
        numbers_count = (len(numbers))

if titlecase_words == []:
    titlecase_words_count = 0
if uppercase_words == []:
    uppercase_words_count = 0
if lowercase_words == []:
    lowercase_words_count = 0
if numbers == []:
    numbers_count = 0

#sum of all numbers in the text
numbers_sum = sum([int(n) for n in numbers])

        
#5. OUTPUT
print(f"There are {words_count} words in the selected text.")
print(f"There are {titlecase_words_count} titlecase words.")
print(f"There are {uppercase_words_count} uppercase words.")
print(f"There are {lowercase_words_count} lowercase words.")
print(f"There are {numbers_count} numbers.")
print(f"The sum of all the numbers is {numbers_sum}.")

print(oddelovac)

#6. TABLE
#dictionary with len as keys and occurences as values 
delka_slov = []
for word in stripped_text:
    delka_slov.append(len(word))
delka_slov = set(delka_slov)

tabulka = dict.fromkeys(delka_slov, 0)

for key in tabulka:
    for word in stripped_text:
        if len(word) == key:
            tabulka[key] = tabulka.get(key) + 1

#table printing
print("LEN |   | OCCURENCES")
for key in tabulka:
    if key < 10:
        print(f"{key}   |   | {tabulka.get(key)}")
    else:
        print(f"{key}  |   | {tabulka.get(key)}")
