import math
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient
        
class Property(Locality):
    def __init__(self, locality, name, locality_coefficient):
        self.locality = locality
        super().__init__(name, locality_coefficient)

class Estate(Property):
    def __init__(self, locality:str, name:str, locality_coefficient:float, estate_type:float, area:float):
        super().__init__(locality, name, locality_coefficient)
        self.estate_type = estate_type
        self.area = area
    def calculate_tax(self):
        tax_e = math.ceil(self.area * self.estate_type * self.locality_coefficient)
        return f"Daň je {tax_e} Kč."
    
class Residence(Property):
    def __init__(self, locality:str, name:str, locality_coefficient:float, area:float, commercial:bool):
        super().__init__(locality, name, locality_coefficient)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        tax_r = math.ceil(self.area * self.locality_coefficient * 15)
        if self.commercial == True:
            return f"Daň je {tax_r * 2} Kč."
        else:
            return f"Daň je {tax_r} Kč."
    
lesni_pozemek_0 = Estate("Střed","Mělník", 2, 0.35, 500)
byt_bydleni_1 = Residence("Pha", "Praha", 3, 60, False)
byt_podnikani_2 = Residence("Pha", "Praha", 3, 60, True)
zemedelsky_pozemek_3 = Estate("Man","Manětín", 0.8, 0.85, 900)
dum_bydleni_4 = Residence("Man", "Manětín", 0.8, 120, False)
kancelar_podnikani_5 = Residence("Morava", "Brno", 3, 90, True)

print(lesni_pozemek_0.calculate_tax())
print(byt_bydleni_1.calculate_tax())
print(byt_podnikani_2.calculate_tax())
print(zemedelsky_pozemek_3.calculate_tax())
print(dum_bydleni_4.calculate_tax())
print(kancelar_podnikani_5.calculate_tax())