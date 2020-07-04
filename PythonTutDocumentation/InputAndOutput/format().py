import os
""" "First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'."""

""" "Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first """

print('{0}{1}{0}{punctuation}'.format('abra', 'dabra', punctuation='!'))

print('{:<30}'.format('left alligned'))
print('{:>30}'.format('right alligned'))
print('{:^30}'.format('centered'))
print('{:\'^30}'.format('centered and filled'))

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)) # see documentation for format mini language

row1 = [0, 0, 0]
row2 = [0, 1, 0]
row3 = [0, 0, 0]

user_dir = input('Which direction will you go')
