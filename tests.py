#!/usr/bin/env python3

def rcomplement(dna) :
    '''
    Returns a string with the reverse complement of a DNA sequence.
    Sequences containing non-DNA will return an empty string.

    The complements are A-T and C-G; the returned string should be reversed.
    '''
    return None

def test_rcomplement() :
    assert rcomplement('AACGGT') == 'ACCGTT'
    assert rcomplement('ACGTZ') == ''

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    return None


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]
