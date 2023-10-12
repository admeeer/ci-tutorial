# test-automation workflow tutorial
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



### Getting started
These steps show you how to run the default workflow and help get you used to interacting with GitHub Actions.
- Fork the repository
   1. Navigate to the repository: `https://github.com/admeeer/cicd-tutorial`
   2. In the top right, click the dropdown next to `Fork` and click `Create a new fork`
- Run the workflow
   1. Navigate to the `Actions` tab
   2. On the left, click on the `manual-build-and-test-automation` workflow
   3. On the right, click `Run workflow` and then `Run workflow`
- Check the workflow success
   1. Click the topmost workflow
   2. Success (hopefully!)

### Customizing the tests

This tutorial assumes you have installed a Python interpreter and Git. See https://git-scm.com/ and https://www.python.org/downloads/ for further information.
- Clone the repository
  1. Run `git clone https://github.com/admeeer/cicd-tutorial.git`
- Navigate to the cloned directory
  1. Run `cd cicd-tutorial`
- Customize
  1. Open `script.py` and edit the input in the `print` statement
  2. Navigate to the `tests/` folder, run `cd tests/`
  3. Open `test_script.py` and edit the assert to your input
- Optionally, test locally
  1. Update pip, run `python3 -m pip install --upgrade pip`
  2. Then, run `pip3 install pytest`
  3. If in `tests/`, run `pytest test_script.py`, else, in the directory, run `pytest tests/`
- Push your local changes up to GitHub
  1. Run `git add *`, note: if you modified any other files, this command will capture those changes too
  2. Run `git commit -m "Customized output and modified test to assert towards new output"`
  3. Run `git push`
- Check the workflows success
  1. Navigate to the `Actions` tab
  2. On the left, click on the `build-and-test-automation` workflow
  3. Click the topmost workflow
  4. Success (hopefully!)
