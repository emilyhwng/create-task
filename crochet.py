from PIL import Image
import os

os.system('cls')

# maximizes dimensions maintaining original aspect ratio under the maximum number of pixels
def get_dimensions(image, max_pixels):
    image = Image.open(image)
    
    width, height = image.size
    total_pixels = width * height
    if total_pixels > max_pixels:
        ratio = width / height
        new_width = int((max_pixels * ratio) ** 0.5)
        new_height = int(new_width / ratio)
    else:
        new_width, new_height = width, height
    return new_width, new_height

# creates pixel grid using colors of palette represented by letters
def pixelate(image, colors):
    image = Image.open(image)

    image = image.resize((width, height))
    palette = image.quantize(colors)
    
    pattern = ''
    for i in range(height):
        for j in range(width):
            color_index = palette.getpixel((j, i))
            pattern += chr(ord('A') + color_index)
        pattern += '\n'

    print("\nDimensions:", width, "x", height)
    return pattern

# creates written pattern counting number of consecutives stitches in a color for each row, starting from the bottom left and working way up going back and forth
def written_pattern(pattern):
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
    
    result.reverse()
    
    string = ''    
    for i in range (len(result)):
        side = ''
        if i % 2 == 0:
            side = "[RS]"
        else: 
            side = "[WS]"
        string = "row " + str(i + 1) + " " + side + ": " + result[i]
        print(string)

# getting input information (file name, max pixels, and number of palette colors)
name = input('what is the image file name? ')
max_pixels = int(input('maximum number of pixels? '))
colors = int(input('how many different colors do you want to use? '))
file_name = name + '.jpg'

# calculating dimensions and making pixel grid
width, height = get_dimensions(file_name, max_pixels)
pixel_grid = pixelate(file_name, colors)

# printing pixel grid and written pattern
print('\n' + pixel_grid)
print('---------- WRITTEN PATTERN ----------\n')
print('foundation chain: ' + str(width) + ' chains')
written_pattern(pixel_grid)