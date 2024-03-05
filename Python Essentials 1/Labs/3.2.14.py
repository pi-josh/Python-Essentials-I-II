# Essentials of the while loop
'''
Scenario
Listen to this story: a boy and his father, a computer programmer,
are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat.
The pyramid is stacked according to one simple principle:
each lower layer contains one block more than the layer above.

Your task is to write a program which reads the number of blocks the builders have,
and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers
- if the builders don't have a sufficient number of blocks and cannot complete the next layer, 
hey finish their work immediately.
'''

blocks = int(input("Enter the number of blocks: "))

height = 0
i = 1
while blocks >= 0:
    blocks -= i
    if blocks >= 0:
        height += 1
    else:
        break
    i += 1

print("The height of the pyramid:", height)

