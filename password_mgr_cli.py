
class Menu():


    def __init__(self):
        print('Welcome to Password Manager')


    def startMenu(self):
        print('-'*30)
        print(('-'*13) + 'Menu'+ ('-' *13))
        print('1. Create new password')
        print('2. Find all sites and apps connected to an email')
        print('3. Find a password for a site or app')
        print('Q. Exit')
        print('-'*30)
        

menuObj = Menu()