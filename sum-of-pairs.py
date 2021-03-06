# SUM OF PAIRS (5 KYU)
#
# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]
#
# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]
#
# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)
#
# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]

def sum_pairs(ints, s):
    if len(ints) < 2:
        return None
    t = {ints[0]}
    for i in range(1, len(ints)):
        x = s - ints[i]
        if x in t:
            return [x,ints[i]]
        t.add(ints[i])
    return None

# NOTE:
# I initially wrote the following method:
#
# l = len(ints)
#     for i in range(1, l):
#         for j in range(i):
#             x = ints[i]
#             y = ints[j]
#             if x + y == s:
#                 return [y, x]
#     return None
#
# This method works in theory, but it timed out on some of the larger test cases
# that they gave me on codewars. My initial method was O(n ** 2), and the method
# I ended up sumbitting was roughly O(n), since sets are about constant time.
