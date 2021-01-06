import os


def uninstall():
    try:
        from IPython.terminal.interactiveshell import TerminalInteractiveShell

        startup_dir = TerminalInteractiveShell.instance().get_ipython().profile_dir.startup_dir
        script = os.path.join(startup_dir, '90-ipypandex.py')
        if os.path.exists(script):
            os.remove(script)
            print(f"Script {script} removed")
        else:
            print(f"Script {script} already removed")
    except ModuleNotFoundError:
        # All good, ipython is already removed
        print("IPython is already removed from this installation")


if __name__ == '__main__':
    uninstall()
