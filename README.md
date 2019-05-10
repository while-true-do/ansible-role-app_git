<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-app_git.svg)](https://github.com/while-true-do/ansible-role-app_git/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-app_git.svg)](https://github.com/while-true-do/ansible-role-app_git/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-app_git.svg)](https://github.com/while-true-do/ansible-role-app_git/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-app_git.svg)](https://github.com/while-true-do/ansible-role-app_git/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-app_git.svg)](https://travis-ci.com/while-true-do/ansible-role-app_git)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-app_git%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/app_git)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-app_git%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/app_git)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-app_git%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/app_git)

# Ansible Role: app_git

An Ansible Role to install and configure git (local or server).

## Motivation

[Git](https://git-scm.com/) is very commonly used for many open source projects.
Having a role, will help to ensure it is installed properly. The role can also
configure git as [git-server](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server).

## Description

This role installs git.

-   install git and git-svn
-   configure git as server (via ssh)

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible User Module](https://docs.ansible.com/ansible/latest/modules/user_module.html)
-   [Ansible File Module](https://docs.ansible.com/ansible/latest/modules/file_module.html)
-   [Ansible Lineinfile Module](https://docs.ansible.com/ansible/latest/modules/lineinfile_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/app_git)
```
ansible-galaxy install while_true_do.app_git
```

Install from [Github](https://github.com/while-true-do/ansible-role-app_git)
```
git clone https://github.com/while-true-do/ansible-role-app_git.git while_true_do.app_git
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.app_git

# Role can be client|server
wtd_app_git_role: "client"

wtd_app_git_package:
  - git
  - git-svn
# State can be present|latest|absent
wtd_app_git_package_state: "present"

# Below variables are only used for wtd_app_git_mode: "server"
wtd_app_git_dir: "/var/git"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.app_git
```

#### Advanced

Install git with capabilities to server repositories.

```
- hosts: all
  roles:
    - role: while_true_do.app_git
      wtd_app_git_role: "server"
```

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-app_git/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-app_git/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
