from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    a_lines = a.splitlines()
    b_lines = b.splitlines()
    c_lines=[]

    for a in a_lines:
        if a in b_lines:
            c_lines.append(a)

    c_lines_set = []
    [c_lines_set.append(c) for c in c_lines if c not in c_lines_set] # list comprehension to remove duplicate sentences
    # TODO
    #print(c_lines)
    return c_lines_set


def sentences(a, b):
    """Return sentences in both a and b"""
    a_sent = sent_tokenize(a)
    b_sent = sent_tokenize(b)
    c_sent = []

    for a in a_sent:
        if a in b_sent:
            c_sent.append(a)


    c_sent_set = []
    [c_sent_set.append(c) for c in c_sent if c not in c_sent_set] # list comprehension to remove duplicate sentences

    # TODO
    return c_sent_set


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    a_ss = []
    b_ss = []
    for i in range(0, len(a)-n+1, 1):
        a_ss.append(a[i:i+n])

    for j in range(0, len(b)-n+1, 1):
        b_ss.append(b[j:j+n])

    c_ss = []

    for a in a_ss:
        if a in b_ss:
            c_ss.append(a)

    c_ss_set = []
    [c_ss_set.append(c) for c in c_ss if c not in c_ss_set] # list comprehension to remove duplicate substrings

    # TODO
    return c_ss_set

