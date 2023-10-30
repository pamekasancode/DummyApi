from pathlib import Path
import sys
import subprocess


TEST_DIR = Path("tests", "django").resolve()

if sys.platform == "win32":
    exec(f"'{Path(TEST_DIR, 'Scripts', 'activate.bat').resolve()}'")

else:
    # exec(f"source '{Path(TEST_DIR, 'bin', 'activate').resolve()}'")
    subprocess.Popen(["/usr/bin/python3", Path(TEST_DIR, 'bin', 'activate_this.py').resolve()])

# exec(open(Path(TEST_DIR, "testing", "manage.py").resolve()).read())


