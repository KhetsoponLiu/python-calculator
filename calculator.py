class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b    #แก้จุดที่ 1 สลับ a,b

    def multiply(self, a, b):
        result = 0
        is_negative = b < 0
        b = abs(b)
        for i in range(b):  #แก้ไขจุดที่ 2 เปลี่ยนจาก b + 1 เป็น b
            result = self.add(result, a)
        if is_negative:
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Error")
        result = 0
        while a >= b:   #แก้ไขจุดที่ 3 เปลี่ยนจาก > เป็น >=
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Error")
        while a >= b:   #แก้ไขจุดที่ 4 เปลี่ยนจาก <= เป็น >=
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))