from PIL import Image, ImageDraw

path_to_row_image = "uncolored_cirqle.png"
img = Image.open(path_to_row_image)

size = img.size
height, width = size
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 250)
LIGHT_BLUE = (135, 206, 250, 250)


drawMatrix = [[3] * width for i in range(0, height)]
for i in range(0, height):
    for j in range(0, width):
        if img.getpixel((i, j)) != WHITE:
            drawMatrix[i][j] = 1

filled = 0
poped = 0
stack = []
print(drawMatrix)
print(img.getcolors())

stack.append((350, 350))

while len(stack) != 0:
    pixel = stack.pop(-1)
    y, x = pixel
    print(f'Вытащил и закрасил пиксель: {(x, y)}')
    poped += 1
    filled += 1
    drawMatrix[y][x] = 2
    x_temp = x
    x += 1
    print('Пошел направо')
    while drawMatrix[y][x] != 1:
        drawMatrix[y][x] = 2
        print(f'Закрасил пиксель {(x, y)}')
        filled += 1
        x += 1
    x_right = x - 1
    x = x_temp
    x -= 1
    print('Пошел налево')
    while drawMatrix[y][x] != 1:
        drawMatrix[y][x] = 2
        print(f'Закрасил пиксель {(x, y)}')
        filled += 1
        x -= 1
    x_left = x + 1
    x = x_left
    y -= 1
    print('Пошел вверх')
    while(x <= x_right):
        flag = False
        while drawMatrix[y][x] != 2 and drawMatrix[y][x] != 1 and x < x_right:
            if not flag:
                flag = True
            print('Пошел направо в поисках незакрашенных пикселей')
            x += 1
        if flag:
            if x == x_right and drawMatrix[y][x] != 1 and drawMatrix != 2:
                print(f'Добавил пиксель {(x, y)} в стек')
                stack.append((y, x))
            else:
                print(f'Добавил пиксель {(x - 1, y)} в стек')
                stack.append((y, x - 1))
            flag = False
        x_enter = x
        while (drawMatrix[y][x] == 2 or drawMatrix[y][x] == 1) and x < x_right:
            print('Пошел направо в последнем while')
            x += 1
        if x == x_enter:
            print('Пошел направо в последнем if')
            x += 1
    x = x_left
    y += 2
    print('Пошел вниз')
    while(x <= x_right):
        flag = False
        while drawMatrix[y][x] != 2 and drawMatrix[y][x] != 1 and x < x_right:
            if not flag:
                flag = True
            print('Пошел направо в поисках незакрашенных пикселей')
            x += 1
        if flag:
            if x == x_right and drawMatrix[y][x] != 1 and drawMatrix != 2:
                print(f'Добавил пиксель {(x, y)} в стек')
                stack.append((y, x))
            else:
                print(f'Добавил пиксель {(x - 1, y)} в стек')
                stack.append((y, x - 1))
            flag = False
        x_enter = x
        while (drawMatrix[y][x] == 2 or drawMatrix[y][x] == 1) and x < x_right:
            print('Пошел направо в последнем while')
            x += 1
        if x == x_enter:
            print('Пошел направо в последнем if')
            x += 1

idDraw = ImageDraw.Draw(img)
for i in range(0, height):
    if i == width - 2:
            print("tut")
    for j in range(0, width):
        if(drawMatrix[i][j] == 2):
            idDraw.point((i, j), fill=LIGHT_BLUE)

print('Готово!')
print(f'Закрашено пикселей: {filled}')
print(f'Всего было в стеке пикселей: {poped}')
print(f'Зря побывало в стеке пикселей: {(((poped - filled) * 100) / poped):.2f} %')

img.save("line_colored_cirqle.png")