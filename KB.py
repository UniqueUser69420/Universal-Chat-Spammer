import subprocess

def install_keyboard():
    try:
        subprocess.check_call(['pip', 'install', 'keyboard'])
        print("keyboard library installed successfully!")
    except subprocess.CalledProcessError:
        print("An error occurred while installing the keyboard library.")

if __name__ == "__main__":
    install_keyboard()