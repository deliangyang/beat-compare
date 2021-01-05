def b():
    print(1)


if __name__ == '__main__':
    locals()['b']()
    globals()['b']()
    print(locals())