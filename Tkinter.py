import subprocess

def install_tkinter():
    try:
        # Check if Tkinter is already installed
        import tkinter

        print("Tkinter is already installed.")

    except ImportError:
        # Install Tkinter using the appropriate package manager
        try:
            subprocess.check_call(['pip', 'install', '--user', 'tk'])
            print("Tkinter installed successfully.")

        except subprocess.CalledProcessError:
            print("Error installing Tkinter. Please check your internet connection and try again.")

if __name__ == '__main__':
    install_tkinter()
