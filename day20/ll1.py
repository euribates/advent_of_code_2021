import numpy as np

input_files = ["20-sample.txt", "20-input.txt"]

with open(input_files[1], 'r') as f:
    data =  [a.strip() for a in f.readlines()]

iea = data[0]
image = np.array([list(x) for x in data[2:]])
outside = '.'


def get_char(grid):
    flat = grid.flatten()
    flat[flat == "."] = 0
    flat[flat == "#"] = 1

    bitstring = "".join(flat)
    value = int(bitstring, 2)

    return iea[value]

def step(img, outside, iea=iea):
    img = np.pad(img, 2, 'constant', constant_values = outside)
    new_img = np.zeros((img.shape[0] - 2, img.shape[1] - 2), dtype=str)

    for y in range(new_img.shape[0]):
        for x in range(new_img.shape[1]):
            new_img[y][x] = get_char(img[y:y+3, x:x+3])

    return new_img

def part1(image, outside):
    for i in range(2):
        print('size antes', image.shape)
        image = step(image, outside)
        print('size despues', image.shape)
        outside = get_char(np.array(list(outside*9)).reshape((3,3)))

    print(np.count_nonzero(image == "#"))
    return image

i = part1(image, outside)
print(i)
