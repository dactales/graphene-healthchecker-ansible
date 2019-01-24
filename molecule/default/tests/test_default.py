import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_file(host):
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


@pytest.mark.parametrize("socket", ["tcp://127.0.0.1:8080"])
def test_socket(host, socket):
    s = host.socket(socket)
    assert s.is_listening


@pytest.mark.parametrize(
    "file",
    [
        "/home/healthcheck/healthcheck_healthcheck/uwsg.ini",
        "/home/healthcheck/healthcheck_healthcheck/config.yaml",
    ],
)
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize(
    "dir",
    [
        "/home/healthcheck/healthcheck_healthcheck/",
        "/home/healthcheck/healthcheck_healthcheck/env",
    ],
)
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


def test_service(host):
    s = host.service("graphene-healthchecks-healthcheck.service")
    assert s.is_enabled
    assert s.is_running
