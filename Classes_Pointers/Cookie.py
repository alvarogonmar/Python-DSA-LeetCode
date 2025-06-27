class Cookie:  # Class definition for Cookie
    def __init__(self, color): # Constructor to initialize the color of the cookie, we use 'self' to refer to the instance
        self.color = color # Instance variable to store the color of the cookie

    def get_color(self): # Method to retrieve the color of the cookie
        return self.color # Returns the color of the cookie

    def set_color(self, color): # Method to set a new color for the cookie
        self.color = color


cookie_one = Cookie('green') # Creating an instance of Cookie with color 'green'
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
