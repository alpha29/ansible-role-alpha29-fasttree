def test_fasttree(host):
    """
    Check fasttree version.
    """
    cmd = "FastTreeDblMP"
    cmd_result = host.run(cmd)
    assert cmd_result.rc == 0, "'{}' returned status {}.".format(cmd, cmd_result.rc)
    assert "FastTree Version 2.1.10 Double precision" in cmd_result.stderr, f"'{cmd}' returned stdout '{cmd_result.stdout}', stderr '{cmd_result.stderr}'"
