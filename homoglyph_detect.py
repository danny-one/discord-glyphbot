# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:25:27 2021

@author: danny-one
"""

import homoglyphs_fork as hg

# get all categories
cats = hg.Categories.get_all()
# {'RUNIC', 'DESERET', ..., 'SOGDIAN', 'TAI_LE'}

# load alphabet on init by categories
homoglyphs = hg.Homoglyphs(cats)  # alphabet loaded here


# load alphabets & set ascii range
homoglyphs = hg.Homoglyphs(
    languages={'en'},
    strategy=hg.STRATEGY_LOAD,
    ascii_strategy=hg.STRATEGY_REMOVE,
    ascii_range=range(ord('0'), ord('z')),
    categories = cats
)
    
def user_check(new_joiner, member_list):
    results = []
    similar_members = []
    
    for i in range(len(member_list)):
        mbr = member_list[i]
        results.append([])
        for glyph_a in homoglyphs.to_ascii(new_joiner):
            for glyph in homoglyphs.to_ascii(mbr):
                results[i].append(str.lower(glyph_a) == str.lower(glyph))
        if any(results[i]) == True:
            similar_members.append(member_list[i])
    
    return similar_members



'''
# sample use

new_joiner = 'ТЕСТO49' # uses homoglyphs of latin letters
member_list = ['TECT049', 'ImportantUser', 'Some0therGuy']

user_check(new_joiner, member_list)


# sample call to pull similar combos
# hg.Homoglyphs().get_combinations('w')

'''
