# gradient_charset = " .:-=+*#%@"
gradient_charset = "  ░░▒▒▓▓██"
scale = len(gradient_charset) - 1

def print_img(img, width=28):
    render = '┌'
    for i in range(width):
        render += '─'
    render += '┐'

    for i in range(len(img)):
        if i % width == 0:
            if i == 0:
                render += '\n│'
            else:
                render += '│\n│'
        render += gradient_charset[int((img[i] / 255) * scale)]

    render += '│\n└'
    for i in range(width):
        render += '─'
    render += '┘'

    print(render)