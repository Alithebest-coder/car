#Write a program to create two classes for two different 
# countries that consist of three methods to
# display the following information of respective country capital, 
# language and type of country. Then, use Polymorphism to
# create a common interface for both classes.




class BMW:
    def max_speed(self):
        print("the maxspeed of a BMW is 200")
    def fuel_type(self):
        print("the fule is 95")
class ferrari:
    def max_speed(self):
        print("the maxspeed of a ferrari is")
    def  fuel_type(self):
        print(" the fule is 98")
        
Tobj=BMW()
Jobj=ferrari()
for c in (Tobj,Jobj):
    c.max_speed()
    c.fuel_type()
    