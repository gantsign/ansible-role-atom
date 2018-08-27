import pytest
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('atom_package', [
    'minimap',
    'linter'
])
def test_packages(host, atom_package):
    cmd = 'sudo --user test_usr -H apm list --bare | grep -E %s'
    assert host.run(cmd, '^' + atom_package + '@').rc == 0
