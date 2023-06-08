from selene.support.shared import browser
from selene import be, have


def test_xyz_bank():
    browser.open('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    browser.element('[ng-click="customer()"]').click()
    browser.element('[id="userSelect"]').click()
    browser.element('[value="2"]').click()
    browser.element('[class="btn btn-default"]').click()
    browser.element('[id="accountSelect"]').click()
    browser.element('[value="number:1006"]').click()
    browser.element('[ng-class="btnClass1"]').click()
    browser.element('[ng-click="back()"]').click()
    browser.element('[ng-click="deposit()"]').click()
    # browser.element('[class="form-control ng-pristine ng-invalid ng-invalid-required ng-touched"]').send_keys("10000")
    # browser.element('[class="btn btn-default"]').click()
