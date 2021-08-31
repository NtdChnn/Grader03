class Stack():

    def __init__(self):    # ใช้สำหรับสร้าง list ว่าง
        self.s = []

    def push(self,i):      # เก็บข้อมูลลง stack
        self.s.append(str(i))

    def pop(self):         # นำข้อมูลออกจาก stack
        self.s.pop()

    def isEmpty(self):     # ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        if len(self.s) != 0:
            return False
        else: return True

    def size(self):        # ตรวจสอบจำนวนข้อมูลใจ stack
        return len(self.s)

    def items(self):
        return self.s


print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:
    s.push(e)

print(s.size(), "Data in stack : ", s.items())

while not s.isEmpty():
    s.pop()

print(s.size(),"Data in stack : ", s.items())
