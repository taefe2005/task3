class ThiefFinder:
    def __init__(self):
        self.a3 = "true"  # متن سوال
        self.a1 = "true"
        self.c1 = 'false'
        self.c3 = 'false'
        self.d2 = 'true'  # تاثیری رو جواب ندارند
        self.a2 = "true"
        self.b1 = 'true'  # محتمل ترین فرض حالت اول
        self.b3 = ''
        self.b2 = ''
        self.c2 = ''
        self.d1 = ''
        self.d3 = ''
        self.false_count = 2
        self.true_count = 5

    def find_thief(self):
        while self.false_count < 6:
            if self.a2 == 'true':
                self.b3 = 'false'
                self.false_count += 1
                if self.b3 == 'false':
                    self.d3 = 'false'
                    self.false_count += 1
                    self.b2 = 'true'
                    self.true_count += 1
                    if self.true_count == 6:
                        self.c2 = 'false'
                        self.d1 = 'false'
                        self.false_count += 2
                else:
                    break
            else:
                self.a2 == 'false'
                self.false_count += 1
                break

        if (self.true_count == 6 and self.false_count == 6):
            print('The thief is B')

# ایجاد یک نمونه از کلاس ThiefFinder و فراخوانی متد find_thief
thief_finder = ThiefFinder()
thief_finder.find_thief()