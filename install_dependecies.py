import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    # List of packages to install
    packages = ["PyQt5", "pyglet"]

    for package in packages:
        print(f"Installing {package}...")
        install(package)

    print("All dependencies have been installed!")
