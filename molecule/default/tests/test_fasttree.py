def test_fasttree(host):
    """
    Check fasttree version.
    """
    cmd = "FastTreeDblMP"
    cmd_result = host.run(cmd)
    assert cmd_result.rc == 0, "'{}' returned status {}.".format(cmd, cmd_result.rc)
    assert "FastTree 1.2.3.4.5" in cmd_result.stdout, f"'{cmd}' returned stdout '{cmd_result.stdout}', stderr '{cmd_result.stderr}'"
