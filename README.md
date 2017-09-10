Ansible Role: Atom
==================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-atom.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-atom)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.atom-blue.svg)](https://galaxy.ansible.com/gantsign/atom)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-atom/master/LICENSE)

Role to install the [atom.io](https://atom.io) text editor by GitHub.

Requirements
------------

* Ansible >= 2.0
* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Users to install packages for and/or write config.cson
users: []
```

Users are configured as follows:

```yaml
users:
  - username: # Unix user name
    atom_packages:
      - # package 1
      - # package 2
    atom_config: # The config (in YAML not CSON)
    atom_config_overwrite: yes # By defult the config file will not be overwritten
```

Example Playbooks
-----------------

Minimal playbook:

```yaml
- hosts: servers
  roles:
    - role: gantsign.atom
```

Playbook with packages installed and config:

```yaml
- hosts: servers
  roles:
    - role: gantsign.atom
      users:
        - username: vagrant
          atom_packages:
            - minimap
            - linter
            - atom-beautify
            - file-icons
          atom_config:
            "*":
              core:
                projectHome: "/home/vagrant/workspace"
              editor:
                showIndentGuide: true
                showInvisibles: true
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
