import re

key_regex = re.compile('[^a-zA-Z]')
output_regex = re.compile('[^a-zA-Z ]')


def get_lookup_key(line):
    stripped_line = key_regex.sub('', line).lower()
    characters = [*stripped_line]
    characters.sort()
    return ''.join(characters)


def format_anagram(anagram):
    return output_regex.sub('', anagram)


def format_occurence_counts(key_lookup):
    output = ''
    occurence_counts = {}
    characters = [*key_lookup]
    for character in characters:
        if character not in occurence_counts:
            occurence_counts[character] = 0

        occurence_counts[character] += 1

    for character, occurence_count in occurence_counts.items():
        uppercase_character = character.upper()
        percetage = 100 * occurence_count / len(key_lookup)
        formatted_percetage = "{:,.2f}".format(percetage)
        output += f'{uppercase_character} - {str(occurence_count)}, {formatted_percetage}%\n'

    return output


def format_anagrams(lookup_key, anagram_set):
    output = '("'
    stripped_anagrams = [format_anagram(anagram) for anagram in anagram_set]
    formatted_anagrams = '", "'.join(stripped_anagrams)
    output += formatted_anagrams
    output += '")”\n'
    output += format_occurence_counts(lookup_key)

    return output


# Get file input and build a dictionary of anagrams
file_path = input('Please enter file path: ')
processed_anagrams = {}

file = open(file_path, 'r')

while True:
    line = file.readline()

    if not line:
        break

    lookup_key = get_lookup_key(line)

    if lookup_key not in processed_anagrams:
        processed_anagrams[lookup_key] = set()

    anagram_set = processed_anagrams[lookup_key]
    anagram_set.add(line)

# Print processed anagrams
for lookup_key, anagram_set in processed_anagrams.items():
    if len(anagram_set) > 1:
        formatted_anagrams = format_anagrams(lookup_key, anagram_set)
        print(formatted_anagrams)
