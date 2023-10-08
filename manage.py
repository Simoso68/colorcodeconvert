from sys import argv
from platform import system
from subprocess import run, check_output

if system() != "Linux":
    print("error: colorcodeconvert's manage tool only support Linux.")
    exit(1)

for arg in argv[1:]:
    if arg == "clean":
        run(["rm", "-rf", "colorcodeconvert/__pycache__", "dist", "build", "colorcodeconvert.egg-info"])
    elif arg == "build":
        run(["python3", "setup.py", "sdist", "bdist_wheel"])
    elif arg == "release":
        run(["twine", "upload", "dist/*"])
    else:
        print(f"error: unknown action '{arg}'")
        exit(1)