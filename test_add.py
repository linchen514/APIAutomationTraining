import pytest
import os
import json
import yaml

data = yaml.safe_load(open("test_add_data.yml"))
cases = []
testdatas = []


for icases in data['businessTests']:
    cases.append(icases.get('casename', ''))
    testdatas.append(icases.get('testdata', {}))

#print(cases)
#print(testdatas)

# print(data)



def add(x, y):
    return x + y


class Test_add:
    @pytest.mark.parametrize('x, y, expect', testdatas, ids=cases)
    @pytest.mark.add
    @pytest.mark.functiontest
    def test_business_add(self, x, y, expect):
        assert add(x, y) == expect

    #
    # @pytest.mark.add
    # @pytest.mark.smoketest
    # @pytest.mark.functiontest
    # def test_business_zore(self):
    #     assert add(0, 0) == 0
    #
    # @pytest.mark.add
    # @pytest.mark.functiontest
    # def test_business_positive(self):
    #     assert add(1, 9) == 10
    #
    # @pytest.mark.add
    # @pytest.mark.functiontest
    # def test_business_negative(self):
    #     assert add(-1, -9) == -10
    #
    # @pytest.mark.add
    # @pytest.mark.functiontest
    # def test_business_bignumber(self):
    #     assert add(999999999, 1000000000) == 1999999999
    #
    # @pytest.mark.add
    # @pytest.mark.functiontest
    # def test_business_possitive_and_negative(self):
    #     assert add(10, -80) == -70
    #
    # @pytest.mark.inc
    # @pytest.mark.illegalinputtest
    # @pytest.mark.xfail(raises=TypeError, reason="illegal input")
    # def test_business_illegalinput(self):
    #     assert add('a', 1) == "a1"
