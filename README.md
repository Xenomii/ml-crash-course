# Introduction
This repository contains code for [Machine Learning A-Z™: Hands-On Python & R In Data Science](https://nlbsg.udemy.com/course/machinelearning/learn/lecture/19229276#overview) Udemy course.

# Requirements
To run this project, you will need to install [Python 3.9.15](https://www.python.org/downloads/release/python-3915/). 

You can use [pyenv](https://github.com/pyenv/pyenv) to install and manage different versions of Python if you do not have the specified version installed on your machine.

You can also use [Poetry](https://python-poetry.org/) to easily install and manage the Python packages that are used for the project.

Follow the guide below to install both pyenv and Poetry. This guide assumes you are using a Linux operating system (preferrably Ubuntu).
## Pyenv
Run the command below to install some dependencies required by pyenv:
```
sudo apt-get install -y git gcc make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev zlib1g-dev libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev
```
Execute the command below to install pyenv onto your machine:
```
curl https://pyenv.run | bash
```

<strong>You should get a warning stating that you have not added pyenv to the load path.</strong>

Use your preferred editor to write to the appropriate shell file that you are using (i.e., .bashrc, .zsh, etc):
```
sudo nano ~/.bashrc
```

Copy the text below and paste it at the bottom of the file:
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Once that is done, restart your shell:
```
exec $SHELL
```

Run this command to ensure that you have installed pyenv correctly:
```
pyenv update
```

## Python
Once you have installed pyenv, you can begin using it to install and manage the specified version of Python required for this project.

To install the required version of Python using pyenv, run the command below:
```
pyenv install 3.9.15
```

To ensure that you are using that version of Python, run this command:
```
pyenv global 3.9.15
```

## Poetry
A tool for dependency management and packaging in Python. You can declare the libraries your project depends on and it will manage them for you.

To install it onto your machine, run this command:
```
curl -sSL https://install.python-poetry.org | python3 -
```

Proceed to add Poetry to your PATH by editing your shell file:
```
sudo nano ~/.bashrc
```

Copy and paste the following at the end of your shell file:
```
export PATH="/home/xenome/.local/bin:$PATH"
```

After that, restart your shell:
```
exec $SHELL
```

Test that Poetry is working by running this command:
```
poetry --version
```

Before you set-up the virtual environment, you would need to configure Poetry to find the current Python version of your shell:
```
poetry config virtualenvs.prefer-active-python true
```

After this, you can install the dependencies that you need by running:
```
poetry install
```
This will auto-create a virtual environment and install the necessary Python packages outlined in `pyproject.toml`.

You can access said virtual environment by running this command:
```
poetry shell
```

This command however, is quite buggy at times and an alternative for this command is to run this:
```
source $(poetry env info --path)/bin/activate
```

# Running the Project
Before you can run the project, you must first clone the repository and install the required Python dependencies.

## Clone GitHub Repository
Ensure that you select an appropriate directory to place the project into before cloning:
```
cd /path/to/project/directory
git clone https://github.com/ICT3204/Coursework-2
```

## Dependencies
Move into the cloned repository and install the required dependencies:
```
cd ml-crash-course
poetry install
```

## Desktop Application
Once that is done, you can run the desktop application by executing the main Python file:
```
cd /path/to/section
python pythonfile.py
```