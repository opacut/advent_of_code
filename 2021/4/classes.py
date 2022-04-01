class Board:
    def __init__(self, data):
        data = [[int(y) for y in x.split(" ") if y != ''] for x in data]
        print(f"Data: {data}")
        self.data = data
        self.a1 = [int(data[0][0]), False]
        self.a2 = [int(data[0][1]), False]
        self.a3 = [int(data[0][2]), False]
        self.a4 = [int(data[0][3]), False]
        self.a5 = [int(data[0][4]), False]
        self.b1 = [int(data[1][0]), False]
        self.b2 = [int(data[1][1]), False]
        self.b3 = [int(data[1][2]), False]
        self.b4 = [int(data[1][3]), False]
        self.b5 = [int(data[1][4]), False]
        self.c1 = [int(data[2][0]), False]
        self.c2 = [int(data[2][1]), False]
        self.c3 = [int(data[2][2]), False]
        self.c4 = [int(data[2][3]), False]
        self.c5 = [int(data[2][4]), False]
        self.d1 = [int(data[3][0]), False]
        self.d2 = [int(data[3][1]), False]
        self.d3 = [int(data[3][2]), False]
        self.d4 = [int(data[3][3]), False]
        self.d5 = [int(data[3][4]), False]
        self.e1 = [int(data[4][0]), False]
        self.e2 = [int(data[4][1]), False]
        self.e3 = [int(data[4][2]), False]
        self.e4 = [int(data[4][3]), False]
        self.e5 = [int(data[4][4]), False]
        self.closed = False
    
    @property
    def row_1(self):
        return [self.a1,self.a2,self.a3,self.a4,self.a5]
    
    @property
    def row_2(self):
        return [self.b1,self.b2,self.b3,self.b4,self.b5]

    @property
    def row_3(self):
        return [self.c1,self.c2,self.c3,self.c4,self.c5]

    @property
    def row_4(self):
        return [self.d1,self.d2,self.d3,self.d4,self.d5]

    @property
    def row_5(self):
        return [self.e1,self.e2,self.e3,self.e4,self.e5]

    @property
    def column_1(self):
        return [self.a1,self.b1,self.c1,self.d1,self.e1]
    
    @property
    def column_2(self):
        return [self.a2,self.b2,self.c2,self.d2,self.e2]

    @property
    def column_3(self):
        return [self.a3,self.b3,self.c3,self.d3,self.e3]

    @property
    def column_4(self):
        return [self.a4,self.b4,self.c4,self.d4,self.e4]

    @property
    def column_5(self):
        return [self.a5,self.b5,self.c5,self.d5,self.e5]

    @property
    def all_fields(self):
        return [self.a1,self.a2,self.a3,self.a4,self.a5,self.b1,self.b2,self.b3,self.b4,self.b5,self.c1,self.c2,self.c3,self.c4,self.c5,self.d1,self.d2,self.d3,self.d4,self.d5,self.e1,self.e2,self.e3,self.e4,self.e5]

    def check_completion(self):
        if all([y[1] for y in self.row_1]):
            return True
        if all([y[1] for y in self.row_2]):
            return True
        if all([y[1] for y in self.row_3]):
            return True
        if all([y[1] for y in self.row_4]):
            return True
        if all([y[1] for y in self.row_5]):
            return True
        if all([y[1] for y in self.column_1]):
            return True
        if all([y[1] for y in self.column_2]):
            return True
        if all([y[1] for y in self.column_3]):
            return True
        if all([y[1] for y in self.column_4]):
            return True
        if all([y[1] for y in self.column_5]):
            return True
        return False

    def process_number(self, number):
        for field in self.all_fields:
            if field[0] == number:
                field[1] = True
                #print("Hit! For number"+str(number)+". Whole board: "+str(self.all_fields))
                if self.check_completion():
                    print("WE HAVE A WINNER!!! The score is "+str(sum([field[0] for field in self.all_fields if not field[1]])*number))
                    #return True
                    self.closed = True
                break
