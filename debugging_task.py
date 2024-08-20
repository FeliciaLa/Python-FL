# Function to print dictionary values given the keys
def print_values_of(dictionary, *keys):    # function needs to accept a variable number of keys: 'keys' -> '*keys'
    for key in keys:
        print(dictionary[key])   # Name error: Change k to key or k is not defined

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", # Syntax Error: "" instead of ''
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')    # Type Error: print_values_of() takes 2 positional arguments but 4 were given -> change line 2

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

