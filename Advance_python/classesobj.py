class Human:
    def __init__(self, name,occupation):
        self.name=name,
        self.occupation=occupation

    def do_work(self):
        if self.occupation=="Tennis Player":
            print(self.name,'Plays Tennis')
        elif self.occupation=="actor":
            print(self.name,' Shoots a Drama')

    def speaks(self):
        print(self.name,"Says How Are You?")


Tom=Human("Tom Cruise","actor")
Tom.do_work()
Tom.speaks()
#
Maria=Human("Maria","Tennis Player")
Maria.do_work()
Maria.speaks()
#

class System:
    def __init__(self, name,brand,model):
        self.name=name
        self.brand=brand
        self.model=model
    def drive(self):
        print(f'{self.name} is driving {self.brand} {self.model} ');

my_car=System("AQ_Khan","Toyota","CIVIC")
my_car.drive()
your_car=System("Sami","Honda","Corola")
your_car.drive()



class User:
    def __init__(self, username,email,password):
        self.username=username
        self.email=email
        self.password=password

    def display_user(self):
        print(f"Username: {self.username} \n Password : {self.email}")

# Getting NEW users
User1=User(input("Enter Your Username: "),input("Enter Your Email: "),input("Enter Your Passcode: "))
User1.display_user()
User2=User(input("Enter Your Username: "),input("Enter Your Email: "),input("Enter Your Passcode: "))
User2.display_user()

