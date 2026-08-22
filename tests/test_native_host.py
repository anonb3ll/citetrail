import os
import stat
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_native_host_wrapper_creates_private_state_dir(tmp_path: Path) -> None:
    state_home = tmp_path / "state"
    env = {
        **os.environ,
        "HOME": str(tmp_path / "home"),
        "XDG_STATE_HOME": str(state_home),
    }
    previous_umask = os.umask(0o022)
    try:
        completed = subprocess.run(
            [str(ROOT / "scripts" / "citetrail-native-host")],
            input=b"",
            env=env,
            capture_output=True,
            timeout=5,
            check=False,
        )
    finally:
        os.umask(previous_umask)

    state_dir = state_home / "citetrail"
    log_file = state_dir / "native-host.log"
    assert completed.returncode == 0
    assert stat.S_IMODE(state_dir.stat().st_mode) == 0o700
    assert stat.S_IMODE(log_file.stat().st_mode) == 0o600


def test_package_exposes_a_single_version() -> None:
    from citetrail import __version__

    assert __version__ == "0.1.0"
