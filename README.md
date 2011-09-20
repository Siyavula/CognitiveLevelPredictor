# Siyavula Cognitive Level Predictor for Fullmarks

This module contains functions that takes a fullmarks assesment item and tries to predict
the cognitive level of the question as specified by the Blooms system based on keywords in the text.


## Usage

    import CLPredictor as coglev
    
    # read the html content as a string
    html = open('question.html', 'r').read()
    
    text = coglevel.getText(html)
    bloomlevel = coglevel.getBloomsLevel(text)


This is bound to change soon.