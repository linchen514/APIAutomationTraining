import pytest


def inc(x):
    return x + 1


class Test_inc:
    @pytest.mark.inc
    @pytest.mark.smoketest
    @pytest.mark.functiontest
    def test_business_zore(self):
        assert inc(0) == 1

    @pytest.mark.functiontest
    def test_business_positive(self):
        assert inc(9) == 10

    @pytest.mark.functiontest
    def test_business_negative(self):
        assert inc(-1) == 0

    @pytest.mark.functiontest
    def test_business_bignumber(self):
        assert inc(999999999) == 1000000000

    @pytest.mark.functiontest
    @pytest.mark.illegalinputtest
    @pytest.mark.xfail(raises=TypeError, reason="illegal input")
    def test_business_illegalinput(self):
        assert inc('a') == "a1"
