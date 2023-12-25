from operator import itemgetter

class Microprocessor:
    def __init__(self, microprocessor_id, brand, price, computer_id):
        self.microprocessor_id = microprocessor_id
        self.brand = brand
        self.price = price
        self.computer_id = computer_id

class Computer:
    def __init__(self, computer_id, name):
        self.computer_id = computer_id
        self.name = name

class MicroprocessorComputer:
    def __init__(self, computer_id, microprocessor_id):
        self.computer_id = computer_id
        self.microprocessor_id = microprocessor_id

print(Computer(1, 'PC'))
# <__main__.Computer object at 0x00000180C81F83A0>

computers = [
    Computer(1, 'Desktop PC'),
    Computer(2, 'Laptop'),
    Computer(3, 'Server'),
    # Add more computers if needed
]

microprocessors = [
    Microprocessor(1, 'Intel', 25000, 1),
    Microprocessor(2, 'AMD', 35000, 1),
    Microprocessor(3, 'ARM', 25000, 2),
    Microprocessor(4, 'Apple', 45000, 3),
    # Add more microprocessors if needed
]

microprocessors_computers = [
    MicroprocessorComputer(1, 1),
    MicroprocessorComputer(1, 2),
    MicroprocessorComputer(2, 3),
    MicroprocessorComputer(3, 4),
    MicroprocessorComputer(3, 5),
    MicroprocessorComputer(3, 6),
    # Add more relationships if needed
]

def main():
    one_to_many = [(m.brand, m.price, c.name)
                   for c in computers
                   for m in microprocessors
                   if m.computer_id == c.computer_id]

    many_to_many_temp = [(c.name, mc.computer_id, mc.microprocessor_id)
                         for c in computers
                         for mc in microprocessors_computers
                         if c.computer_id == mc.computer_id]

    many_to_many = [(m.brand, m.price, computer_name)
                    for computer_name, computer_id, microprocessor_id in many_to_many_temp
                    for m in microprocessors if m.microprocessor_id == microprocessor_id]

    print('Task E1')
    print(list(filter(lambda i: i[2].find('Server') != -1, one_to_many)))

    print('Task E2')
    res_12_unsorted = []
    for c in computers:
        computer_microprocessors = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(computer_microprocessors) > 0:
            c_prices = [price for _, price, _ in computer_microprocessors]
            c_prices_sum = round(sum(c_prices) / len(computer_microprocessors), 2)
            res_12_unsorted.append((c.name, c_prices_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('Task E3')
    print(list(filter(lambda i: i[0].find('A') != -1, many_to_many)))

if __name__ == '__main__':
    main()
