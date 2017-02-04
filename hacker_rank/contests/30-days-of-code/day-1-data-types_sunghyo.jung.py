inputs = [5.35, 'a', False, 100, "I am a code monkey", True, 17.3, 'c', "derp"]
for data in inputs:
    if type(data) is int:
        print 'Primitive : int'
    elif type(data) is float:
        print 'Primitive : double'
    elif type(data) is bool:
        print 'Primitive : boolean'
    elif type(data) is str and len(data) == 1:
        print 'Primitive : char'
    elif type(data) is str:
        print 'Referenced : String'
