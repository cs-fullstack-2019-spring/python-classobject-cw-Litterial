def main():
    def quest3():
        array=[]
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

        #define each object and adds them to an array.
        Judy=BMI("Judy",120,62)
        array.append(Judy)
        Joseph=BMI("Joseph", 210, 80)
        array.append(Joseph)
        Carl=BMI("Carl", 95, 59)
        array.append(Carl)

        for x in range(len(array)):
            print(array[x].calculate_BMI())
    quest3()


if __name__ == '__main__':
    main()