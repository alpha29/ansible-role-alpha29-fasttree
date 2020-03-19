def test_fasttree(host):
    """
    Check fasttree version.
    """
    cmd = "FastTreeDblMP"
    cmd_result = host.run(cmd)
    # FastTreeDblMP returns a non-standard exit status...?
    assert cmd_result.rc == 1, "'{}' returned status {}.".format(cmd, cmd_result.rc)
    assert "FastTree Version 2.1.10 Double precision" in cmd_result.stderr, f"'{cmd}' returned stdout '{cmd_result.stdout}', stderr '{cmd_result.stderr}'"
