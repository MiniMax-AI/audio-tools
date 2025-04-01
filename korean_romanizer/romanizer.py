import re

from .syllable import Syllable
from .pronouncer import Pronouncer

'''
### Transcribing vowels ###
'''

vowel = {
    # 단모음 monophthongs
    'ㅏ' : 'a',
    'ㅓ' : 'eo',
    'ㅗ' : 'o',
    'ㅜ' : 'u',
    'ㅡ' : 'eu',
    'ㅣ' : 'i',
    'ㅐ' : 'ae',
    'ㅔ' : 'e',
    'ㅚ' : 'oe',
    'ㅟ' : 'wi',
    
    # 이중모음 diphthongs
    'ㅑ' : 'ya',
    'ㅕ' : 'yeo',
    'ㅛ' : 'yo',
    'ㅠ' : 'yu',
    'ㅒ' : 'yae',
    'ㅖ' : 'ye',
    'ㅘ' : 'wa',
    'ㅙ' : 'wae',
    'ㅝ' : 'wo',
    'ㅞ' : 'we',
    'ㅢ' : 'ui', # [붙임 1] ‘ㅢ’는 ‘ㅣ’로 소리 나더라도 ‘ui’로 적는다.
}

'''
### Transcribing consonants ###

Consonants are defined in separate dicts, choseong and jongseong,
for some characters are pronounced differently depending on 
its position in the syllable.

e.g. ㄱ, ㄷ, ㅂ, ㄹ are (g, d, b, r) in onset,
                  but (k, t, p, l) in coda.
e.g. ㅇ is a null sound when placed in onset, but becomes [ng] in coda.
'''

# 초성 Choseong (Syllable Onset)
onset = {
    # 파열음 stops/plosives
    'ᄀ' : 'g',
    'ᄁ' : 'kk',
    'ᄏ' : 'k',
    'ᄃ' : 'd',
    'ᄄ' : 'tt',
    'ᄐ' : 't',
    'ᄇ' : 'b',
    'ᄈ' : 'pp',
    'ᄑ' : 'p',
    # 파찰음 affricates
    'ᄌ' : 'j',
    'ᄍ' : 'jj',
    'ᄎ' : 'ch',
    # 마찰음 fricatives
    'ᄉ' : 's',
    'ᄊ' : 'ss',
    'ᄒ' : 'h',
    # 비음 nasals
    'ᄂ' : 'n',
    'ᄆ' : 'm',
    # 유음 liquids
    'ᄅ' : 'r',
    # Null sound
    'ᄋ' : '',
}

'''
종성 Jongseong (Syllable Coda)

"The 7 Jongseongs (7종성)"
Only the seven consonants below may appear in coda position
'''

coda = {
    # 파열음 stops/plosives
    'ᆨ' : 'k',
    'ᆮ' : 't',
    'ᆸ' : 'p',
    # 비음 nasals
    'ᆫ' : 'n',
    'ᆼ' : 'ng',
    'ᆷ' : 'm',
    # 유음 liquids
    'ᆯ' : 'l',
    
    None: '',
}
    
class Romanizer(object):
    def __init__(self, text):
        self.text = text

    def romanize(self, han_sylla=True):
        '''
        han_sylla=True: 直接返回韩语拼音
        '''
        pronounced = Pronouncer(self.text).pronounced
        # hangul = r"[가-힣ㄱ-ㅣ]"
        _romanized = ""
        for char in pronounced:
            if 0xAC00 <= ord(char) <= 0xD7A3:
                s = Syllable(char)
                if s is None:
                    _romanized += char
                    continue
                    
                if han_sylla:
                    if s.initial:
                        _romanized += s.initial
                    if s.medial:
                        _romanized += s.medial
                    if s.final:
                        _romanized += s.final
                else:
                    # 原始逻辑
                    if not s.medial and not s.final:
                        # s is NOT a full syllable (e.g. characters)
                        # if onset.get(chr(s.initial)):
                        #     _romanized += onset[chr(s.initial)]
                        # elif vowel.get(chr(s.initial)):
                        #     _romanized += vowel[chr(s.initial)]
                        # else:
                        #    _romanized += char
                        _romanized += char
                    else:
                        # s is a full syllable
                        if s.initial is not None:
                            _romanized += onset[s.initial] + vowel[s.medial] + coda[s.final]
                        else:
                            _romanized += char
            else:
                _romanized += char

        return _romanized
