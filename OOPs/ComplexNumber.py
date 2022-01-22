
class ComplexNumber:
    def __init__(self, real, imaginary) -> None:
        self.real = real
        self.imaginary = imaginary

    def printComplex(self):
        print(f"{self.real} + {self.imaginary}i" )    

    def Add(self,Obj2):
        real = self.real + Obj2.real
        imaginary = self.imaginary + Obj2.imaginary
        result = ComplexNumber(real, imaginary) 
        return result

ComplexNumber1 = ComplexNumber(2,3)
ComplexNumber1.printComplex()
ComplexNumber2 = ComplexNumber(-3,5)
ComplexNumber2.printComplex()
Addition_result = ComplexNumber1.Add(ComplexNumber2)
Addition_result.printComplex()

    
