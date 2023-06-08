from selene.support.shared import browser
from faker import Faker
fake_data = Faker("ru_RU")

def test_demoqa_element_text_box():
    browser.open('https://demoqa.com/text-box')
    browser.element('[id="userName"]').type(fake_data.first_name())
    browser.element('[id="userEmail"]').type(fake_data.email())
    browser.element('[id="currentAddress"]').send_keys("What is love")
    browser.element('[id="permanentAddress"]').send_keys("baby dont hert me")
    browser.element('[id="submit"]').click()