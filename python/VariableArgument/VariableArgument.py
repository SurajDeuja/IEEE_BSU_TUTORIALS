
def arguments(*args, **kwargs):
    for i in args:
        print i

    for k,v in kwargs.iteritems():
        print "Key =", k, "Value =", v



arguments(1, 2, 3, 5, 4, A=1, B=2, C=3)