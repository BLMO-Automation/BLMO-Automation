from behave import *
from features.TestBase.testbase import *


@when("I open automationpractice website")
def step_impl(context):
    page = LMOHomePage(context)
    page.url_open("http://www.automationpractice.com")
    page.sign_in.click()