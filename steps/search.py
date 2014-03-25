from behave import given
from behave import when
from behave import then
from hamcrest import assert_that
from hamcrest import equal_to, is_not

@given(u'I am on Google landing page')
def step_impl(context):
  context.browser.get('http://google.com')

@when(u'I enter the information on the search field')
def step_impl(context):
  context.browser.find_element_by_id('gbqfq').send_keys('Python')

@when(u'I click on Search button')
def step_impl(context):
  context.browser.find_element_by_id('gbqfb').click()

@then(u'I see the results from my search')
def step_impl(context):
  context.browser.implicitly_wait(3)
  result = context.browser.find_element_by_link_text('Welcome to Python.org')
  assert_that(result.is_displayed(), equal_to(False))

