class NavErrors:
    def __init__(self):
        self.always_valid = ['(', '[', '{', '<']
        self.current_list = []

        
    def add_value(self, value: str) -> None:
        self.current_list.append(value)
    

if __name__ == "__main__":
    naverror = NavErrors()
    
    # Read points.
    with open('2021\Day10_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        for line in data:
            for c in line:
                if c in naverror.always_valid:
                    naverror.add_value(c)
                elif naverror.is_expected():
                    naverror.add_value(c)
                else:
                    # Unexpected value
                    pass
            