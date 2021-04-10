from dz_phone_numbers import DzPhoneNumber
import pytest 


def test_invalid_numbers():
    with pytest.raises(ValueError):
        DzPhoneNumber('0550abcdef')
   