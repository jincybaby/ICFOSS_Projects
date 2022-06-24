# Morpheme Generator for Malayalam

The Morpheme Generator helps to obtain a list with the stem and stripped suffixes from a given input word. 

### Requirement

Python3

### Installation

You may create a virtual environment for installing the package.

```
python -m venv ENV_DIR
source ENV_DIR/bin/activate
```

Install the morpheme generator

```
pip install morph-gen
```

Otherwise, use

```
pip install --user morph-gen
```

### Implementation

After installation, you can import the module to utilize the morph() function

```
import morph_gen
morph_gen.morph(wordi)
```
The above code will output the root of the input word *wordi*. Please note that the input word must be given in Malayalam.

For example,

if you need to find the root of the word "മകന്റെയുമാണെന്നാണ്", you may follow the below steps

```
import morph_gen
morph_gen.morph("മകന്റെയുമാണെന്നാണ്")
```
Output:
```
['മകന്‍ ', 'ന്റെ', 'ഉം', 'ആണ്', 'എന്ന്', 'ആണ്']
```

# Creators
* Jincy Baby

# Contribution
* Dr. Abrar K J, Research Fellow ICFOSS, Contributed to familiarize the grammatical rules of Malayalam Language
 

## Project Guidence and Support
Dr. Rajeev RR, Program Head, ICFOSS

# Developers 
This project is  developed by ICFOSS

## Licensed under GNU GPL v3.0.
