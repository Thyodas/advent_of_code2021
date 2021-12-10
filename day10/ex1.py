list_input = open('input.txt', 'r').read().split('\n')

stack = []
errors = 0
open = "({[<"
points = {")":3, "]":57, "}":1197, ">":25137}
associate = {")":"(", "]":"[", "}":"{", ">":"<"}

for line in list_input:
    for le in line:
        if le in open:
            stack.append(le)
        else:
            if stack.pop() != associate[le]:
                errors += points[le]

print(errors)