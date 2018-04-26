# -*- coding: utf-8 -*
import os
from appium import webdriver

def before_feature(context, feature):
    app = '/Users/yangfangming/Desktop/TestDemo/app/TestApp.app'
    context.driver = webdriver.Remote(
    	command_executor='http://127.0.0.1:4723/wd/hub',
    	desired_capabilities={
    		'app': app,
    		'platformName': 'ios',
    		'deviceName': 'iPhone 8',
    		'platformVersion': '11.1',
    		'bundleId': 'com.yfm.TestApp'
    	})

def after_feature(context, feature):
	context.driver.quit()