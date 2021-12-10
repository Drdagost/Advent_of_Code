import statistics

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
        if value == '(':
            return(1)
        elif value == '[':
            return(2)
        elif value == '{':
            return(3)
        elif value == '<':
            return(4)
        else:
            return(0)   

if __name__ == "__main__":
    naverror = NavErrors()
    rev_list = []
    total_points = []
    
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
                    #print(f'{line} - Expected {naverror.is_expected()}, but found {c} instead.')
                    naverror.current_list = []
                    break

            if len(naverror.current_list) > 0:
                total = 0
                rev_list = naverror.current_list
                rev_list.reverse()
                for c in rev_list:
                    total *= 5
                    total += naverror.calc_points(c)
                total_points.append(total)
                print(f'{line} - Complete by adding {len(naverror.current_list)} characters, total points: {total}')

    print(f'The middle score {statistics.median(total_points)}')