# test_script.py
import subprocess

def test_script_output(capfd):
    # run the script file under a new process
    subprocess.run(['python', './script.py'])
    
    # Capture process output
    captured = capfd.readouterr()

    # Assert the output is correct
    assert captured.out == "Hello, World!\n"
