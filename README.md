Ansible Role: Atom
==================

[![Tests](https://github.com/gantsign/ansible-role-atom/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-atom/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.atom-blue.svg)](https://galaxy.ansible.com/gantsign/atom)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-atom/master/LICENSE)

Role to install the [atom.io](https://atom.io) text editor by GitHub.

Requirements
------------

* Ansible >= 2.9

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

        * Note: other versions are likely to work but have not been tested.

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
    atom_config_overwrite: yes # By default the config file will not be overwritten
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
            '*':
              core:
                projectHome: '/home/vagrant/workspace'
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

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
