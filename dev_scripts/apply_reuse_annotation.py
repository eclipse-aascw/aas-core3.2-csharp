# SPDX-FileCopyrightText: 2026 2026 aas-core3.2-csharp AUTHORS
#
# SPDX-License-Identifier: MIT

"""Apply the REUSE annotation for the generated code."""

import os
import pathlib
import subprocess
import sys

_LICENSE = "MIT"

_COPYRIGHT = "2026 aas-core3.2-csharp AUTHORS"


def main() -> int:
    """Execute the main routine."""
    repo_root = pathlib.Path(os.path.realpath(__file__)).parent.parent

    src_dir = os.path.relpath(str(repo_root / "src" / "AasCore.Aas3_2"), os.getcwd())
    test_dir = os.path.relpath(
        str(repo_root / "src" / "AasCore.Aas3_2.Tests"), os.getcwd()
    )

    subprocess.run(
        [
            sys.executable,
            "-m",
            "reuse",
            "annotate",
            "--copyright",
            _COPYRIGHT,
            "--license",
            _LICENSE,
            "-r",
            src_dir,
            test_dir,
        ],
        check=True,
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
