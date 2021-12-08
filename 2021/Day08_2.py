class CalcDigits:
    def __init__(self) -> None:
        self.digit_list = ['', '', '', '', '', '', '', '', '', '']
        
        self.top = ''
        self.middle = ''
        self.bottom = ''
        self.tr = ''
        self.br = ''
        self.tl = ''
        self.bl = ''

    def remove_duplicates(self, in_string: str) -> str:
        result = ''
        for c in in_string:
            if in_string.count(c) == 1:
                result += c
        return(result)
    
    def get_parts(self) -> None:
        self.top = self.remove_duplicates(self.digit_list[1] + self.digit_list[7])
        self.tr = self.remove_duplicates(self.digit_list[6] + self.digit_list[8])
        self.br = self.remove_duplicates(self.tr + self.digit_list[1])
        self.bl = self.remove_duplicates(self.digit_list[8] + self.digit_list[9])
        self.middle = self.remove_duplicates(self.digit_list[8] + self.digit_list[0])
        self.tl = self.remove_duplicates(self.digit_list[4] + self.digit_list[1] + self.middle)
        self.bottom = self.remove_duplicates(self.digit_list[8] + self.digit_list[4] + self.top + self.bl)

    def get_known_digits(self, known_digits: list) -> None:
        for known_digit in known_digits:
            length = len(known_digit)
            if length == 2:
                self.digit_list[1] = known_digit
            if length == 4:
                self.digit_list[4] = known_digit
            if length == 3:
                self.digit_list[7] = known_digit
            if length == 7:
                self.digit_list[8] = known_digit

    def get_six(self, known_digits: list) -> None:
        for known_digit in known_digits:
            length = len(known_digit)
            if length == 6:
                for c in self.digit_list[1]:
                    if c not in known_digit:
                        self.digit_list[6] = known_digit
        self.get_parts()

    def get_nine_zero(self, known_digits: list) -> None:
        for known_digit in known_digits:
            length = len(known_digit)
            if length == 6 and known_digit != self.digit_list[6]:
                # Zero
                for c in self.digit_list[4]:
                    if c not in known_digit:
                        self.digit_list[0] = known_digit
                        break
                # Nine
                else:
                    self.digit_list[9] = known_digit
        self.get_parts()

    def get_two_three_five(self, known_digits: list) -> None:
        for known_digit in known_digits:
            length = len(known_digit)
            if length == 5:
                if self.remove_duplicates(known_digit + self.top + self.tl + self.middle + self.br + self.bottom) == '':
                    self.digit_list[5] = known_digit
                if self.remove_duplicates(known_digit + self.top + self.tr + self.middle + self.bl + self.bottom) == '':
                    self.digit_list[2] = known_digit
                if self.remove_duplicates(known_digit + self.top + self.tr + self.middle + self.br + self.bottom) == '':
                    self.digit_list[3] = known_digit

    def get_unknown_digits(self, known_digits: list) -> None:
        # need to get six to find nine and zero
        self.get_six(known_digits)
        # now we can get nine and zero
        self.get_nine_zero(known_digits)
        # now we can set two, three and five
        self.get_two_three_five(known_digits)  

    def get_four_digits(self, four_digits: list) -> int:
        result = ''
        for digit in four_digits:
            for x in enumerate(self.digit_list):
                if self.remove_duplicates(x[1] + digit) == '':
                    result += str(x[0])
        return int(result)

if __name__ == "__main__":
    digit = CalcDigits()
    total = 0
    # Read points.
    with open('2021\Day08_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        for line in data:
            segments = []
            display = []
            # Clean the input
            line = line.split(' | ')
            segments = line[0].split(' ')
            display = line[1].split(' ')
            digit.get_known_digits(segments)
            digit.get_unknown_digits(segments)
            #print(digit.get_four_digits(display))
            total += digit.get_four_digits(display)
    print(f'Sum of all 4 digit displays: {total}')

