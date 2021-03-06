# -*- coding: utf-8 -*-

import pytest


def test_whitespace():
    from rasa_nlu.tokenizers.whitespace_tokenizer import WhitespaceTokenizer
    tk = WhitespaceTokenizer()
    sentence = u"Hi. My name is rasa"
    assert tk.tokenize(sentence) == [u'Hi.', u'My', u'name', u'is', u'rasa']


def test_spacy():
    def tokenize_sentence(sentence, expected_result, language):
        from rasa_nlu.tokenizers.spacy_tokenizer import SpacyTokenizer
        tk = SpacyTokenizer(language)
        assert tk.tokenize(sentence) == expected_result

    tokenize_sentence(u"Hi. My name is rasa", [u'Hi', u'.', u'My', u'name', u'is', u'rasa'], 'en')
    tokenize_sentence(u"Hallo. Mein name ist rasa", [u'Hallo', u'.', u'Mein', u'name', u'ist', u'rasa'], 'de')


def test_mitie():
    from rasa_nlu.tokenizers.mitie_tokenizer import MITIETokenizer
    tk = MITIETokenizer()

    tk.tokenize(u"Hi. My name is rasa") == [u'Hi', u'My', u'name', u'is', u'rasa']
    tk.tokenize(u"ὦ ἄνδρες ᾿Αθηναῖοι.") == [u'ὦ', u'ἄνδρες', u'᾿Αθηναῖοι']
