from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_config(File):
    config_file = File('/home/test_usr/.atom/config.cson')

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'test_usr'
    assert config_file.group == 'test_usr'
    assert oct(config_file.mode) == '0600'
    assert config_file.contains('"projectHome": "/home/vagrant/workspace"')
