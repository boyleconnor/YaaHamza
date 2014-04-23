from arabic.utils.constants import TASHKEEL


def search_pattern(word):
        return '^' + ''.join(['(%s[%s]*)' % (i, TASHKEEL) for i in word]) + '$'
