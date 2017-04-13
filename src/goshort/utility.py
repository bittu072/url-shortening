import random
import string

def code_generator(size=10, chars=string.ascii_lowercase + string.ascii_uppercase):
    # new_code = ''
    # for i in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for i in range(size))
