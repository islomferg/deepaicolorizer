# <p align="center">deepaicolorizer

## Getting started.
```
$ pip install deepaicolorizer
```

## Colorize photos example
```python
import colorizer

api = colorizer.Colorizer('Token https://deepai.org')
print(api.colorizeByFile(open('test.png', 'rb')))
print(api.colorizeByImageUrl('https://www.python.org/static/img/python-logo.png'))
```