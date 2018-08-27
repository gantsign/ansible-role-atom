import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config(host):
    config_file = host.file('/home/test_usr/.atom/config.cson')

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'test_usr'
    assert config_file.group == 'test_usr'
    assert oct(config_file.mode) == '0600'
    assert config_file.contains('"projectHome": "/home/vagrant/workspace"')


def test_perserve_config(host):
    config_file = host.file('/home/test_usr4/.atom/config.cson')

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'test_usr4'
    assert config_file.group == 'test_usr4'
    assert oct(config_file.mode) == '0600'
    assert config_file.contains('Existing config')


def test_overwrite_config(host):
    config_file = host.file('/home/test_usr5/.atom/config.cson')

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'test_usr5'
    assert config_file.group == 'test_usr5'
    assert oct(config_file.mode) == '0600'
    assert config_file.contains('"projectHome": "/home/vagrant/workspace"')

    backup_path = host.check_output('find %s | grep --color=never -E %s',
                                    '/home/test_usr5/.atom/',
                                    '~$')
    backup_file = host.file(backup_path)

    assert backup_file.is_file
    assert oct(backup_file.mode) == '0600'
    assert backup_file.contains('Existing config')
