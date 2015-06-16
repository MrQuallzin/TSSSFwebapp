# The sanity check steps, implemented
from expects import *


@when(u'I add {x:Integer} and {y:Integer}')
def add_x_and_y(context, x, y):
  context.val = x + y

@then(u'I should have {val:Integer}')
def should_have_val(context, val):
  expect(context.val).to(equal(val))
@when(u'I check the value of {val:Boolean}')
def check_the_value_of_bool(context, val):
  context.val = val


@then(u'it should be {val:Boolean}')
def value_should_be_boolean(context, val):
  expect(context.val).to(equal(val))
