def escape(string):
    return ''.join(c if ord(c) < 127 and ord(c) > 31 else '\\x%02x' % ord(c) for c in string)
