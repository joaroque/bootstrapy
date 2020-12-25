from .boostrapy import Strapy

__all__ = ['BLACK', 'RED', 'GREN', 'ORANGE', 'BLUE', 'PURPLE',
           'CYAN', 'GREY', 'YELLOW', 'LRED', 'LGREEN', 'LBLUE',
           'LPURPLE', 'LCYAN', 'BGBLACK', 'BGRED', 'BGGREEN',
           'GBORANGE', 'BGBLUE', 'GBPURPLE', 'BGCYAN', 'BGGRAY',
           'BOLD', 'LIGHT', 'ITALIC', 'UNDERLINE', 'PISCA', 'INVERTED',
           'STRIKE', 'INFO', 'QUE', 'BAD', 'GOOD', 'RUN']

__version__ = '0.0.1'

if __name__ == '__main__':
    print("All Commands: ", __all__)
    print("Current version: ", __version__)