def test_atom(host):
    assert host.run('which atom').rc == 0


def test_apm(host):
    assert host.run('apm --version').rc == 0
