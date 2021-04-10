from dz_phone_numbers import DzPhoneNumber
import pytest

def test_phone_carrier():
    with pytest.raises(ValueError):
        phone_number1 = DzPhoneNumber('055012llsd')
        phone_number2 = DzPhoneNumber('06501')
        phone_number3 = DzPhoneNumber('0750123')
        phone_number1.is_ooredoo()
        phone_number2.is_mobilis()
        phone_number3.is_djezzy()