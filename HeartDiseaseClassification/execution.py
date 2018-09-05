# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:20:49 2018

@author: girijamohanty
"""
import sys
from classification import Learning
def main():
    path=sys.argv[1]
    Learning(path)

if __name__ == "__main__":
    main()