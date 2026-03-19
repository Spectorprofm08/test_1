import random

class  Character(object):
    def __init__(self):
        self.mana = 150
        self.hp = 100
# Vector
class Character_vect(Character):
    def __init__(self,mana, hp, name):
        self.hp = hp
        self.mana = mana
        self.name = name
        self.type_element_spell = "fire" 
        self.spell = ["fire_wall", "fireball", "summon_fire"]
        self.count_mane_of_spell = [10, 20, 15]
        self.damage_of_spell = [10, 25, 5]
    def cast(self, spell, character):
        if (random.randint(0,1) == 1) and (self.mana > 0):
            for n in range(len(self.spell)):
                if (self.spell[n] == spell) and (self.mana >= self.count_mane_of_spell[n]):
                        self.mana = self.mana - self.count_mane_of_spell[n]
                        if (character.hp >= self.damage_of_spell[n]):
                            character.hp = character.hp - self.damage_of_spell[n]
                            return self.mana
                        else:
                            character.hp = character.hp - character.hp
                            return self.mana
        else:
            return self.mana
# Virus
class Character_vir(Character):
    def __init__(self,mana, hp, name):
        self.hp = hp
        self.mana = mana
        self.name = name
        self.Type_element_spell = "water" 
        self.spell = ["water_height", "wave", "flow"]
        self.count_mane_of_spell = [10, 15, 20]
        self.damage_of_spell = [0, 5, 25]
    def cast(self, spell, character):
        if (random.randint(0,1) == 1) and (self.mana > 0):
            for n in range(len(self.spell)):
                if (self.spell[n] == spell) and (self.mana >= self.count_mane_of_spell[n]):
                        self.mana = self.mana - self.count_mane_of_spell[n]
                        if (character.hp >= self.damage_of_spell[n]):
                            character.hp = character.hp - self.damage_of_spell[n]
                            return self.mana
                        else:
                            character.hp = character.hp - character.hp
                            return self.mana
        else:
            return self.mana
# Finik
class Character_fin(Character):
    def __init__(self, mana, hp, name):
        self.hp = hp
        self.mana = mana
        self.name = name
        self.Type_element_spell = "potion" 
        self.spell = ["mana_potion", "splash_ragen_potion", "ragen_potion"]
        self.count_mane_of_spell = [10, 15, 20]
        self.regen_of_spell = [25, 15, 35]
    def cast(self, spell, character):
        if (random.randint(0,1) == 1) and (self.mana > 0):
            for n in range(len(self.spell)):
                if (self.spell[n] == spell):
                        if (self.mana >= self.count_mane_of_spell[n]) and (spell == "mana_potion"):
                            self.mana = self.mana - self.count_mane_of_spell[n]
                            character.mana = character.mana + self.regen_of_spell[n]
                            return self.mana
                        if (self.mana >= self.count_mane_of_spell[n]) and (spell == "splash_ragen_potion"):
                            self.mana = self.mana - self.count_mane_of_spell[n]
                            vect.hp = vect.hp + self.regen_of_spell[n]
                            vir.hp = vir.hp + self.regen_of_spell[n]
                            fin.hp = fin.hp + self.regen_of_spell[n]
                            return self.mana
                        if (self.mana >= self.count_mane_of_spell[n]) and (spell == "ragen_potion"):
                            self.mana = self.mana - self.count_mane_of_spell[n]
                            character.hp = character.hp + self.regen_of_spell[n]
                            return self.mana
        else:
            return self.mana
# настройка маны и здоровья (mana, hp)
vect = Character_vect(100, 115, "Vector")
vir = Character_vir(110, 120, "Virus")
fin = Character_fin(150, 90, "Finik")

# # жерибьевка хода
attack = 0
pl_vect_move = [vir,fin]
pl_vir_move = [vect,fin]
pl_fin_move = [vect,vir,fin]


while ((vir.hp > 0) and (vect.hp > 0)) and ((vect.mana > 0) and (vir.mana > 0)):
    move  = random.randint(0,2)
    if (move == 0):
        attack = attack + 1
        print("ход", attack, "Vector")
        vect_attack = random.choice(vect.spell)
        pvm = random.choice(pl_vect_move)
        print(vect_attack, pvm.hp)
        print(vect_attack, vect.cast(vect_attack, pvm), ":vect mana", "=>", pvm.hp, ":",pvm.name, "HP")
    elif (move == 1):
        attack = attack + 1
        print("ход", attack, "Virus")
        vir_attack = random.choice(vir.spell)
        pvim = random.choice(pl_vir_move)
        print(vir_attack, pvim.hp)
        print(vir_attack, vir.cast(vir_attack, pvim), ":vir mana", "=>", pvim.hp, ":",pvim.name, "HP")
    elif (move == 2):
        attack = attack + 1
        print("ход", attack, "Finik")
        fin_attack = random.choice(fin.spell)
        pfm = random.choice(pl_fin_move)
        print(fin_attack, pfm.hp)
        if fin_attack != "splash_ragen_potion":
            print(fin_attack, fin.cast(fin_attack, pfm), ":fin mana", "=>", pfm.hp, ":",pfm.name, "HP")
        else:
            print(fin_attack, fin.cast(fin_attack, fin), ":fin mana", "=>", vect.hp, ":vect HP", vir.hp, ":vir HP", fin.hp, ":fin HP")
if (vect.hp <= 0) or (vect.mana <= 0):
    print("Выйграл - Virus", "(за", attack, "ходов)")
elif (vir.hp <= 0) or (vir.mana <= 0):
    print("Выйграл - Vector", "(за", attack, "ходов)")
elif (vect.mana <= 0) and (vir.mana <= 0):
    print("Ничья")
print(vect.name, vect.hp, vect.mana)
print(vir.name, vir.hp, vir.mana)
print(fin.name, fin.hp, fin.mana)
