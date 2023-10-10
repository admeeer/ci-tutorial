# test_script.py
import subprocess

def test_hello_world_output(capfd):
    subprocess.run(['python', './script.py'])
    
    # Capture the output
    captured = capfd.readouterr()

    # Assert the output is correct
    assert captured.out == "Hello, World!\n"
