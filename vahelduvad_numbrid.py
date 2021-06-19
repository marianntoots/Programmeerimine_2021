
def pikim_alamsõne(string):
    best_start_index = 0
    best_end_index = 0
    start_index = 0
    end_index = 0
    for i, letter in enumerate(string):
        if end_index == 0 or (int(letter) % 2 == 0) != (int(string[i-1]) % 2 == 0):
            end_index = i+1
        else:
            if end_index - start_index > best_end_index - best_start_index:
                best_start_index = start_index
                best_end_index = end_index
            start_index = end_index = i
    if end_index - start_index > best_end_index - best_start_index:
        best_start_index = start_index
        best_end_index = end_index
    return string[best_start_index:best_end_index]


strings = (
    "3242489248128243892349823486523",
    "1203482471275648238294239472394",
    "8214928744024782480297489247098"
)

for string in strings:
    print(string, "->", pikim_alamsõne(string))
