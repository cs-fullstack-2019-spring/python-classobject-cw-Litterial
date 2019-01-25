def main():
    def quest1():
    #Create a class Dog. Make sure it has the attributes name, breed, color, gender.
    # Create a function that will print all attributes of the class.
    # Create an object of Dog in your problem1 function and print all of it's attributes.
        class Dog():
            def __init__(self,name,breed, color, gender):  #constructor
                self.name = name
                self.breed = breed
                self.color = color
                self.gender = gender
            def printAll(self):
                return(f"Name: {self.name}\nBreed: {self.breed} \nColor: {self.color} \nGender: {self.gender}")
        mydog= Dog("Spike","Pitbull","White","Cis-male")
        print(mydog.printAll())

    def quest2():
    #Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
        def function():
            press_equal=""
            while(press_equal!="="):      #loops until '=' is printed
                press_equal=input("Please input a string. Enter '=' to escape. ")
                if(press_equal=='q'):  #optional code for fun
                    print("LOL WRONG ASSIGNMENT")
                elif(press_equal=="="):
                    print("Escaped.")
        function()
    def quest3():
        class BMI():
            def __init__(self,name,weight,height):
                self.name = name
                self.weight=weight
                self.height=height
            def calculate_BMI(self):   #calculates BMI
                calculated_BMI=(self.weight/(self.height^2))*702
                return (f"{self.name}'s Caluclated BMI {calculated_BMI}")
            def changeWeight(self,newweight):    #changes weight
                self.weight=newweight
            def changeHeight(self,newheight):    #changes height
                self.height=newheight
            def printall(self):                  #prints all
                return(f"Name: {self.name}\nWeight: {self.weight} \nHeight: {self.height}")

        #In your main file create three Person objects. Change the weight and height of each one.
        #Objects
        Judy=BMI("Judy",120,62)
        Joseph=BMI("Joseph", 210, 80)
        Carl=BMI("Carl", 95, 59)

        #Prints all
        print(Judy.printall())
        print(Joseph.printall())
        print(Carl.printall())

        #Changes to Weight and Height then prints
        Joseph.changeWeight(265)
        Carl.changeHeight(60)
        print(Joseph.printall())
        print(Carl.printall())

        #Calculates BMI and prints
        print(Judy.calculate_BMI())
        print(Joseph.calculate_BMI())
        print(Carl.calculate_BMI())

    def quest4():
    #Create a class Product that represents a product sold online. A product has a name, price, and quantity.
    #The class should have changeProduct:
        class Product():
            def __init__(self,name,price="None",quanity="None"):
                self.name=name
                self.price=price
                self.quanity=quanity
            def changeProduct(self,newname,newprice,newquanity):#a) If changeProduct has one parameter, it can change the name of the product.
                if self.price=="None" and self.quanity =="None":
                    self.name = newname
                elif self.quanity == "None":#b) If changeProduct has two parameters it can change the name and price of the product.
                    self.name = newname
                    self.price = newprice
                else:#c) If changeProduct has three parameters it can change the name, price, and quantity of the product.
                    self.name = newname
                    self.price = newprice
                    self.quanity = newquanity

            #Create an object of Product in your problem4 function and print all of it's attributes.
            def printAll(self):
                return(f"Name: {self.name}, Price: ${self.price}, Quanity: {self.quanity}")


        #Examples
        full=Product("Pencil", .99, 24)
        notquitefull=Product("Water Bottle",3)
        almostempty=Product("Eraser")
        #Prints will print none if there is no parameter
        print(full.printAll())
        print(notquitefull.printAll())
        print(almostempty.printAll())
        #changes
        full.changeProduct("Pen",3,5)
        notquitefull.changeProduct("Soda", 100, 4)
        almostempty.changeProduct("Paper",8,3)
        #Results
        print(full.printAll())
        print(notquitefull.printAll())
        print(almostempty.printAll())

    #quest1()
    #quest2()
    quest3()
    # quest4()

if __name__ == '__main__':
    main()
