

#Parent Class
class Instruments:
    Brand = 'Unknown'
    Color = 'Unknown'
    Key_Count = None
    String_Count = None
    Key_Weight = None 
    Tuning = 'Standard'

    #Method
    def Information(self):
        msg = "\nBrand: {}\nColor: {}\nKey Count: {}\nString Count: {}\nKey Weight: {}\nTuning: {}".format(self.Brand, self.Color,self.Key_Count, self. String_Count, self.Key_Weight, self.Tuning)
        return msg

#child class
class Piano(Instruments):
    Brand = 'Yamaha'
    Color = 'Silver'
    Key_Count = 76
    Key_Weight = '30 grams'
# Polymorphism (left out string count and Tuning)
    def Information(self):
        msg = "\nBrand: {}\nColor: {}\nKey Count: {} \nKey Weight: {}".format(self.Brand, self.Color,self.Key_Count, self.Key_Weight)
        return msg
#child class
class Guitar(Instruments):
    Brand = 'Fender'
    Color = 'Black and White'
    String_Count = 6
    Tuning = 'EADGBE'
# Polymorphism (left out key count and key weight)
    def Information(self):
        msg = "\nBrand: {}\nColor: {}\nString Count: {}\nTuning: {}".format(self.Brand, self.Color, self. String_Count, self.Tuning)
        return msg


    

if __name__ == "__main__":
    Piano = Piano()
    print(Piano.Information())

    Guitar = Guitar()
    print(Guitar.Information())

