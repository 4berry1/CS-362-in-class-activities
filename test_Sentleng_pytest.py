import Sentleng

def test_calc_4():
    output = Sentleng.calc("i o u c p q")
    assert output == 6

def test_calc_5():
    output = Sentleng.calc("is this a palandrome")
    assert output == 4

def test_calc_6():
    output = Sentleng.calc("False")
    assert output == 1

def test_calc_7():
    output = Sentleng.calc("")
    assert output == 0
    