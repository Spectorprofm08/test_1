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
        for n in range(len(self.spell)):
            if (self.spell[n] == spell):
                self.mana = self.mana - self.count_mane_of_spell[n]
                character.hp = character.hp - self.damage_of_spell[n]
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
        for n in range(len(self.spell)):
            if (self.spell[n] == spell):
                self.mana = self.mana - self.count_mane_of_spell[n]
                character.hp = character.hp - self.damage_of_spell[n]
        return self.mana
fin = Character_1(100, 100)
vir = Character_2(120, 100)
# print(fin.hp,fin.mana)
# print(fin.spell[2])
# print(fin.count_mane_of_spell[2])
print(fin.cast("fireball", vir), "-fin")
print(vir.hp)
print(vir.cast("wave", fin), "-vir")
print(fin.hp)
