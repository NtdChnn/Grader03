class Stack(){

    def __init__(self):    # ใช้สำหรับสร้าง list ว่าง


    def push(self,i):      # เก็บข้อมูลลง stack

    def pop(self):         # นำข้อมูลออกจาก stack

    def isEmpty(self):     # ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false

    def size(self):        # ตรวจสอบจำนวนข้อมูลใจ stack
}

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)
