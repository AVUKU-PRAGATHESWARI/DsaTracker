from random import shuffle
import time
class binarytreenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None 
    def __str__(self):
        return("node[%s]"%self.val) 
class binarytree:
    def 