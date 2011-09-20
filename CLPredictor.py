#!/use/bin/python

#
#   Functions that take a question and answer in Fullmarks format and returns a predicted level based on Blooms keywords
#




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
        'knowledge' : ['list', 'define', 'tell', 'describe', 'identify', 'show', 'know', 'label', 'collect', 'select', 'reproduce', 'match', 'recognize', 'examine', 'tabulate', 'quote', 'name']
        
        }





if __name__ == '__main__':
    print('Cogntive Level Predictor module ran')


