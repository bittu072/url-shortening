import random
import string

def code_generator(size=10, chars=string.ascii_lowercase + string.ascii_uppercase):
    # new_code = ''
    # for i in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for i in range(size))

def create_shorturl(instance, size=6):
    new_url = code_generator(size=size)
    klass = instance.__class__
    # this is similar to importing ShortenURL class from models.py

    qs_exists = klass.objects.filter(shorturl=new_url).exists()
    if qs_exists:
        return create_shorturl(size=size)
    return new_code
