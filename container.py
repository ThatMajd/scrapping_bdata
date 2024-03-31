import selenium.webdriver.remote.webelement
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import requests
from constants import BUTTONS

EMAIL = "majdb594@gmail.com"
PASSWORD = "MAJAD2$$1"
JOBS_URL = "https://www.linkedin.com/jobs/search"

USER = "brd-customer-hl_80709a30-zone-scraping_browser6"
PASS = "sb4h7pmd66yp"
AUTH = f'{USER}:{PASS}'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'


print('Connecting to Scraping Browser...')
sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
driver =  Remote(command_executor=sbr_connection, options=ChromeOptions())


