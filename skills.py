# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    unique_words = {}

    input_words = input_string.split(' ')

    for word in input_words:
        if word in unique_words.keys():
            unique_words[word] += 1
        else:
            unique_words[word] = 1

    return unique_words


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    # Why would you use a dictionary for this??? This seems like a really clunky way.
    # Is there a better way to do this that I'm missing?

    dict1 = {}
    dict2 = {}
    final_list = []

    # For each number in the list, if already in the dictionary, increment the value
    for num in list1:
        if dict1.get(num, 0) > 0:
            dict1[num] += 1
        else:
            dict1[num] = 1
    # print 'dict1: ', dict1

    for num in list2:
        if dict2.get(num, 0) > 0:
            dict2[num] += 1
        else:
            dict2[num] = 1
    # print 'dict2: ', dict2

    # Iterate through dict1 by key
    for key in dict1:
        # If key is also in dict2
        if dict2.get(key, 0) > 0:
            # Append the key to the final list as many times as the value
            # associated with dict1[key] or dict2[key], whichever is greater
            i = 0
            while i < dict2[key] or i < dict1[key]:
                final_list.append(key)
                i += 1

    # print 'final_list: ', final_list
    return final_list


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    # set1 = set()
    # set2 = set()

    # for word in list1:
    #     set1.add(word)

    # for word in list2:
    #     set2.add(word)

    # return list(set1.intersection(set2))

    dict1 = {}
    dict2 = {}
    final_list = []

    for num in list1:
        dict1[num] = 'in list'

    for num in list2:
        dict2[num] = 'in list'

    for key in dict1:
        if dict2.get(key, 0) == 'in list':
            final_list.append(key)

    return final_list


def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    num_dict = {}
    pair_list = []

    # For each number in input_list
    for num in input_list:
        # Iterate through input list again to compare each number to each
        # other number, including the number itself
        for x in input_list:
            # If the number plus the other number equals 0
            if num + x == 0:
                # and if the number is less than or equal to the other number
                # (so we don't end up with duplicate pairs)
                if num <= x:
                    # Add the numbers as a key, value pair
                    num_dict[num] = x
    # For each key value pair in num_dict, unpack the key and value and
    # add them as a nested list inside pair_list
    for key, value in num_dict.iteritems():
        pair_list.append([key, value])

    return pair_list


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    # I'm essentially just using the dictionary keys like a set. Is there a different way?

    words_dict = {}

    for word in words:
        words_dict[word] = 0

    return words_dict.keys()


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    encoding_map = {'e': 'p',
                    'a': 'd',
                    't': 'o',
                    'i': 'u'
                    }

    phrase_list = list(phrase)

    for i in range(len(phrase_list)):
            if phrase_list[i] in encoding_map.keys():
                phrase_list[i] = encoding_map[phrase_list[i]]

    phrase = ''.join(phrase_list)

    return phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    # If a word appears more than onece, should that word appear more than once
    # in the list of words of that length?
    word_dict = {}
    word_list = []

    for word in words:

        if word_dict.get(len(word), 0) != 0:
            word_dict[len(word)].append(word)
        else:
            word_dict[len(word)] = [word]

    # print word_dict

    for k, v in word_dict.iteritems():
        word_list.append((k, v))

    return word_list


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    translation_map = {
        'sir': 'matey',
        'hotel': 'fleabag inn',
        'student': 'swabbie',
        'boy': 'matey',
        'madam': 'proud beauty',
        'professor': 'foul blaggart',
        'restaurant': 'galley',
        'your': 'yer',
        'excuse': 'arr',
        'students': 'swabbies',
        'are': 'be',
        'lawyer': 'foul blaggart',
        'the': 'th\'',
        'restroom': 'head',
        'my': 'me',
        'hello': 'avast',
        'is': 'be',
        'man': 'matey'
    }

    phrase_list = phrase.split()
    for i in range(len(phrase_list)):
            if phrase_list[i] in translation_map.keys():
                phrase_list[i] = translation_map[phrase_list[i]]

    to_print = ' '.join(phrase_list)

    return to_print

# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    return ''


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
