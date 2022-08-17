import pytest

from Pages.registrationPage import Registration
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider




class Test_Registration(BaseTest):

    @pytest.mark.parametrize("name, phone, email, country, city, username, password", dataProvider.data_provider("Registration"))
    def test_fill_up_registration_form(self, name, phone, email, country, city, username, password):

        Reg = Registration(self.driver)
        Reg.fill_form(name, phone, email, country, city, username, password)
