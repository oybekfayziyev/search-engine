import settings
from menu import *

if __name__ == "__main__":

    inp = None
    print(menu())
   
    while inp is None:        
        inp = getInput()
    
    get_option_by_input(inp)


