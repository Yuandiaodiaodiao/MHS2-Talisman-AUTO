def castimg(src, args, h=1, w=1):
    args = [args[0] * h, args[1] * h, args[2] * w, args[3] * w]
    args = list(map(int, args))
    return src[args[0]:args[1], args[2]:args[3], ...]

