def calculate_pyramid_height(blocks):
    layer = 0
    height = 0
    while blocks >= layer + 1 :
        blocks -= layer
        layer += 1
        height += 1
    return height
