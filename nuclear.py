import math
import matplotlib.pyplot as plt


class Nucleus():
    def __init__(self):
        q = 1
        self.nuclei = []
        while q == 1:
            print(self.nuclei)
            vvod = input('Хотите ли вы продолжить ввод?\nВведите Да или Нет: ')
            if vvod == 'Да' or vvod == 'да':
                self.A = int(input('Введите массовое число ядра А: '))
                self.Z = int(input('Введите зарядовое число ядра Z: '))
                self.nuclei.append(self.Z)
                self.nuclei.append(self.A)
            elif vvod == 'Нет' or vvod == 'нет':
                print('Ввод окончен.\n')
                break
            else:
                print('Ошибка ввода.')
        self.programm_main()

    def add_elements(self):
        q = 1
        while q == 1:
            print(self.nuclei)
            vvod = input('Хотите ли вы продолжить ввод?\nВведите Да или Нет: ')
            if vvod == 'Да' or vvod == 'да':
                self.A = int(input('Введите массовое число ядра А: '))
                self.Z = int(input('Введите зарядовое число ядра Z: '))
                self.nuclei.append(self.Z)
                self.nuclei.append(self.A)
            elif vvod == 'Нет' or vvod == 'нет':
                print('Ввод окончен.\n')
                break
            else:
                print('Ошибка ввода.')
        self.programm_main()

    def energy_vaizekker(self, value):
        n = 2 * (value - 1)
        self.A = self.nuclei[n + 1]
        self.Z = self.nuclei[n]
        if self.A % 2 != 0:
            self.energy = 15.7 * self.A - 17.8 * (self.A ** (2 / 3)) - 0.71 * (
                        (self.Z ** 2) / (self.A ** (1 / 3))) - 23.7 * ((self.A - 2 * self.Z) ** 2) / self.A
        elif self.A % 2 == 0 and self.Z % 2 == 0:
            self.energy = 15.7 * self.A - 17.8 * (self.A ** (2 / 3)) - 0.71 * (
                        (self.Z ** 2) / (self.A ** (1 / 3))) - 23.7 * ((self.A - 2 * self.Z) ** 2) / self.A + 34 * (
                                      self.A ** (-3 / 4))
        elif self.A % 2 == 0 and self.Z % 2 != 0:
            self.energy = 15.7 * self.A - 17.8 * (self.A ** (2 / 3)) - 0.71 * (
                        (self.Z ** 2) / (self.A ** (1 / 3))) - 23.7 * ((self.A - 2 * self.Z) ** 2) / self.A - 34 * (
                                      self.A ** (-3 / 4))
        self.udel_energy = self.energy / self.A
        print('Удельная энергия ядра :', round(self.udel_energy, 3), ' МэВ/нуклон')

    def energy_vaizekker_plots(self, value1, value2):
        self.A = value1
        self.Z = value2
        if self.A % 2 != 0:
            self.energy = 15.7 * self.A - 17.8 * (self.A ** (2 / 3)) - 0.71 * (
                        (self.Z ** 2) / (self.A ** (1 / 3))) - 23.7 * ((self.A - 2 * self.Z) ** 2) / self.A
        elif self.A % 2 == 0 and self.Z % 2 == 0:
            self.energy = 15.7 * self.A - 17.8 * (self.A ** (2 / 3)) - 0.71 * (
                        (self.Z ** 2) / (self.A ** (1 / 3))) - 23.7 * ((self.A - 2 * self.Z) ** 2) / self.A + 34 * (
                                      self.A ** (-3 / 4))
        elif self.A % 2 == 0 and self.Z % 2 != 0:
            self.energy = 15.7 * self.A - 17.8 * (self.A ** (2 / 3)) - 0.71 * (
                        (self.Z ** 2) / (self.A ** (1 / 3))) - 23.7 * ((self.A - 2 * self.Z) ** 2) / self.A - 34 * (
                                      self.A ** (-3 / 4))
        self.udel_energy = self.energy / self.A
        return round(self.udel_energy, 3)

    def mass(self):
        self.izbitok = self.Z * 7.289 + (self.A - self.Z) * 8.071 - self.energy
        self.massa = self.izbitok + self.A * 931.5
        return print('Масса ядра :', round(self.massa, 3), ' МэВ или ', round(self.massa / 931.5, 3), ' а.е.м.')

    def radius(self):
        self.rad = 1.4 * (self.A) ** (1 / 3)
        return print('Радиус ядра :', round(self.rad, 3), ' Фм')

    def radius_plot(self, value1):
        self.r = 1.4 * (value1) ** (1 / 3)
        return round(self.r, 3)

    def ustoychivost_b(self):
        self.Z_ravn = int(self.A / (0.015 * self.A ** (2 / 3) + 2)) + 1
        if self.Z != self.Z_ravn:
            print('Ядро неустойчиво и претерпевает b-распад')
        else:
            print('Ядро устойчиво к b-распаду')

    def proverka_delenia(self):
        if self.A % 4 == 0 and self.Z % 4 == 0:
            print('Ядро делится на два чётно-чётных осколка')
        else:
            print('Ядро не делится на два чётно-чётных осколка')
        self.A = 0
        self.Z = 0

    def atom_info(self, val):
        self.energy_vaizekker(val)
        self.mass()
        self.radius()
        self.ustoychivost_b()
        self.proverka_delenia()

    def plots_drawer(self):
        q = 1
        A = list()
        Z = list()
        r = list()
        E = list()
        for i in range(1, int(len(self.nuclei) / 2)):
            n = 2 * (i - 1)
            Z.append(self.nuclei[n])
            A.append(self.nuclei[n + 1])
        for m in range(0, len(Z)):
            E.append(self.energy_vaizekker_plots(A[m], Z[m]))
            r.append(self.radius_plot(A[m]))
        E_sort=[]
        r_sort=[]
        A_sort=[]
        Z_sort=[]
        for f in range(0,len(E)):
            A_sort.append(min(A))
            i=A.index(min(A))
            A.pop(i)
            E_sort.append(E[i])
            E.pop(i)
            r_sort.append(r[i])
            r.pop(i)
        
        plt.figure(figsize=[18, 6])

        plt.subplot(1, 2, 1)
        plt.plot(A_sort, r_sort, linewidth=2)
        plt.ylabel('Радиус ядра, Фм')
        plt.xlabel('Массовое число, A')
        plt.title('Зависимость радиусая ядра от массового числа')
        plt.xlim([0, max(A_sort)+5])
        plt.ylim([0,max(r_sort)+1])

        plt.subplot(1, 2, 2)
        plt.plot(A_sort, E_sort, linewidth=2)
        plt.ylabel('Удельная энергия, МэВ')
        plt.xlabel('массовое число, A')
        plt.title('Зависимость удельной энергии от массового числа')
        plt.xlim([0, max(A_sort)+5])
        plt.ylim([0,max(E_sort)+1])
        plt.show()

        self.programm_main()

    def programm_main(self):
        q = 1
        while q == 1:
            print('Возможные действия:\n1. Получить информацию об элементе из списка введённых.\n2. Построить графики зависимости радиусов элементов от массового числа r(A) и удельной энергии связи от массового числа E(A).\n3. Дополнить список элементов.\n4. Завершить работу программы.')
            function = int(input('Введите номер необходимого действия: '))
            if function == 1:
                i = int(input('Введите порядковый номер элемента, для которого хотите получить информацию: '))
                self.atom_info(i)
            if function == 3:
                self.add_elements()
            if function == 2:
                self.plots_drawer()
            if function == 4:
                break


nuclear = Nucleus()
nuclear.programm_main()
