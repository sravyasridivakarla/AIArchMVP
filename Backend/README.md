# AIArchMVP

set up a virtual environment

```
python -m venv /path/to/new/virtual/environment
```

activate the virtual environment

```
source /path/to/new/virtual/environment/bin/activate
```

install the dependencies

```
pip install -U pymilvus
pip install "pymilvus[model]"
pip install "fastapi[standard]"
pip install dependency-injector

```

OR

```
pip install -r requirements.txt
```

Run the script

```
python quickstart.py

OR

uvicorn Backend.main:app --reload
```
