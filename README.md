YaaHamza
========
YaaHamza is an under development reference tool for the Arabic language, developed using Django.
It is designed to have features that are particularly helpful for the Arabic language, much like Chinese-specific website YellowBridge.

Name
----------
The name "YaaHamza" is derived from the last two letters of the Arabic Alphabet (Abjad), Yaa and Hamza.
It could also be interpreted as a call using the Arabic word for "hey" ("yaa") and the Arabic name "Hamza"; in other
words, "Hey Hamza!".

Implementation
----------
YaaHamza manages three types of dictionary entries: Roots, Words, and Inflections.
Roots are triliteral or quadriliteral Arabic roots.
Words can be any Arabic word (at all levels of derivation), with no applied inflection,
potentially linked to a Root. Finally, Inflections are fully-inflected words, with a link to the associated word.

Also included are two models for derivational and inflectional patterns. Deriver and Inflecter both use
a regular-expression based template system to produce Words and Inflections.