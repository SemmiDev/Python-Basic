class Segiempat:
    p = 0
    l = 0
    def hitungLuas(self):
        return self.p * self.l

if __name__ == '__main__':
    s = Segiempat()
    s.p = int(input("Panjang : "))
    s.l = int(input("Lebar : "))
    print(s.hitungLuas())
