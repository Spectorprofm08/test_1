import random

class  Character(object):
    def __init__(self):
        self.mana = 150
        self.hp = 100
# Vector
class Character_vect(Character):
    def __init__(self,mana, hp):
        self.hp = hp
        self.mana = mana
        self.type_element_spell = "fire" 
        self.spell = ["fire_wall", "fireball", "summon_fire"]
        self.count_mane_of_spell = [10, 20, 15]
        self.damage_of_spell = [10, 25, 5]
    def cast(self, spell, character):
        if (random.randint(0,2) == 1) and (self.mana > 0):
            for n in range(len(self.spell)):
                if (self.spell[n] == spell):
                        self.mana = self.mana - self.count_mane_of_spell[n]
                        character.hp = character.hp - self.damage_of_spell[n]
                        return self.mana
        else:
            return self.mana
# Virus
class Character_vir(Character):
    def __init__(self,mana, hp):
        self.hp = hp
        self.mana = mana
        self.Type_element_spell = "water" 
        self.spell = ["water_height", "wave", "flow"]
        self.count_mane_of_spell = [10, 15, 20]
        self.damage_of_spell = [0, 5, 25]
    def cast(self, spell, character):
        if (random.randint(0,2) == 1) and (self.mana > 0):
            for n in range(len(self.spell)):
                if (self.spell[n] == spell):
                        self.mana = self.mana - self.count_mane_of_spell[n]
                        character.hp = character.hp - self.damage_of_spell[n]
                        return self.mana
        else:
            return self.mana
# Finik
class Character_fin(Character):
    def __init__(self, mana, hp):
        self.hp = hp
        self.mana = mana
        self.Type_element_spell = "potion" 
        self.spell = ["mana_potion", "splash_ragen_potion", "ragen_potion"]
        self.count_mane_of_spell = [10, 15, 20]
        self.regen_of_spell = [25, 40, 50]
    def cast(self, spell, character):
        if (random.randint(0,2) == 1) and (self.mana > 0):
            for n in range(len(self.spell)):
                if (self.spell[n] == spell) and (spell == "mana_potion"):
                        self.mana = self.mana - self.count_mane_of_spell[n]
                        character.mana = character.mana + self.regen_of_spell[n]
                        return self.mana
                if (self.spell[n] == spell) and (spell == "splash_ragen_potion"):
                    self.mana = self.mana - self.count_mane_of_spell[n]
                    vect.hp = vect.hp + self.regen_of_spell[n]
                    vir.hp = vir.hp + self.regen_of_spell[n]
                    fin.hp = fin.hp + self.regen_of_spell[n]
                    return self.mana
                if (self.spell[n] == spell) and (spell == "ragen_potion"):
                    self.mana = self.mana - self.count_mane_of_spell[n]
                    character.hp = character.hp + self.regen_of_spell[n]
                    return self.mana
        else:
            return self.mana
# настройка маны и здоровья (mana, hp)
vect = Character_vect(100, 100)
vir = Character_vir(120, 100)
fin = Character_fin(150, 100)

# print("mana_potion", fin.cast("mana_potion", vir), ":fin mana", "=>", vir.mana, ":vir Mana")
# print("splash_ragen_potion", fin.cast("splash_ragen_potion", fin), ":fin mana", "=>", vect.hp, ":vect HP", vir.hp, ":vir HP", fin.hp, ":fin HP")
# print("ragen_potion", fin.cast("ragen_potion", vect), ":fin mana", "=>", vect.hp, ":vect HP")
# # жерибьевка хода
attack = 0
pl_vect_move = [vir,fin]
pl_vir_move = [vect,fin]
pl_fin_move = [vect,vir,fin]
while (vir.hp > 0) and (vect.hp > 0) and ((vect.mana > 0) or (vir.mana > 0)):
    move  = random.randint(0,2)
    if (move == 0):
        attack = attack + 1
        print("ход", attack, "Vector")
        vect_attack = random.choice(vect.spell)
        print(vect_attack, vect.cast(vect_attack, pl_vect_move), ":vect mana", "=>", pl_vect_move.hp, ":",pl_vect_move, "HP")
    elif (move == 1):
        attack = attack + 1
        print("ход", attack, "Virus")
        vir_attack = random.choice(vir.spell)
        print(vir_attack, vect.cast(vir_attack, pl_vir_move), ":vir mana", "=>", pl_vir_move.hp, ":",pl_vir_move, "HP")
    elif (move == 2):
        attack = attack + 1
        print("ход", attack, "Finik")
        fin_attack = random.choice(fin.spell)
        if fin_attack != "splash_ragen_potion":
            print(fin_attack, fin.cast(fin_attack, pl_fin_move), ":fin mana", "=>", pl_fin_move.hp, ":",pl_fin_move, "HP")
        else:
            print(fin_attack, fin.cast(fin_attack, fin), ":fin mana", "=>", vect.hp, ":vect HP", vir.hp, ":vir HP", fin.hp, ":fin HP")
if (vect.hp <= 0):
    print("Выйграл - Virus", "(за", attack, "ходов)")
elif (vir.hp <= 0):
    print("Выйграл - Vector", "(за", attack, "ходов)")
else:
    print("Ничья")
