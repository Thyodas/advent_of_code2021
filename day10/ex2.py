list_input = open('input.txt', 'r').read().split('\n')

errors = []
open = "({[<"
points = {"(":1, "[":2, "{":3, "<":4}
associate = {")":"(", "]":"[", "}":"{", ">":"<"}

for line in list_input:
    stack = []
    current = 0
    for le in line:
        if le in open:
            stack.append(le)
        else:
            if stack[-1] == associate[le]:
                stack.pop()
            else:
                break
    else:
        for a in reversed(stack):
            current *= 5
            current += points[a]
        errors.append(current)

print(sorted(errors)[len(errors) // 2])