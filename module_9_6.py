def all_variants(texst):
    k = ""
    l = 0
    for g in range(len(texst)):
        if g == 0:
            for i in range(len(texst)):
                k = texst[i]
                yield k
        else:
            for f in range(len(texst) + 1):
                if g != len(texst) :
                    g = g + 1
                    k = texst[f:g]
                    yield k
                else:
                    break
a = all_variants("abc")
for i in a:
    print(i)