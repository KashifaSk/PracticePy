from application import get_op_sys
import pytest

def test_get_op_sys(mocker):
    #Mock the slow function and return true
    mocker.patch('application.is_windows', return_value = True)
    assert get_op_sys()=='Windows'