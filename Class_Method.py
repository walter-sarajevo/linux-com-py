class Checkout_Cover(object):

    def __init__(self,command):
        self.command = command
        self.checkoutcode = 0

    def checkout(self, command):

        for byte in command:
            self.checkoutcode += ord(byte) - 32

        self.checkoutcode = self.checkoutcode % 95 + 32

        return [self.checkoutcode, chr(self.checkoutcode)]

a = Checkout_Cover("others")

b = "yours"

# print(a.checkout(b))

print(a.checkout(a.command))
print(a.checkoutcode)
print(a.checkout("yours"))
print(a.checkoutcode)
