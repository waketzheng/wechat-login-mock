import string

from django.utils.crypto import get_random_string


def random_string(num):
    chars = string.digits + string.ascii_letters + "_-"
    return get_random_string(num, allowed_chars=chars)
