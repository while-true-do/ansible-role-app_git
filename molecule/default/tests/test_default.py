import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_git_package(host):
    pkg = host.package('git')
    assert pkg.is_installed


def test_git_svn_package(host):
    pkg = host.package('git-svn')
    assert pkg.is_installed


def test_git_shell(host):
    file = host.file('/etc/shells')
    assert file.contains('/usr/bin/git-shell')


def test_git_user(host):
    user = host.user('git')
    assert user.name == 'git'
    assert user.shell == '/usr/bin/git-shell'
    assert user.password == '!!'


def test_git_group(host):
    group = host.group('git')
    assert group.exists


def test_git_directory(host):
    dir = host.file('/git')
    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'git'
    assert dir.group == 'git'
    assert oct(dir.mode) == '0o770'
