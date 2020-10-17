from behave import given, when, then, step
from calculator import Calculator

@given('the numbers {number1:f} and {number2:f}')
def step_impl(context, number1, number2):
    context.calculator = Calculator()
    context.number1 = number1
    context.number2 = number2
    pass

@when('sum thoses numbers')
def step_impl(context):
    context.result = context.calculator.sum(context.number1, context.number2)
    pass

@when('subtract thoses numbers')
def step_impl(context):
    context.result = context.calculator.subtract(context.number1, context.number2)
    pass

@when('multiply thoses numbers')
def step_impl(context):
    context.result = context.calculator.multiply(context.number1, context.number2)
    pass

@when('divide thoses numbers')
def step_impl(context):
    context.result = context.calculator.divide(context.number1, context.number2)
    pass

@then('the result should be {result:f}!')
def step_impl(context, result):
    assert context.result == result