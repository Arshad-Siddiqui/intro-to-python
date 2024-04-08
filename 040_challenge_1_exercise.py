# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  long_words = filter_short_words(words)

  pass

def filter_short_words(words):
  shortened_words = []
  for word in words:
    if len(word) >= 10:
      shortened_words.append(word)
  return shortened_words

def transform_longer_words(words):
  transformed_words = []
  for word in words:
    if len(word) > 15:
      transformed_words.append(word[0:15] + "...")
    else:
      transformed_words.append(word)
  return transformed_words

def filter_hyphens(words):
  no_hyphens = []
  for word in words:
    if '-' not in word:
      no_hyphens.append(word)
  return no_hyphens

check_that_these_are_equal(
  transform_longer_words([
    'longlongwordword',
    'megalongwordwordword'
  ]
  ), ['longlongwordwor...',
      'megalongwordwor...']
)

check_that_these_are_equal(
  filter_short_words([
    'banana',
    'fred',
    'megalongwordwordword',
    'key'
  ]), [
    'megalongwordwordword',
  ]
)

check_that_these_are_equal(
  filter_hyphens([
    "fred",
    "bob",
    "fr-ed",
    "b-ob",
  ]), ["fred", "bob"]
)
check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
