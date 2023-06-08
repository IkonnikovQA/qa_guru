from selene.support.shared import browser
from selene import be, have

def test_demoqa_check_box():
    browser.open('https://demoqa.com/checkbox')
    browser.element('[class="rct-icon rct-icon-expand-close"]').click()