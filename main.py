#import random 
from random import randint
from game_data import data
from art import logo, vs
from replit import clear

def get_character():
  return data[randint(0, len(data)-1)]

def print_character(phrase, character):
  print(f"{phrase}: {character['name']}, a {character['description']}, from {character['country']}.")

def more_followers_character(character_a, character_b):
  if character_a['follower_count'] > character_b['follower_count']:
    return character_a
  else:
    return character_b

def print_higher_lower(characters, score):
  #Print Logo
  print(logo)
  if score > 0:
    print(f"You're right! Current score: {score}.")
  
  #print A
  print_character("Compare A", characters['A'])
  #print vs
  print(vs)
  #print B
  print_character("Against B", characters['B'])
  


#establish characters
characters = {
  'A': get_character(),
  'B': get_character()
}

#init score
score = 0
print_higher_lower(characters, score)
should_ask =True

while should_ask:
  #Ask who has more follower
  answer = input("Who has more followers? Type 'A' or 'B': ")
  clear()
  #if player is right score + 1
  if characters[answer] == more_followers_character(characters['A'],characters['B']):
    score += 1
    characters['A'] = characters['B']
    characters['B'] =  get_character()

    print_higher_lower(characters, score)

  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    should_ask = False
