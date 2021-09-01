class ManageStack():

    def __init__(self):
        self.s = []

    def add(self, i):
        self.s.append(int(i))
        print(f'Add = {i}')

    def pop(self):
        if len(self.s) == 0:
            print("-1")
        else:
            print(f'Pop = {self.s[-1]}')
            self.s.pop()

    def delete(self, i):
        self.deL = []
        if len(self.s) == 0:
            print("-1")
        else:
            while int(i) in self.s:
                self.s.remove(int(i))
                print(f'Delete = {i}')

    def lessThan(self, i):
        self.deL = []
        if len(self.s) == 0:
            print("-1")
        else:
            for j in range(0, len(self.s)):
                if self.s[j] < int(i):
                    self.deL.append(self.s[j])
            self.deL.reverse()
            for k in range(0, len(self.deL)):
                self.s.remove(self.deL[k])
                print(f'Delete = {self.deL[k]} Because {self.deL[k]} is less than {i}')

    def moreThan(self, i):
        self.deL = []
        if len(self.s) == 0:
            print("-1")
        else:
            for j in range(0, len(self.s)):
                if self.s[j] > int(i):
                    self.deL.append(self.s[j])
                    print(f'Delete = {self.s[j]} Because {self.s[j]} is more than {i}')
            for k in range(0, len(self.deL)):
                self.s.remove(self.deL[k])


    def __str__(self):
        return f'Value in Stack = {self.s}'



ip = [e for e in input("Enter Input : ").split(",")]

s = ManageStack()

for i in range(0,len(ip)):
    if ip[i] == 'P':
        s.pop()
    else:
        command, value = ip[i].split()
        if command == 'A':
            s.add(value)
        elif command == 'D':
            s.delete(value)
        elif command == 'LD':
            s.lessThen(value)
        else: s.moreThen(value)

print(s)
