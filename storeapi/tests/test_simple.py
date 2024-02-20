def test_add_two():
    x = 1
    y = 2
    assert x+y == 3

def test_dict_content():
    x = {"a":1,"b":2}
    expected = {"a":1}
   # assert expected.items() <= x.items()
    assert all(item in x.items() for item in expected.items())
    
    