import pytest
from .main import *
from utils.util import *
from utils.constant import *

def test_creating_an_account_successfully():
    computed = processFile("infile.txt", "", False)
    expected = [ 
        {
            'accounts': 
            {
                'activeCard': False, 
                'availableLimit': 750
            }, 
            'violations': []
        }
    ]
    assert computed == expected