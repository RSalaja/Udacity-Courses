Python_Reference = 'https://s3-us-west-2.amazonaws.com/gae-supplemental-media/cs101/unit1-python-reference.pdf'
Unit_1 = 'http://www.cs.virginia.edu/~evans/cs101/unit1-notes.pdf'
Unit_2 = 'http://www.cs.virginia.edu/~evans/cs101/unit2-notes.pdf'
Unit_3 = 'http://www.cs.virginia.edu/~evans/cs101/unit3-notes.pdf'
Unit_4 = 'http://www.cs.virginia.edu/~evans/cs101/unit4-notes.pdf'
Unit_5 = 'http://www.cs.virginia.edu/~evans/cs101/unit5-notes.pdf'
Unit_6 = 'http://www.cs.virginia.edu/~evans/cs101/unit6-notes.pdf'



def open_resource(a):

    if print(a) == print(Unit_1 or Unit_2 or Unit_3 or Unit_4 or Unit_5 or Unit_6):
        import webbrowser
        webbrowser.open(a)
    else:
        import webbrowser
        webbrowser.open(Python_Reference)

open_resource(5)