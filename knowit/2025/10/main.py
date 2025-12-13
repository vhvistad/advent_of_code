class Machine:
    def __init__(self, name, temp, water, co2):
        self.name = name
        self.temp = temp
        self.water = water
        self.co2 = co2
        self.total = 0

    def will_produce(self):
        if not 95 <= self.temp <= 105:
            return False
        
        if not 400 <= self.water <= 1500:
            return False
        
        if not 300 <= self.co2 <= 500:
            return False
        
        return True
    
    def produce(self):
        amount = self.water - 100 + (self.co2 / 10)

        if self.temp >= 100:
            amount -= int(amount/40)
        
        self.total += int(amount)

        return int(amount)
    
    def get_total(self):
        return self.total
    
    def reset(self, temp, water, co2):
        self.temp = temp
        self.water = water
        self.co2 = co2


if __name__ == "__main__":
    filename = 'julebrusmaskiner'
    test = 'test'

    top_producer = [None, 0]
    amount = 0
    machines = {}

    with open(f'/home/vegard/repos/advent_of_code/knowit/2025/10/{filename}.txt', 'r') as f:
        for line in f.readlines():
            name, temp, water, co2 = line.strip().split(',')
            name = name[7:]
            temp = int(temp[12:-1])
            water = int(water[6:-1])
            co2 = int(co2[10:-1])

            if name not in machines.keys():
                machines[name] = Machine(name, temp, water, co2)
            else:
                machines[name].reset(temp, water, co2)

            machine = machines[name]

            if machine.will_produce():
                produced = machine.produce()
                amount += produced

                if machine.total > top_producer[1]:
                    top_producer = [machine.name, machine.total]
            
            machines[name] = machine


    print(f'Total amount: {amount}\nTop producer: {top_producer[0]} ({top_producer[1]})')

    print(f'Answer: {amount} {top_producer[0]}')