__author__ = 'sunghyo.jung'

class MyBook:
    __metaclass__ = ABCMeta
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price = price

    def display(self):
        print 'Title: ' + title
        print 'Author: ' + author
        print 'Price: %d' % (price)