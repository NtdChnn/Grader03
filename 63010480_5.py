class Stack():

    def __init__(self):    # ใช้สำหรับสร้าง list ว่าง
        self.s = []

    def add(self,i):      # เก็บข้อมูลลง stack
        self.s.append(int(i))

    def toxic(self):
        for i in range(0,len(self.s)):
            if self.s[i] % 2 == 1:
                self.s[i] += 2
            elif self.s[i] % 2 == 0:
                self.s[i] -= 1

    def look(self):
        num = []
        if len(self.s) == 0:
            print(0)
        elif len(self.s) == 1:
            print(1)
        else :
            for j in range(0,len(self.s)):
                if len(num) != 0:
                    while self.s[j] > num[-1]:
                        num.pop()
                        if len(num) == 0:
                            num.append(self.s[j])
                            break
                    if self.s[j] < num[-1]:
                        num.append(self.s[j])
                else:
                    num.append(self.s[j])
            print(len(num))


ip = [e for e in input("Enter Input : ").split(",")]

s = Stack()

for i in range(0,len(ip)):
    if ip[i] == 'B':
        s.look()
    elif ip[i] == 'S':
        s.toxic()
    else:
        command, value = ip[i].split()
        if command == 'A':
            s.add(value)
