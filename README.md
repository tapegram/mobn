mobn
A tool for mob programming.

# Setup

```
git clone git@github.com:tapegram/mobn.git
ln -s <PATH_TO_MOBN>/mobn /usr/local/bin/mobn
```
Set up your preferred workstream via an environment variable. For example.
```
export MOBN_WORKSTREAM_NAME=matcha-mob
```

# Usage

```
mobn new       # start a new work stream
mobn continue  # start your turn on an already created work stream
mobn done      # ready to create PR
mobn help      # for help!
```

# Dev requirements

Make sure you have pip3
```
python3 -m pip install --upgrade pip
```
And virtualenv
```
sudo pip3 install virtualenv
```

# Create a virtual env (if you haven't already)
```
virtualenv -p /usr/bin/python3 venv
```

# Install dependencies
```
pip install -r requirements.txt
```

# Running tests
From your virtual env run `pytest`