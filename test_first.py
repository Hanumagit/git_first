import math

def testfisrst():
    num=64
    assert math.sqrt(num)==8

def test_second():
    name="hanumantha rao"
    assert name=="hanumantha rao"

def test_third():
    name="hanu"
    assert len(name)==4

def test_fourth():
    name="john"
    assert name is "john"

def testfifth():
    name="hanuman"
    output=name.replace("n"," ",1)
    assert output == "ha uman"

def test_sixth():
    name="hanuman"
    output1=name.upper()
    assert output1 == "HANUMAN"

def test_seventh():
    name="hanumantha rao"
    assert name[:3] == 'han'

def test_eighth():
    name="hanuman"
    assert name.count('a') == 2

def test_nineth():
    name="hanuman"
    assert name.capitalize() == "Hanuman"

def test_tenth():
    name="hanumantha Rao"
    assert name.title() == "Hanumantha Rao"

def test_split():
    name="hanuman"
    output = name.split()
    assert output == ['hanuman']
