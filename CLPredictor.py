#!/usr/bin/env python

#
#   Functions that take a question and answer in Fullmarks format and returns a predicted level based on Blooms keywords
#

import lxml.etree as etree
import os



Blooms_levels = {'evaluation':7, 'synthesis':6, 'analysis':5, 'application':4, 'comprehension':3, 'knowledge':2, 'fragmented_knowledge':1}

Blooms_phrases = {
        # Level 7
        'evaluation' : ['assess', 'decide', 'rank', 'grade', 'test', 'measure', 'recommend', 'convince', 'select', 'judge', 'explain', 'discriminate', 'support', 'conclude', 'compare', 'summarize', 'critique', 'interpret', 'justify'],
        
        # Level 6
        'synthesis' : [ 'combine', 'integrate', 'modify', 'rearrange', 'substitute', 'plan', 'create', 'design', 'invent', 'what if?', 'compose', 'formulate', 'prepare', 'generalize', 'rewrite', 'categorize', 'combine', 'compile', 'reconstruct'],

        # Level 5
        'analysis' : ['analyze', 'separate', 'order', 'explain', 'connect', 'classify', 'arrange', 'divide', 'compare', 'select', 'infer', 'break down', 'contrast', 'distinguish', 'diagram', 'illustrate'],

        # Level 4
        'application' : [ 'apply', 'demonstrate', 'calculate', 'complete', 'illustrate', 'show', 'solve', 'examine', 'modify', 'relate', 'change', 'classify', 'experiment', 'discover', 'construct', 'manipulate', 'prepare', 'produce'], 

        # Level 3
        'comprehension' : ['summarize', 'describe', 'interpret', 'contrast', 'predict', 'associate', 'distinguish', 'estimate', 'differentiate', 'discuss', 'extend', 'comprehend', 'convert', 'defend', 'explain', 'generalize', 'give example', 'rewrite' ],

        # Level 2
        'knowledge' : ['list', 'define', 'tell', 'describe', 'identify', 'show', 'know', 'label', 'collect', 'select', 'reproduce', 'match', 'recognize', 'examine', 'tabulate', 'quote', 'name'],
        'fragmented_knowledge' : []
        
        }


def getBloomsLabel(bloomlevel):
    '''Given the Bloom level as a integer or string, return the cognitive level's label as a string'''
    try:
        bloomlevel = int(bloomlevel)
    except:
        print("Invalid input value, please input an integer in the range 1 to 7")
        return None
    
    # erroneous input
    if bloomlevel not in [1,2,3,4,5,6,7]:
        print("Invalid input value, please input an integer in the range 1 to 7")
        return None

    for b in Blooms_levels.keys():
        if Blooms_levels[b] == bloomlevel:
            return b





def getText(question_html):
    ''' Given the html string of a question from fullmarks, extract the text and return as a string
    
    For now we'll skip the MathML parts, Blooms doesn't use that.
    
    question_html should be a string containing the html contents of the question



    '''

    # parse the html that comes in
    try:
        html = etree.HTML(question_html)
    except etree.XMLSyntaxError as e:
        print(e, e.args)
        return None
    

    # we want to extract all the words in the text


    text = []

    for element in html.iter():
        if element.text is not None:
            text.append(element.text)

    text = ' '.join(text).lower()

    return text



def getBloomsLevel(text):
    ''' Given the question's text as a string, return a predicted value for the Bloom's cognitive value based upon matches to the keywords'''

    matches = {}
    # split the text so we can match whole words
    text = text.split(' ') 


    # for every bloom level
    for b in Blooms_levels.keys():
        keywords = Blooms_phrases[b]

        # count the occurence of each keyword in the text
        count = sum([text.count(k) for k in keywords])
        
        matches[b] = count
    
    print matches
    # get the name of the highest count
    highest = 0 
    level = 0    
    for m in matches.keys():
        count = matches[m]
        if matches[m] != 0:
            if count >= highest:
                highest = count
                level = Blooms_levels[m]

    return level 






if __name__ == '__main__':
    print('Cogntive Level Predictor module ran')
    
    # load the questions for testing
    question_files = [q for q in os.listdir('test_questions') if os.path.splitext(q)[1] == '.html']
    
    for q in question_files:
        print '\n', q , '\n', 
        html = open('test_questions/'+q ,'r').read()
        text = getText(html)
        level = getBloomsLevel(text) 
        print text
        print(level)
        print(getBloomsLabel(level))
    


