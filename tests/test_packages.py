import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('atom_package', [
    'minimap',
    'linter'
])
def test_packages(Command, atom_package):
    cmd = 'sudo --user test_usr -H apm list --bare | grep -E %s'
    assert Command(cmd, '^' + atom_package + '@').rc == 0
