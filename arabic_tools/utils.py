from arabic_tools.constants import TASHKEEL


def search_pattern(word):
        return '^' + ''.join(['(%s[%s]*)' % (i, TASHKEEL) for i in word]) + '$'


def match_to_template():
    pass


def spelling_to_template(word, root=('ف', 'ع', 'ل')):
    word = str(word)
    if ' ' in word or type(word) != str:
        raise ValueError()
    for i, j in enumerate(root):
        word.replace(j, ('\\%s' % i))
    return word