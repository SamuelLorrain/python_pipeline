# Pipeline

A simple implementation of the pipeline pattern in python

It has been inspired by the use of operator overloading in `pathlib`

It's a toy project.

## Usage

For basic pipeline implementation:

```python
from pipeline import Pipeline
# define auxilliary methods
# used to transform the entry data
def x(s):
    return "-" + s + "-"

def y(s):
    return "_" + s + "_"

def z(s):
    return "~" + s + "~"

# define a Pipeline using the
# Pipeline class, and append multiple
# functions to transform the given entry
# data
pipeline = Pipeline("i") | x | y | x | y | z | x | y | z

# call the pipeline
pipeline()
# result:
#   ~_-~_-_-i-_-_~-_~
```

From stream based pipeline, which define `read` and `readline` methods

```python
from pipeline import Pipeline
# define auxilliary methods
# used to transform the entry data
def x(s):
    return "-" + s + "-"

def y(s):
    return "_" + s + "_"

def z(s):
    return "~" + s + "~"

# define a StreamPipeline using the
# StreamPipeline class, and append multiple
# functions to transform the given entry
# data
spipeline = StreamPipeline("i") | x | y | x | y | z | x | y | z

# call the pipeline
while i := spipeline.read():
    print(i)
```

## Todo

- packaging
- testing
- assign pipeline to a context manager ?
