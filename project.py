import random

class  Character(object):
    def __init__(self):
        self.mana = 150
        self.hp = 100
class Character_1(Character):
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
class Character_2(Character):
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
fin = Character_1(100, 100)
vir = Character_2(120, 100)
attack = 0
while (vir.hp > 0) and (fin.hp > 0) and ((fin.mana > 0) or (vir.mana > 0)):
    fin_attack = random.choice(fin.spell)
    vir_attack = random.choice(vir.spell)
    if (random.randint(0,1) == 1):
        attack = attack + 1
        print("ход", attack, "Fin")
        print(fin_attack, fin.cast(fin_attack, vir), ":fin mana", ",", vir.hp, ":vir HP")
        print(vir_attack, vir.cast(vir_attack, fin), ":vir mana", ",", fin.hp, ":fin HP")
    else:
        attack = attack + 1
        print("ход", attack, "Vir")
        print(vir_attack, vir.cast(vir_attack, fin), ":vir mana", ",", fin.hp, ":fin HP")
        print(fin_attack, fin.cast(fin_attack, vir), ":fin mana", ",", vir.hp, ":vir HP")
if (fin.hp <= 0):
    print("Выйграл - Vir", "(за", attack, "ходов)")
elif (vir.hp <= 0):
    print("Выйграл - Fin", "(за", attack, "ходов)")
else:
    print("Ничья")
