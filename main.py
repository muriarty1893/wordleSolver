import nltk
from nltk.corpus import words, wordnet
from input_handler import get_user_input
from word_filter import filter_wordlist

pattern, must_include, must_not_include, excluded_positions = get_user_input()
word_length = len(pattern)

nltk_words = words.words()
filtered_nltk = set(filter_wordlist(nltk_words, word_length, pattern, must_include, must_not_include, excluded_positions))

wordnet_words = set()
for syn in wordnet.all_synsets():
    for lemma in syn.lemmas():
        wordnet_words.add(lemma.name().lower())
filtered_wordnet = set(filter_wordlist(wordnet_words, word_length, pattern, must_include, must_not_include, excluded_positions))

filtered_words_txt = set()
with open('words.txt', 'r') as f:
    words_txt = [line.strip().lower() for line in f]
    filtered_words_txt = set(filter_wordlist(words_txt, word_length, pattern, must_include, must_not_include, excluded_positions))

common_words = filtered_nltk & filtered_wordnet & filtered_words_txt

print(f"{len(common_words)} common words found:\n")
for w in sorted(common_words):
    print(w)