def compress(text):
    dictionary = {}
    next_code = 1
    i = 0
    final_output = []

    while i < len(text):
        match = ""
        match_code = ""

        temp_j = i
        while temp_j < len(text) and text[i:temp_j+1] in dictionary:
            match = text[i:temp_j+1]
            match_code = dictionary[match]
            temp_j += 1

        if match == "":
            current_char = text[i]
            final_output.append(current_char)
            

            dictionary[current_char] = str(next_code)
            next_code += 1
            i += 1
        else:

            i += len(match)
            if i < len(text):
                next_char = text[i]
                final_output.append(f"{match_code}{next_char}")
                
                new_pattern = match + next_char
                dictionary[new_pattern] = str(next_code)
                next_code += 1
                i += 1
            else:
                final_output.append(match_code)

    return "".join(final_output)


data = input("What do you want me to compress?  ") 
 
print(f"Original: {data}")
print(f"Compressed: {compress(data)}")
