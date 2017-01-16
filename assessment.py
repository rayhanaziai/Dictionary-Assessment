"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_count = {}
    separated_words = phrase.split(" ")
    for word in separated_words:
        quantity = word_count.get(word, 0) + 1
        word_count[word] = quantity
    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_and_prices = {"Watermelon": 2.95, "Cantaloupe": 2.50, "Musk": 3.25, "Christmas": 14.25}
    return melon_and_prices.get(melon_name, "No price found")


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    dict_of_lengths = {}
    for word in words:
        length = len(word)
        if length in dict_of_lengths:
            dict_of_lengths[length].append(word)
        else:
            dict_of_lengths[length] = [word]
        dict_of_lengths[length].sort()

    result = []
    for length, words in dict_of_lengths.items():
        result.append((length, words))
    return sorted(result)


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_to_pirate = {"sir": "matey", "hotel": "fleabag inn", "student": "swabbie", "man": "matey", "professor": "foul blaggart", "restaurant": "galley", "your": "yer", "excuse": "arr", "students": "swabbies", "are": "be", "restroom": "head", "my": "me", "is": "be"}

    english_words = phrase.split(" ")
    pirate_words = []

    for word in english_words:
        if word in english_to_pirate:
            pirate_words.append(english_to_pirate[word])
        else:
            pirate_words.append(word)

    pirate_phrase = " ".join(pirate_words)

    return pirate_phrase


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    first_and_last = {}

    # Loop through words and put first letter of each word as a key, and full words as values
    for word in names:
        first_letter = word[0].lower()
        if first_letter in first_and_last.keys():
            first_and_last[first_letter].append(word)
        else:
            first_and_last[first_letter] = [word]

    # Insert first name into a result list, and delete it from the dictionary
    game_result = [names[0]]
    for value in first_and_last.values():
        if names[0] in value:
            index_to_del = value.index(names[0])
            value.pop(index_to_del)

   # As long as the last letter of the word in our list has a key in our dictionary, find the next word from the value and then delete it from the dictionary
    while game_result[-1][-1] in first_and_last.keys():
        last_letter = game_result[-1][-1]
        game_result.append(first_and_last[last_letter][0])
        if len(first_and_last[last_letter]) == 1:
            del first_and_last[last_letter]
        else:
            first_and_last[last_letter].pop(0)
    return game_result


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
