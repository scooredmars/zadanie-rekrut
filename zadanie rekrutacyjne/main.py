import itertools
'''
W celu zmiany pliku z danymi wejsciowymi  należy zmienć nazwę pliku w linijce 19 lub wpisać dane do pliku
'''

class zoo:
    def __init__(self):
        self.number_of_elephants = 0
        self.weight_of_elephants = []
        self.starting_position = []
        self.final_position =  []
        self.simple_weight_sum = 0
        self.more_arg_weight_sum = 0
        self.met1 = 0
        self.met2 = 0

    def open_file(self):
        List = []
        List = open("dane-testowe/" + "slo3.in", 'r').readlines()
        amount_of_elephants = List[0]
        weight_of_elephants = List[1]
        starting_position = List[2]
        final_position = List[3]

        weight_of_elephants = weight_of_elephants.split()
        starting_position = starting_position.split()
        final_position = final_position.split()

        self.number_of_elephants = int(amount_of_elephants)

        for a in weight_of_elephants:
            self.weight_of_elephants.append(int(a))

        for a in starting_position:
            self.starting_position.append(int(a))

        for a in final_position:
            self.final_position.append(int(a))

    def number_difference(self):
        loop = 0
        C1 = 2
        vertical_database = []
        temp_data = []
        simple_swap = []
        swap_with_more_arg = []
        same_num = []
        # grupowanie liczb poczatkowy-koncowy cykl
        while True:
            if loop == self.number_of_elephants:
                break
            start = self.starting_position[loop]
            end = self.final_position[loop]
            vertical_database.append({'kol1': start, 'kol2': end})
            loop += 1

        # rozdziela baze na cykle 2 liczbowe i wieloliczbowe
        for a in vertical_database:
            for b in vertical_database:
                if (a['kol1'] == b['kol2']) and (b['kol1'] == a['kol2']):
                    if a['kol1'] != a['kol2']:
                        temp_data.append([a['kol1'], a['kol2']])
                    else:
                        same_num.append(a['kol1'])
                elif (a['kol1'] != b['kol2']) and (b['kol1'] == a['kol2']):
                    swap_with_more_arg.append(a)

        # usuwa duplikaty
        for a in temp_data:
            for b in temp_data:
                if a == b[::-1]:
                    if a[0] != a[1]:
                        temp_data.remove(b[::-1])
                        simple_swap.append(
                            {'kol1': a[0], 'kol2': a[1]})

        # suma wag i min waga sloni z cykli 2 liczbowych
        simple_swap_data = []
        if simple_swap:
            for a in simple_swap:
                sumaC1 = 0
                minC1 = 0
                sumaC1 += self.weight_of_elephants[(a['kol1'] - 1)]
                sumaC1 += self.weight_of_elephants[(a['kol2'] - 1)]
                if self.weight_of_elephants[(a['kol1'] - 1)] >= self.weight_of_elephants[(a['kol2'] - 1)]:
                    minC1 = self.weight_of_elephants[(a['kol2'] - 1)]
                else:
                    minC1 = self.weight_of_elephants[(a['kol1'] - 1)]
                simple_swap_data.append({'sumaC': sumaC1, 'minC': minC1})

        temp_list = []
        cycle_list = []
        temp_numb = []
        temp_numb2 = []
        start_arg = swap_with_more_arg[0]['kol1']
        end_arg = swap_with_more_arg[0]['kol1']
        stop = False
        new_num = False
        # wykrycie cykli wieloliczbowych i pogrupowanie ich
        while stop == False:
            for a in range(len(swap_with_more_arg)):
                if cycle_list and new_num:
                    for b in cycle_list:
                        if not swap_with_more_arg[a]['kol1'] in b:
                            start_arg = swap_with_more_arg[a]['kol1']
                            end_arg = swap_with_more_arg[a]['kol1']
                            new_num = False
                            if not swap_with_more_arg[a]['kol1'] in temp_numb:
                                if a == (len(swap_with_more_arg) - 1):
                                    temp_numb.append(swap_with_more_arg[a]['kol1'])
                                    stop = True
                                    break
                if swap_with_more_arg[a]['kol2'] == start_arg:
                    if not swap_with_more_arg[a]['kol1'] in temp_numb2:
                        temp_list.append(swap_with_more_arg[a]['kol1'])
                        temp_numb2.append(swap_with_more_arg[a]['kol1'])
                    start_arg = swap_with_more_arg[a]['kol1']
                    if start_arg == end_arg:
                        if temp_list:
                            cycle_list.append(temp_list)
                        temp_list = []
                        new_num = True
            if len(cycle_list) > 0:
                v = 0
                j = 0
                for k in range(len(cycle_list)):
                    v += len(cycle_list[k])
                for h in range(len(simple_swap)):
                    j += len(simple_swap[h])
                if (v + j + len(same_num)) == self.number_of_elephants:
                    stop = True

        # usuniecie duplikatow
        for a in cycle_list:
            a.sort()
        cycle_list.sort()
        cycle_list = list(cycle_list for cycle_list,
                          _ in itertools.groupby(cycle_list))

        # suma wag, dlugosc cyklu i min waga sloni z cykli wieloliczbowych
        if cycle_list:
            self.max = max(self.weight_of_elephants)
            multi_element_cycle = []
            for a in range(len(cycle_list)):
                sumaC2 = 0
                minC2 = 0
                for b in range(len(cycle_list[a])):
                    sumaC2 += self.weight_of_elephants[(cycle_list[a][b] - 1)]
                    if minC2 == 0:
                        minC2 = self.max
                    if self.weight_of_elephants[(cycle_list[a][b] - 1)] <= minC2:
                        minC2 = self.weight_of_elephants[(cycle_list[a][b] - 1)]
                multi_element_cycle.append({'sumaC': sumaC2, 'C': len(cycle_list[a]), 'minC': minC2})

        self.method1(simple_swap_data, C1, True)
        self.method1(multi_element_cycle, 0, False)
        self.method2(simple_swap_data, C1, True)
        self.method2(multi_element_cycle, 0, False)

    def method1(self, list_of_cycles, C, simple):
        if simple:
            object_sum = 0
            for a in list_of_cycles:
                object_sum += a['sumaC'] + (C - 2) * a['minC']
            self.simple_weight_sum = object_sum
        else:
            object_sum = 0
            for a in list_of_cycles:
                object_sum += a['sumaC'] + (a['C'] - 2) * a['minC']
            self.more_arg_weight_sum = object_sum
            self.met1 = self.simple_weight_sum + self.more_arg_weight_sum
            return self.met1

    def method2(self, list_of_cycles, C, simple):
        self.min = min(self.weight_of_elephants)
        if simple:
            simple_sum = 0
            for a in list_of_cycles:
                simple_sum += a['sumaC'] + a['minC'] + (C + 1) * self.min
            self.simple_weight_sum = simple_sum
        else:
            object_sum = 0
            for a in list_of_cycles:
                object_sum += a['sumaC'] + a['minC'] + (a['C'] + 1) * self.min
            self.more_arg_weight_sum = object_sum
            self.met2 = self.simple_weight_sum + self.more_arg_weight_sum
            return self.met2

    def profitability_of_the_method(self):
        if self.met1 <= self.met2:
            print(self.met1)
        elif self.met1 >= self.met2:
            print(self.met2)

data = zoo()
data.open_file()
data.number_difference()
data.profitability_of_the_method()