from pages.LoginPage.LoginPage import LoginPage
import pytest
import allure



class Test_login:
    @pytest.mark.run(order=0)

    def test_login(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("13003895886","Zlin@5886.")

