def checkio(*args):
    lis = []
    if args :
        for arg in args:
            lis.append(arg)
            arg+=1
        n = min(lis)
        x = max(lis)
        res = x - n
        print(round(res,3))
    else:return 0
checkio(-0.036,-0.11,-0.55,-64)