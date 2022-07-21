from fluidra.__init__ import *
import time
import numpy
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

openOwnersCenter('akahley@fluidra.com', 'Welcome043!', 'production')

openDevice('iAqua-C25')

switchWindow(1)

use('Menu')
time.sleep(0.2)
use('System Setup')
time.sleep(0.2)
use('Color Lights')
time.sleep(0.2)
colorLightSetup('jandy', 4)
time.sleep(0.2)
use('Home')
time.sleep(0.2)
use('Other Devices')
time.sleep(0.2)
lightTest('jandy', 4)
use('Menu')
time.sleep(0.2)
use('System Setup')
time.sleep(0.2)
use('Color Lights')
time.sleep(0.2)
turnOffAuxLight('jandy', 4)
input('Press enter to continue when next test is set')
colorLightSetup('pentair', 4)
time.sleep(0.2)
use('Home')
time.sleep(0.2)
use('Other Devices')
time.sleep(0.2)
lightTest('pentair', 4)
time.sleep(0.2)
use('Menu')
time.sleep(0.2)
use('System Setup')
time.sleep(0.2)
use('Color Lights')
time.sleep(0.2)
turnOffAuxLight('pentair', 4)
input('Press enter to continue when next test is set')
colorLightSetup('hayward', 4)
time.sleep(0.2)
use('Home')
time.sleep(0.2)
use('Other Devices')
time.sleep(0.2)
lightTest('hayward', 4)
time.sleep(0.2)
use('Menu')
time.sleep(0.2)
use('System Setup')
time.sleep(0.2)
use('Color Lights')
time.sleep(0.2)
turnOffAuxLight('hayward', 4)
