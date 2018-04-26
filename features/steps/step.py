# -*- coding: utf-8 -*
from behave import *

@given(u'第一个值输入 10')
def step_impl(context):
	el = context.driver.find_element_by_accessibility_id('textfield1')
	el.clear()
	el.set_value("10")



@given(u'第二个值输入 20')
def step_impl(context):
	el = context.driver.find_element_by_accessibility_id('textfield2')
	el.clear()
	el.set_value("20")


@when(u'点击 求和按钮')
def step_impl(context):
	el = context.driver.find_element_by_accessibility_id('sum')
	el.click()


@then(u'结果应该为30')
def step_impl(context):
	# el = context.driver.find_element_by_accessibility_id('result')
	el = context.driver.find_element_by_class_name('XCUIElementTypeStaticText')
	actual = el.get_attribute('value')
	print(actual)
	assert actual=='30', 'result is 30'