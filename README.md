# Bootstrapy


Bootstrapy is a minimal and powerful interface to print colored text and labels in the terminal. Python 2 and Python 3 support.


## Examples

#### Colors

[![Bootstrapy colors](https://i.postimg.cc/L8XrW3D3/colors.png)](https://postimg.cc/XpRHGFTr)

#### Backgrounds

[![Bootstrapy backgrounds ](https://i.postimg.cc/pdvKTqSD/bgs.png)](https://postimg.cc/68H8bLt3)

#### Styles

[![Bootstrapy styles](https://i.postimg.cc/t4qxGYn5/styles.png)](https://postimg.cc/w7rvhxVy)

#### Labels

[![Bootstrapy labels](https://i.postimg.cc/j5s68ZQs/labels.png)](https://postimg.cc/rdPtsGPb)


### Installation
You can install `bootstrapy` with **pip** as follows:
```
pip install bootstrapy
```

### Usage
First of all, import everything that bootstrapy has to offer as follows:

```python
from bootstrapy import Strapy
```

Printing colored text is as simple as doing

```python
print(Strapy.RED+ "Lorem ipsum dolor sit amet" + Strapy.END)
```

Easy right?
But what if you want to print italic text?
You can simply do this

```python
print(Strapy.ITALIC+ "Lorem ipsum dolor sit amet" + Strapy.END)
```

You can also combine styles and colors

```python
print(Strapy.RED + Strapy.ITALIC + Strapy.BOLD + "Lorem ipsum dolor sit amet" + Strapy.END)
```
or

```python
style = Strapy.RED + Strapy.ITALIC + Strapy.BOLD
print(style + " Lorem ipsum dolor sit amet" + Strapy.END)
```
Output:
[![exemple.png](https://i.postimg.cc/dVhJCYbF/exemple.png)](https://postimg.cc/5XMccZ9K)

And what is the use of those labels?\
I have been using these labels in projects as a minimal output schema.\
If some error occured in your program or something else bad happened you don't need to print the whole line in red. With Bootstrapy, you can simply do this

```python
print(Strapy.BAD+ "Lorem ipsum dolor sit amet" + Strapy.END)
```

#### List of all colors

```python
   #COLORS
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    GREY = '\033[37m'    
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    LRED = '\033[91m'
    LGREEN = '\033[92m'
    LBLUE = '\033[94m'
    LPURPLE = '\033[95m'
    LCYAN = '\033[96m'
```

#### List of all bg

```python
bold, bg, under, strike, italic, 
#BACKGROUNDS
    BGBLACK = '\033[40m' 
    BGRED = '\033[41m'
    BGGREEN = '\033[42m'
    BGORANGE = '\033[43m'
    BGBLUE = '\033[44m'
    BGPURPLE = '\033[45m'
    BGCYAN = '\033[46m'
    BGGRAY = '\033[47m'
```

#### List of all styles

```python
info, que, run, bad, good
    BOLD = '\033[1m' 
    LIGHT = '\033[2m' 
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'  
    PISCA = '\033[5m' 
    INVERTED = '\033[7m' 
    STRIKE = '\033[9m' 
```
#### List of all labels
```python
    #LABLES
    INFO = '\033[33m' + '[!]' 
    QUE = '\033[34m' + '[?]'
    BAD = '\033[31m' + '[-]'
    GOOD = '\033[32m' + '[+]'
    RUN = '\033[97m' + '[~]'

```
**Note:** Windows versions below windows 10 do not support ANSI escape sequences so the colors will not be printed in command prompt.


### Contribution
So if you can start a pull request for windows support that would be great.
Additional colors and labels will be appreciated too.
