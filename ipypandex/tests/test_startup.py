import os
from subprocess import Popen, PIPE

from IPython.testing.tools import get_ipython_cmd, default_argv


def ipexec(fname, options=None, commands=()):
    """
    Shamelessly stolen from ipython tests but without relative path requirements
    """
    if options is None: options = []

    cmdargs = default_argv() + options

    ipython_cmd = get_ipython_cmd()
    full_cmd = ipython_cmd + cmdargs + ['--', fname]
    print(full_cmd)
    env = os.environ.copy()
    # FIXME: ignore all warnings in ipexec while we have shims
    # should we keep suppressing warnings here, even after removing shims?
    env['PYTHONWARNINGS'] = 'ignore'
    # env.pop('PYTHONWARNINGS', None)  # Avoid extraneous warnings appearing on stderr
    for k, v in env.items():
        # Debug a bizarre failure we've seen on Windows:
        # TypeError: environment can only contain strings
        if not isinstance(v, str):
            print(k, v)
    p = Popen(full_cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE, env=env)
    out, err = p.communicate(input='\n'.join(commands) or None)
    return out, err


def test_startup_pandas_vdn_json_output():
    """
    If this package is installed, a startup script will turn on
    echoing 'application/vnd.dataresource+json' as a display output
    for pandas.
    """
    out, err = ipexec(os.path.join(os.path.dirname(__file__), 'echo_pandas.py'))
    assert 'application/vnd.dataresource+json' in out.decode(), err.decode()
