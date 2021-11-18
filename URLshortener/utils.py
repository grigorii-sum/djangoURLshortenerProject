from random import choice
from string import ascii_letters, digits

'''
SIZE for making length of suffix for short URL
AVAILABLE_CHARS for making set of available characters for short URL's suffix
'''
SIZE = 7
AVAILABLE_CHARS = ascii_letters + digits


# Function for creating new random code of 7 characters for new long URL
def create_random_code(chars=AVAILABLE_CHARS):
    return "".join(choice(chars) for _ in range(SIZE))


'''
Function for:
- creating suffix for short URL
- checking that new random code is unique
'''
def create_short_url(model_instance):
    random_code = create_random_code()

    model_class = model_instance.__class__
    if model_class.objects.filter(short_url=random_code).exists():
        return create_short_url(model_instance)

    return random_code
