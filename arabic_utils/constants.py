ROOT_LENGTHS = (3, 4)

FATHA = 'َ'

KASRA = 'ِ'

DAMMA = 'ُ'

SHADDA = 'ّ'

SUKUN = 'ْ'

TASHKEEL = FATHA + KASRA + DAMMA + SHADDA + SUKUN

FATHAN = 'ً'

KASRAN = 'ٍ'

DAMMAN = 'ٌ'

TANWEEN = FATHAN + KASRAN + DAMMAN

DIACRITICS = TASHKEEL + TANWEEN

ALIF = 'ا'

BAA = 'ب'

TAA = 'ت'

THAA = 'ث'

JIM = 'ج'

HHAA = 'ح'

XAA = 'خ'

DAL = 'د'

DHAL = 'ذ'

RAA = 'ر'

ZAYN = 'ز'

SIN = 'س'

SHIN = 'ش'

SAD = 'ص'

DAD = 'ض'

TTAA = 'ط'

ZZAA = 'ظ'

EIN = 'ع'

GHAIN = 'غ'

FAA = 'ف'

QAF = 'ق'

KAF = 'ك'

LAM = 'ل'

MIM = 'م'

NUN = 'ن'

HAA = 'ه'

WAW = 'و'

YAA = 'ي'

HAMZA = 'ء'

ALIF_MAQSURA = 'ى'

VOWELS = ALIF + WAW + YAA + ALIF_MAQSURA

CONSONANTS = BAA + TAA + THAA + JIM + HHAA + XAA + DAL + DHAL + RAA + ZAYN + SIN + SHIN + SAD + DAD + TTAA + ZZAA + EIN + GHAIN + FAA + QAF + KAF + LAM + MIM + NUN + HAA + HAMZA

ABJAD = VOWELS + CONSONANTS

ARABIC_CHARACTERS = ABJAD + DIACRITICS

ARABIC_LANGUAGE_CODE = 'ar'

ENGLISH_LANGUAGE_CODE = 'en'

POS_CHOICES = (('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'))

GENDER_CHOICES = (('masculine', 'Masculine'), ('feminine', 'Feminine'))

HUMAN_CHOICES = (('human', 'Human'), ('non-human', 'Non-Human'))

TENSE_MOOD_CHOICES = (('indicative-perfect', 'Indicative Perfect'), ('indicative-imperfect', 'Indicative Imperfect'))

COUNT_CHOICES = (('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural'))

PERSON_CHOICES = (('first', 'First'), ('second', 'Second'), ('third', 'Third'))

STATE_CHOICES = (('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite'))

CASE_CHOICES = (('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative'))