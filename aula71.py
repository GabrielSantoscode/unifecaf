x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#   return x + y

def soma(*args):
    print(args)

soma(1, 2, 3, 4, 5, 6)