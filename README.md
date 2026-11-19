# Assignment 7 Iris CI/CD

The project trains a logistic regression classifier and checks held-out accuracy. The workflow installs dependencies, checks Python syntax, runs pytest and executes the model. The deployment step prints two messages and runs after successful tests on a push to main. Pull requests into main run the checks.

## Run locally

Open PowerShell in the Assignment 7 directory:

```powershell
python -m pip install -r requirements.txt
python -m compileall -q app.py src tests
python -m pytest -v
python app.py

$env:MIN_MODEL_ACCURACY = '0.99'
python -m pytest -v
Remove-Item Env:MIN_MODEL_ACCURACY
python -m pytest -v
```

The stricter threshold is the negative control. The default threshold is 0.80.

## Run on GitHub

Create a dedicated repository named mlops-cicd. At its root, place the seven project files, retaining the .github/workflows, src and tests directories. Push the project to main and open Actions to observe the test and simulated deployment jobs.

For the failure demonstration, change MIN_MODEL_ACCURACY in .github/workflows/ci-cd.yml to 0.99 in a dedicated lab commit on main. Check that the test fails and deployment is skipped. Restore 0.80 in a follow-up commit and confirm the jobs pass. A pull request into main can demonstrate CI without deployment.
