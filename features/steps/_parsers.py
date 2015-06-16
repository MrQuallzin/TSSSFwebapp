# common-sense parsers for regexes
from behave import register_type
import parse

@parse.with_pattern(r'[-+]?\d+')
def parse_integer(text):
    return int(text)

register_type(Integer=parse_integer)
