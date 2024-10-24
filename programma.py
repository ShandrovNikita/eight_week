class Nucleus():
    def __init__(self, value2, value1):
        self.A = value1
        self.Z = value2
        self.N = value1-value2

    def energy_vaizekker(self):
        if self.A % 2 != 0 :
            self.energy = 15.7*self.A-17.8*self.A**(2/3)-0.71*self.Z**2/(self.A**(1/3))-23.7*((self.A-2*self.Z)**2)/self.A
        elif self.A % 2 == 0 and self.Z %2 == 0:
            self.energy = 15.7*self.A-17.8*self.A**(2/3)-0.71*self.Z**2/(self.A**(1/3))-23.7*((self.A-2*self.Z)**2)/self.A+34*(self.A)**(-3/4)
        elif self.A % 2 != 0 and self.Z != 0:
            self.energy = 15.7*self.A-17.8*self.A**(2/3)-0.71*self.Z**2/(self.A**(1/3))-23.7*((self.A-2*self.Z)**2)/self.A-34*(self.A)**(-3/4)
        self.udel_energy = self.energy/self.A
        print('�������� ������� ���� :',round(self.udel_energy,3),' ���/������')
        
    def mass(self):
        self.izbitok = self.Z*7.289 + self.N*8.071 - self.energy
        self.mass = self.izbitok + self.A * 931.5
        return print('����� ���� :',round(self.mass,3),' ��� ���',round(self.mass/931.5,3),' �.�.�.')

    def radius(self):
        self.radius = 1.4*(self.A)**(1/3)
        return print('������ ���� :',round(self.radius,3),' ��')

    def ustoychivost_b(self):
        self.Z_ravn = int(self.A/(0.015*self.A**(2/3)+2))+1 
        if self.Z != self.Z_ravn :
            print('������ ��������� � ������������ b-������')
        else :
            print('������ �������� � b-�������')

    def proverka_delenia(self):
        if self.A % 4==0 and self.Z%4==0:
            print('���� ������� �� ��� �����-������ �������')
        else: 
            print('���� �� ������� �� ��� �����-������ �������')

    def atom_info(self):
        self.energy_vaizekker()
        self.mass()
        self.radius()
        self.ustoychivost_b()
        self.proverka_delenia()


nuclei = Nucleus(92,238)
nuclei.atom_info()
