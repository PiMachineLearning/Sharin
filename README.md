# Sharin
PEP 503 compliant static pip repository generator.<br>
Supports hashing whl files and putting those on the URL fragment as recommended by PEP 503.<br>

## Usage
Place all your files inside the directory wheels using the following system
```
main.py
wheels/
  <project name>/
    file.whl
```
Sharin will generate a folder called `dist` that has all the necessary files for it to function as a pip repository
The folder tree for the output may look like
```
dist/
  <project name>/
    file.whl
    index.html
  index.html
```
for the example above.
