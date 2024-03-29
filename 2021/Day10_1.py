class NavErrors:
    def __init__(self):
        self.always_valid = ['(', '[', '{', '<']
        self.current_list = []

        
    def add_value(self, value: str) -> None:
        self.current_list.append(value)


    def is_expected(self) -> str:
        if self.current_list[-1] == '(':
            return(')')
        elif self.current_list[-1] == '[':
            return(']')
        elif self.current_list[-1] == '{':
            return('}')
        elif self.current_list[-1] == '<':
            return('>')
        else:
            return('')


    def calc_points(self, value: str) -> int:
        if value == ')':
            return(3)
        elif value == ']':
            return(57)
        elif value == '}':
            return(1197)
        elif value == '>':
            return(25137)
        else:
            return(0)   

if __name__ == "__main__":
    naverror = NavErrors()
    illegal_cha = []
    total = 0
    
    # Read points.
    with open('2021\Day10_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        for line in data:
            naverror.current_list = []
            for c in line:
                if c in naverror.always_valid:
                    naverror.add_value(c)
                elif naverror.is_expected() == c:
                    naverror.current_list.pop()
                else:
                    print(f'{line} - Expected {naverror.is_expected()}, but found {c} instead.')
                    illegal_cha.append(c)
                    break
    
    for c in illegal_cha:
        total += naverror.calc_points(c)
    
    print(f'Total syntax error score for this file is: {total}')                
            