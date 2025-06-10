# """
# nested_dict = {
#     "a": 1,
#     "b": {
#         "c": 2,
#         "d": {
#             "e": 3
#         }
#     },
#     "f": 4
# }

#     a": 1,
#     "b.c": 2,
#     "b.d.e": 3,
#     "f": 4
# }
# """
# nested_dict = {
#     "a": 1,
#     "b": {
#         "c": 2,
#         "d": {
#             "e": 3
#         }
#     },
#     "f": 4
# }

# def formatJson(inp):
#     d = []
#     s = {}
    
#     for k, v in inp.items():
#         d.append(k)
#         if type(v) == 'dict':
#             while True:

#         else:
#             s[".".join(d)] = v
#             d = []
#     return s

# op = formatJson(nested_dict)
# print(op)

inp = [3, 8, 9, 4, 2, 1, 19, 10]

def getDiff(inp):
    d = {}
    halfi = len(inp)//2
    ci = halfi if len(inp)%2 == 0 else halfi+1
    for i in range(ci):
        for j in range(ci):
            if not j+ci >= len(inp):
                diff = str(abs(inp[i] - inp[j+ci]))
                if not d.get(diff, None):
                    d[diff] = [(inp[i], inp[j+ci])]
                else:
                    d[diff].append((inp[i], inp[j+ci]))
            # if ci > i+j+1: 
            #     adiff = str(inp[i] - inp[i+j+1])
            #     if not d.get(adiff, None):
            #         d[adiff] = [(inp[i], inp[i+j+1])]
            #     else:
            #         d[adiff].append((inp[i], inp[i+j+1]))
            # rdiff = str(inp[ci+i] - inp[ci+j+1])
            # if len(inp) > ci+j+1:
            #     if not d.get(rdiff, None):
            #         d[rdiff] = [(inp[ci], inp[ci+j+1])]
            #     else:
            #         d[rdiff].append((inp[ci], inp[ci+j+1]))
    print(d)

getDiff(inp)

                

