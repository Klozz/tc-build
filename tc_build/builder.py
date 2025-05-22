#!/usr/bin/env python3

import shlex
import shutil
import subprocess
import tc_build.utils


class Folders:

    def __init__(self):
        self.build = None
        self.install = None
        self.source = None


class Builder:

    def __init__(self):
        self.folders = Folders()
        self.show_commands = False

    def build(self):
        raise NotImplementedError

    def clean_build_folder(self):
        if not self.folders.build:
            raise RuntimeError('No build folder set?')

        if self.folders.build.exists():
            if self.folders.build.is_dir():
                shutil.rmtree(self.folders.build)
            else:
                self.folders.build.unlink()

    def run_cmd(self, cmd, capture_output=False, check=True, cwd=None, quiet=False):
        # Siempre imprime el comando completo para depuración
        tc_build.utils.print_info(f"Executing command: {' '.join(shlex.quote(str(elem)) for elem in cmd)}")
        
        if self.show_commands:
            # Acts sort of like 'set -x' in bash
            print(f"$ {' '.join([shlex.quote(str(elem)) for elem in cmd])}", flush=True)
        return subprocess.run(cmd, capture_output=capture_output, check=check, cwd=cwd)
