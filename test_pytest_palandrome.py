import palandrome

def test_calc_4():
    output = palandrome.calc("racecar")
    assert output == 1

def test_calc_5():
    output = palandrome.calc("is this a palandrome")
    assert output == 0

def test_calc_6():
    output = palandrome.calc("False")
    assert output == 1