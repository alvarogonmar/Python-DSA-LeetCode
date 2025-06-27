class Cookie:  # Class definition for Cookie
    def __init__(self, color): # Constructor to initialize the color of the cookie, we use 'self' to refer to the instance
        self.color = color # Instance variable to store the color of the cookie

    def get_color(self): # Method to retrieve the color of the cookie
        return self.color # Returns the color of the cookie

    def set_color(self, color): # Method to set a new color for the cookie
        self.color = color


cookie_one = Cookie('green') # Creating an instance of Cookie with color 'green'
cookie_two = Cookie('blue') # Creating another instance of Cookie with color 'blue'

print('Cookie one is', cookie_one.get_color()) # Using the get_color method to print the color of cookie_one
print('Cookie two is', cookie_two.get_color()) # Using the get_color method to print the color of cookie_two

cookie_one.set_color('yellow') # Changing the color of cookie_one to 'yellow' using the set_color method

print('\nCookie one is now', cookie_one.get_color()) # Printing the new color of cookie_one after changing it
print('Cookie two is still', cookie_two.get_color()) # Printing the color of cookie_two to show it remains unchanged
