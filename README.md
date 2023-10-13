# test-automation workflow tutorial
![Workflow](https://github.com/admeeer/cicd-tutorial/actions/workflows/build_and_test.yml/badge.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This tutorial is designed to get you up and running with GitHub Actions to automate your project's software lifecycle. GitHub Actions versatility extend much further, but this tutorial focuses specifically on automating the build and test phases of an application.

## Table of Contents
- [Forking the repository](#forking-the-repository)
- [Executing the default workflow](#executing-the-default-workflow)
- [Customizing output and test validation](#customizing-output-and-test-validation)
- [Modifying the workflow to extract and archive artifacts](#modifying-the-workflow-to-extract-and-archive-artifacts)
- [Workflow gists](#workflow-gists)

## Forking the repository
First, you'll need to fork the repository - giving you a personal copy. 

- Fork the repository
   1. Navigate to the repository: `https://github.com/admeeer/cicd-tutorial`
   2. In the top right, click the dropdown next to `Fork` and click `Create a new fork`
   3. Click `Create fork`

## Executing the default workflow
These steps show you how to run the default workflow and help get you used to interacting with GitHub Actions. This tutorial assumes you have forked the repository. 

- Run the workflow
   1. Navigate to the `Actions` tab
   2. On the left, click on the `manual-build-and-test-automation` workflow
   3. On the right, click `Run workflow` and then `Run workflow`
- Check the workflow success
   1. Click the topmost workflow
   2. Success (hopefully!)

## Customizing output and test validation

These steps show you how to clone the repository onto your local machine, personalize the output and test validation, and then push your changes up to your GitHub fork. After, we'll view the workflow executing your new changes.

**The ocky way**. This tutorial assumes you have forked the repository and installed a Python interpreter and Git. See https://git-scm.com/ and https://www.python.org/downloads/ for further information. 

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

## Modifying the workflow to extract and archive artifacts

These steps run you through modifying the tests and default workflow to capture pytest output to a file and then upload that output as artifacts to GitHub. This tutorial assumes you have forked the repository.

- Open the workflow
  1. Navigate to repository and open the default workflow file, `.github/build_and_test.yml`.
- Direct pytests output to a file
  1. Under the `test` step, change `pytest -v tests/` to `pytest -v tests/ | tee tests/test_output.txt`. This will tell pytest to direct its output to both the console AND an output file in tests/test_output.txt.
- Add a new step
  1. Investigate the other steps and then create one under the last step, `test`. Add a keyword `name:` and name the new step `upload test artifacts`. This step should be completely under the `test` step and its instructions. It should be similar to this:
  
![image](https://github.com/admeeer/cicd-tutorial/assets/6462261/76281de5-aad4-40a4-83ab-d74aa2e6c069)

  3. Under the `name` of the step, add another keyword called `uses:`. Here, we'll use a predefined GitHub Action that uploads artifacts based on a few parameters that we'll set. Add `actions/upload-artifact@v2` to the right of the keyword. Your new step should be similar to this:

![image](https://github.com/admeeer/cicd-tutorial/assets/6462261/6ba1dbf4-ac7d-4285-8b20-b0de554b0f31)

  5. Under the `uses` of the step, add another keyword called `with`. This keyword defines the parameters of our artifacts. Under `with`, add two indented keywords, `name` and `path`. Set the `name` to something like `test-output`, this will be the name of the artifacts generated. Set `path` to `tests/test_output.txt`. Your step is now completed and with luck, looks something like this:

![image](https://github.com/admeeer/cicd-tutorial/assets/6462261/b17b84e0-b9dc-4933-8d9e-2b3fdfd90c3a)

- Commit your changes
  1. In the top right of the web browser, click `Commit changes`. Add a descriptive commit message, like `Added artifact extraction and capture to workflow` and then click `Commit changes`.
- Check the workflows success
  1. Navigate to the `Actions` tab
  2. On the left, click on the `build-and-test-automation` workflow
  3. Click the topmost workflow
  4. Success (hopefully!)







## Workflow gists

**Stuck?** These gists are what your workflows should look like. 
- **The default workflow** https://gist.github.com/admeeer/4e449981a730fa016d0780a335b9248d
- **The extended workflow with artifact extraction and archival** https://gist.github.com/admeeer/383f82bbdfdc5fe5f5998e7657945c95

