file = open("./books/frankenstein.txt")
content = file.read()

def count_word(content):
  words = content.split()
  return len(words)

def count_character(content):
  character_dict = {}

  for character in content:
    lowered = character.lower()
    if str.isalpha(lowered):
      if lowered in character_dict:
        character_dict[lowered] += 1
      else:
        character_dict[lowered] = 1
      

  return character_dict

def print_report(character_dict, word_count):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in the document")

  for character in character_dict:
    print(f"The '{character}' character was found {character_dict[character]} times")
  
  print("--- End report ---")

word_count = count_word(content)
character_count_dict = count_character(content)

print_report(character_count_dict, word_count)
