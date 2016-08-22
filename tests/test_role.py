def test_atom(Command):
    assert Command('which atom').rc == 0

def test_apm(Command):
    assert Command('apm --version').rc == 0
