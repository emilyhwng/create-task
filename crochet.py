from PIL import Image

def pixelate(image, max_pixels, colors):
    image = Image.open(image)

    width, height = image.size
    total_pixels = width * height
    if total_pixels > max_pixels:
        ratio = width / height
        new_width = int((max_pixels * ratio) ** 0.5)
        new_height = int(new_width / ratio)
    else:
        new_width, new_height = width, height

    image = image.resize((new_width, new_height))

    palette = image.quantize(colors)

    pattern = ''
    for i in range(new_height):
        for j in range(new_width):
            color_index = palette.getpixel((j, i))
            pattern += chr(ord('A') + color_index)
        pattern += '\n'

    print()
    print("Dimensions:", new_width, "x", new_height)
    return pattern

def consecutive_letters(pattern):
    rows = pattern.split('\n')[:-1]
    result = []
    for row in rows:
        count = 0
        line = ''
        start_letter = row[0]
        for i in range(len(row)):
            current_letter = row[i]
            if current_letter == start_letter:
                count += 1
            else:
                line += str(count) + start_letter + ' '
                count = 1
                start_letter = current_letter
        line += str(count) + start_letter
        result.append(line)
    
    string = ''    
    for i in range (len(result)):
        side = ''
        if i % 2 == 0:
            side = "[RS]"
        else: 
            side = "[WS]"
        string = "row " + str(i + 1) + " " + side + ": " + result[i]
        print(string)

name = input('what is the image file name? ')
max_pixels = int(input('maximum number of pixels? '))
colors = int(input('how many different colors do you want to use? '))
file_name = name + '.jpg'

crochet_pattern = pixelate(file_name, max_pixels, colors)
print()
print(crochet_pattern)
counts = consecutive_letters(crochet_pattern)
print()