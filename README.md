mobn
A tool for mob programming.

# Setup

```bash
git clone git@github.com:tapegram/mobn.git
ln -s <PATH_TO_MOBN>/mobn /usr/local/bin/mobn
```
Set up your preferred workstream via an environment variable. For example.
```bash
export MOBN_WORKSTREAM_NAME=matcha-mob
```

# Usage

```bash
mobn new        # start a new work stream
mobn continue   # start your turn on an already created work stream
mobn done pr123 # ready to create PR, put all of the commits on to a new branch called `pr123`
mobn help       # for help!
```

Additionally, you can provide the team members when starting the session so the mob tool will take care of whos turn it is.
```bash
mobn new tom dick harry
```

# Dev requirements

Make sure you have pip3
```bash
python3 -m pip install --upgrade pip
```
And virtualenv
```bash
sudo pip3 install virtualenv
```

# Create a virtual env (if you haven't already)
```bash
virtualenv -p /usr/bin/python3 venv
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Running tests
From your virtual env run `pytest`