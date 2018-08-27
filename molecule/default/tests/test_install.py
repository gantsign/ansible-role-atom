import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_atom(host):
    assert host.run('which atom').rc == 0


def test_apm(host):
    assert host.run('apm --version').rc == 0
