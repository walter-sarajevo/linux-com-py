# coding=utf-8

class NoCheck(object):

    def __init__(self):
        self.description = "Use NO checkout method."
        self.cbyte = ''
        self.ccode = 0
        self.method = "No, here's nothing."

    def checkout(self):
        return self.cbyte
    

class Cover(object):

    def __init__(self):
        self.description = "Checkout method of upcover-module and downcover-module."
        self.cbyte = ''
        self.ccode = 0
        self.method = "checkcode = [SUM( Value - 32) mod (95)] + 32"

    def checkout(self, command):

        for byte in command:
            self.ccode += ord(byte) - 32

        self.ccode = self.ccode % 95 + 32
        self.cbyte = chr(self.ccode)

        return self.cbyte

