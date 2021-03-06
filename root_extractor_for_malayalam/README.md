# Root Extractor for Malayalam

Extracting root of a word is vital in the preprocessing stage of most Language processing systems for Malayalam. The root extraction module can derive the root of any given words regardless of the number of suffixes or words attached with the stem.

### Requirement

Python3

### Installation

You may create a virtual environment for installing the package.
```
python -m venv ENV_DIR
source ENV_DIR/bin/activate
```
and install the root extractor

```
pip install root-pack
```

Otherwise, use

```
pip install --user root-pack
```
### Implementation method

After installation, you can import the module to utilize the root() function

```
import root_pack
root_pack.root(wordi)
```
The above code will output the root of the input word *wordi*. The input word must be given in Malayalam.

For example,

if you need to find the root of the word "മകന്റെയുമാണെന്നാണ്", you may follow the below steps

```
import root_pack
root_pack.root("മകന്റെയുമാണെന്നാണ്")
```
Output:
```
മകന്‍
```

### Advantages of the extractor

1. Sandhi rules are taken into consideration
2. Rules are generalized rather than explicitly specifying each in the code
3. Recursive functions introduced and thus aids to strip any number of suffixes attached with ease
4. Accuracy rate is quite high
