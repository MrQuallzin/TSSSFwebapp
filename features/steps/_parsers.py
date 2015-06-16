# common-sense parsers for regexes
from behave import register_type
import parse

@parse.with_pattern(r'[-+]?\d+')
def parse_integer(text):
    return int(text)

@parse.with_pattern(r'[Tt]rue|[Ff]alse')
def parse_boolean(text):
    if text.lower() == 'true':
        return True
    return False

register_type(Boolean=parse_boolean)
register_type(Integer=parse_integer)
