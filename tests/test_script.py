# test_script.py
import subprocess
import sys

def test_script_output(capfd):
    # Run the script file under a new process using the same Python interpreter
    subprocess.run([sys.executable, './script.py'])
    
    # Capture process output
    captured = capfd.readouterr()

    # Assert the output is correct
    assert captured.out == "Hello, World!\n"
