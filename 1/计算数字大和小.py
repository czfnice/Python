def findMinAndMax(l):
    if l == []:
        return (None,None)
    else:
        min=l[0]
        max=l[0]
        for x in l:
            if x <= min:
                min = x
            elif x >= max:
                max = x
        return (min,max)