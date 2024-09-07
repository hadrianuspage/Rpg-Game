import os
import time
import random
import pickle
import re
from datetime import datetime, timedelta

def announcements():
    clear_screen()
    print()
    print("==============================")
    print("Welcome to Announcements!")
    print("==============================")
    print()
    input("Press Enter to See!")
    clear_screen()
    print("📣 Announcements")
    print("==============================")
    print("- Nerfed Fire Beam damage from 50 to 30")
    print("- Added Craft Gear Option")
    print("- Added Announcements Option")
    print("- Added Report Bugs")
    print("- Added Heal Option")
    print("- Added More Skills")
    print("- Added Level UP System")
    print("- Added 2 Redeem Codes: 'SKIL-BARU-FIRE-BEAM' and 'SKIL-HEVN-DEMN-BLST'")
    print("- Added God Powers Skill to Gacha")
    print("- Added More System and Feature")
    print("- Added New Events")
    print("==============================")
    print()
    input("Press Enter to return")

def report_bugs():
    clear_screen()
    print()
    print("==============================")
    print("Welcome to Report Bugs")
    print("==============================")
    print()
    input("Press Enter to See!")
    clear_screen()
    print("📣 Report Bugs")
    print("==============================")
    print("- Glitching text")
    print("- Material Name not showing")
    print("==============================")
    print()
    input("Press Enter to return")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class GarudaWar:
    def __init__(self, character):
        self.character = character
        self.garuda_feathers = character.garuda_feathers
        self.claimed_rewards = False  # Track if rewards have been claimed
        self.free_feathers_claimed = False  # New flag to track free Garuda Feathers claim

    def garuda_war_menu(self):
        while True:
            clear_screen()
            print("==============================")
            print("          Garuda War         ")
            print("==============================")
            print()
            print("1. Garuda Inventory")
            print("2. Garuda Market")
            print("3. Free Garuda Feathers")
            print("4. Garuda Spending")
            print("5. Garuda Battles")
            print("6. Gacha")
            print("7. Special Deals")
            print("8. Free Skill")
            print("9. Announcements")
            print("10. Exit Garuda War")
            print()
            print("==============================")
            print()
            choice = input("Choose an option: ")

            if choice == '1':
                self.show_garuda_inventory()
            elif choice == '2':
                self.garuda_market()
            elif choice == '3':
                self.free_garuda_feathers()
            elif choice == '4':
                self.garuda_spending()
            elif choice == '5':
                self.garuda_battle()
            elif choice == '6':
                self.gacha()
            elif choice == '7':
                self.special_deals()
            elif choice == '8':
                self.free_skill()
            elif choice == '9':
                self.announcements()
            elif choice == '10':
                break
            else:
                clear_screen()
                print("Invalid choice.")
                input("Press Enter to continue...")

    def show_garuda_inventory(self):
        clear_screen()
        print(f"Garuda Feathers: {self.character.garuda_feathers}")
        print()
        input("Press Enter to return to menu")

    def garuda_market(self):
        clear_screen()
        print("==============================")
        print("          Garuda Market       ")
        print("==============================")
        print()
        print("1. Garuda Chestplate (Attack: 30, HP: 40, Mana: 0) - 150 Garuda Feathers")
        print("2. Tombak (Attack: 20, HP: 15, Mana: 10) - 130 Garuda Feathers")
        print("3. War Flag (Damage: 40) - 220 Garuda Feathers")
        print("4. Garuda Sky Beam (Damage: 60) - 350 Garuda Feathers")
        print()
        print("==============================")
        
        choice = input("Choose an option to buy: ")
        if choice == '1':
            if self.character.garuda_feathers >= 150:
                self.character.garuda_feathers -= 150
                # Add gear to character's gear list
                self.character.gear.append("Garuda Chestplate")
                clear_screen()
                print("You have purchased Garuda Chestplate!")
            else:
                clear_screen()
                print("Not enough Garuda Feathers!")
        elif choice == '2':
            if self.character.garuda_feathers >= 130:
                self.character.garuda_feathers -= 130
                self.character.gear.append("Tombak")
                clear_screen()
                print("You have purchased Tombak!")
            else:
                clear_screen()
                print("Not enough Garuda Feathers!")
        elif choice == '3':
            if self.character.garuda_feathers >= 220:
                self.character.garuda_feathers -= 220
                self.character.skills.append("War Flag")
                Character.SKILLS["War Flag"] = 40
                clear_screen()
                print("You have purchased the skill: War Flag!")
        elif choice == '4':
            if self.character.garuda_feathers >= 220:
                self.character.garuda_feathers -= 220
                self.character.skills.append("Garuda Sky Beam")
                Character.SKILLS["Garuda Sky Beam"] = 60
                clear_screen()
                print("You have purchased the skill: Garuda Sky Beam!")
            else:
                clear_screen()
                print("Not enough Garuda Feathers!")
        else:
            clear_screen()
            print("Invalid choice.")
        
        input("Press Enter to return to menu...")

    def free_garuda_feathers(self):
        clear_screen()
        if not self.free_feathers_claimed:  # Check if already claimed
            self.character.garuda_feathers += 50
            self.free_feathers_claimed = True  # Mark as claimed
            print("You received 50 Garuda Feathers!")
        else:
            print("You have already claimed your free Garuda Feathers.")
        input("Press Enter to return to menu")

    def garuda_spending(self):
        clear_screen()
        total_purchases = 0
        
        while total_purchases < 25:
            print()
            print("====== Garuda Spending =====")
            print(f"\nTotal Purchases: {total_purchases}/25")
            print()
            choice = input("Choose an option:\n\n1. Spend Garuda Feathers\n\n ===========================\n\nType 'back' to exit: ").strip().lower()
            clear_screen()
            if choice == '1':
                if self.character.garuda_feathers >= 30:
                    self.character.garuda_feathers -= 30
                    total_purchases += 1
                    print("You have spent 30 Garuda Feathers!")
                else:
                    print("Not enough Garuda Feathers!")
            elif choice == 'back':
                break
            else:
                clear_screen()
                print("Invalid command.")

        if total_purchases >= 25:
            self.character.skills.append("Tembakan Tombak Ksatria")
            Character.SKILLS["Tembakan Tombak Ksatria"] = 60
            self.character.monster_keys += 4  # Add 4 Monster Keys
            print("Congratulations! You earned the skill: Tembakan Tombak Ksatria (Damage: 60) and 4 Monster Keys!")
            
        clear_screen()
        input("Press Enter to return...")

    def garuda_battle(self):
        if self.character.hp <= 0:
        	clear_screen()
        	print("Your Health is 0!")
        	print()
        	input("Press Enter to the menu")
        else:
        	clear_screen()
        print("==============================")
        print("       Garuda Battles        ")
        print("==============================")
        
        enemies = [
            {"name": "Garuda", "hp": 100, "damage": 15},
            {"name": "Banteng", "hp": 150, "damage": 20},
            {"name": "Asep", "hp": 200, "damage": 25}
        ]
        
        for enemy in enemies:
            enemy_hp = enemy["hp"]
            while enemy_hp > 0 and self.character.hp > 0:
                print(f"\nYour HP: {self.character.hp}")
                print(f"{enemy['name']}'s HP: {enemy_hp}")
                print()
                
                print("1. Attack")
                print("2. Use Skill")
                print("3. Heal")
                print("4. Flee")
                print("5. Use Aura Skill")
                print()
                action = input("Choose your action: ")

                if action == '1':
                    clear_screen()
                    damage = self.character.attack
                    enemy_hp -= damage
                    print(f"You attack {enemy['name']} for {damage} damage.")
                elif action == '2':
                    clear_screen()
                    if not self.character.skills:
                        print("You have no skills to use.")
                        continue
                    print("Available Skills:")
                    for i, skill in enumerate(self.character.skills, start=1):
                        print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")
                    skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                    clear_screen()
                    skill_name = self.character.skills[skill_choice]
                    skill_damage = Character.SKILLS.get(skill_name, 0)
                    enemy_hp -= skill_damage
                    print(f"You use {skill_name} for {skill_damage} damage.")
                elif action == '3':
                    clear_screen()
                    heal_amount = 25
                    self.character.hp = min(self.character.hp + heal_amount, self.character.max_hp)
                    print(f"You healed for {heal_amount} HP. Current HP: {self.character.hp}/{self.character.max_hp}.")
                elif action == '4':
                    clear_screen()
                    input("You fled from the battle.")
                    return
                elif action == '5':
                    clear_screen()
                    if self.character.aura:
                        aura_damage = self.character.use_aura_skill()
                        enemy_hp -= aura_damage
                    else:
                        print("You don't have any aura equipped.")
                        continue
                else:
                    clear_screen()
                    print("Invalid choice.")
                    continue

                if enemy_hp > 0:
                    damage_taken = enemy["damage"]
                    self.character.hp -= damage_taken
                    print(f"{enemy['name']} attacks you for {damage_taken} damage.")
                    if self.character.hp <= 0:
                        print("You have been defeated!")
                        self.character.hp = 0
                        print("Try Again xD")     
                        print()               
                        input("Press Enter to return menu")
                        return
                        
                if enemy_hp <= 0:
                        	print("You have defeated all enemies!")
                        	self.character.garuda_feathers += random.randint(2, 3)
                        	print(f"You received 2-3 Garuda Feathers!")
                        	print()
                        	input("Press Enter to return to menu")
                        	clear_screen()                              	
    def gacha(self):
        clear_screen()
        if self.character.garuda_feathers < 25:
            print("You don't have enough Garuda Feathers for a Gacha.")
            input("Press Enter to return to menu")
            return
            
        self.character.garuda_feathers -= 25
        result = random.choice(['Gold', 'Experience', 'Skill', 'Monster Key'])

        if result == 'Gold':
            gold_amount = random.randint(50, 300)
            self.character.gold += gold_amount
            print(f"You received {gold_amount} Gold!")
        elif result == 'Experience':
            exp_amount = random.randint(10, 50)
            self.character.experience += exp_amount
            print(f"You received {exp_amount} Experience!")
        elif result == 'Skill':
            skill = random.choice(["Garuda Shield", "Serangan Bambu Runcing", "Feathers Hit"])
            self.character.skills.append(skill)
            print(f"You received the skill: {skill}!")
        elif result == 'Monster Key':
            if random.random() < 0.01:  # 1% chance
                self.character.monster_keys += 1
                print("You found a Monster Key!")

        input("Press Enter to return to menu...")

    def special_deals(self):
        clear_screen()
        print("==============================")
        print("        Special Deals         ")
        print("==============================")
        print()
        print("1. Pukulan Asep (Damage: 35) - 5000 Gold")
        print("2. Sruduk (Damage: 40) - 250 Garuda Feathers")
        print("3. Kerupuk Throw (Damage: 50) - 300 Garuda Feathers")
        print("4. Baju Asep (Attack: 10, HP: 8, Mana: 5) - 2500 Gold")
        print("5. Garuda Feather Sword (Attack: 15, HP: 20, Mana: 30) - 200 Garuda Feathers")
        print()
        print("==============================")
        print()
        choice = input("Choose an option: ")

        if choice == '1':
            if self.character.gold >= 5000:
                self.character.gold -= 5000
                self.character.skills.append("Pukulan Asep")
                Character.SKILLS["Pukulan Asep"] = 35
                clear_screen()
                print("You have purchased 'Pukulan Asep'!")
            else:
                clear_screen()
                print("Not enough Gold.")
        elif choice == '2':
            if self.character.garuda_feathers >= 250:
                self.character.garuda_feathers -= 250
                self.character.skills.append("Sruduk")
                Character.SKILLS["Sruduk"] = 40
                clear_screen()
                print("You have purchased 'Sruduk'!")
            else:
                clear_screen()
                print("Not enough Garuda Feathers.")
        elif choice == '3':
            if self.character.garuda_feathers >= 300:
                self.character.garuda_feathers -= 300
                self.character.skills.append("Kerupuk Throw")
                Character.SKILLS["Kerupuk Throw"] = 50
                clear_screen()
                print("You have purchased 'Kerupuk Throw'!")
            else:
                clear_screen()
                print("Not enough Garuda Feathers.")
        elif choice == '4':
            if self.character.gold >= 2500:
                self.character.gold -= 2500
                self.character.gear.append("Baju Asep")
                clear_screen()
                print("You have purchased 'Baju Asep'!")
            else:
                clear_screen()
                print("Not enough Gold.")
        elif choice == '5':
            if self.character.garuda_feathers >= 200:
                self.character.garuda_feathers -= 200
                self.character.gear.append("Garuda Feather Sword")
                clear_screen()
                print("You have purchased 'Garuda Feather Sword'!")
            else:
                clear_screen()
                print("Not enough Garuda Feathers.")
        else:
            clear_screen()
            print("Invalid choice.")

        input("Press Enter to return...")

    def free_skill(self):
        clear_screen()
        choice = input("Type 'Claim Skill' to receive the skill 'Tombak Slayer' (Damage: 20): ").strip()
        if choice.lower() == 'claim skill':
            self.character.skills.append("Tombak Slayer")
            Character.SKILLS["Tombak Slayer"] = 20
            clear_screen()
            print("You received the skill: Tombak Slayer!")
        else:
            clear_screen()
            print("Invalid command.")

        input("Press Enter to return...")

    def announcements(self):
        clear_screen()
        print("Selamat datang di Garuda War ini.")
        print("Event ini dibuat untuk merayakan Hari Kemerdekaan Indonesia")
        print("yang ke 79... Happy Independence Day dan Enjoy Event 🙏")
        print()
        input("Press Enter to return to menu")
        
class Travel:
    def __init__(self, character):
        self.character = character
        self.aura = character.aura

    def travel_menu(self):
        clear_screen()
        print("==============================")
        print("          Travel Menu        ")
        print("==============================")
        print()
        print("1. Heavenly World")
        print("2. Hell World")
        print("3. Dwarf World")
        print("4. Elf World")
        print()
        
        print("==============================")
       
        print()
        choice = input("Choose a world to travel to (enter the number): ")

        if choice == '1':
            self.heavenly_world()
        elif choice == '2':
            self.hell_world()
        elif choice == '3':
            self.dwarf_world()
        elif choice == '4':
            self.elf_world()
        else:
            clear_screen()
            print("Invalid choice.")
            print()
            input("Press Enter to return to menu")

    def heavenly_world(self):
        clear_screen()
        print("==============================")
        print("        Heavenly World       ")
        print("==============================")
        print()
        print("1. Link to a God (Cost: 10.000 Gold, 5000 Experience)")
        print("2. Training Skill (Cost: 1000 Gold per skill)")
        print("3. Sales (10 Monster Keys for 15000 Gold)")
        print("4. Sky Battle against Zeus (HP: 1500, Attack: 15)")
        print()
        
        print("==============================")
        
        print()
        choice = input("Choose an option: ")

        if choice == '1':
            self.link_to_god()
        elif choice == '2':
            self.training_skill()
        elif choice == '3':
            self.sales()
        elif choice == '4':
            self.sky_battle()
        else:
            clear_screen()
            print("Invalid choice.")
            print()
            input("Press Enter to return to menu")

    def link_to_god(self):
        clear_screen()
        if self.character.gold >= 10000 and self.character.experience >= 5000: #10.000 Gold and 5000 Experience
            self.character.gold -= 5000
            self.character.experience -= 2500
            self.character.class_type = 'God'
            self.character.hp = 200
            self.character.attack = 15
            self.character.defense = 20
            self.character.skills += ['Heavenly Aura', 'Heavenly Sky Kick', 'Sky Hammer']
            print("You have received the class God and gained new skills!")
        else:
            print("You do not have enough gold or experience.")
        print()
        input("Press Enter to return to menu")

    def training_skill(self):
        clear_screen()
        print("Available Skills:")
        print()
        print("- Sky Force (30 Damage) - 1000 Gold")
        print("- Sky Initiate (70 Damage) - 1000 Gold")
        print("- Domination (0 Damage) - 1000 Gold")
        print()

        skill_choice = input("Choose a skill to buy (1-3): ")
        skill_list = ['Sky Force', 'Sky Initiate', 'Domination']
        
        if skill_choice in ['1', '2', '3']:
            skill_index = int(skill_choice) - 1
            if self.character.gold >= 1000:
                self.character.gold -= 1000
                self.character.skills.append(skill_list[skill_index])
                clear_screen()
                print(f"You have purchased {skill_list[skill_index]}!")
            else:
                clear_screen()
                print("You do not have enough gold.")
        else:
            clear_screen()
            print("Invalid skill choice.")
            
        print()
        input("Press Enter to return to menu")

    def sales(self):
        clear_screen()
        if self.character.gold >= 15000:
            self.character.gold -= 15000
            self.character.monster_keys += 10
            print("You have purchased 10 Monster Keys!")
        else:
            print("You do not have enough gold.")
            
        print()
        input("Press Enter to return menu")

    def sky_battle(self):
        clear_screen()
        print("You are fighting Zeus!")
        boss_hp = 1500
        while boss_hp > 0 and self.character.hp > 0:
            print(f"\nYour HP: {self.character.hp}")
            print(f"Zeus's HP: {boss_hp}")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Heal")
            print("4. Flee")
            print("5. Use Aura Skill")
            print()

            action = input("Choose your action: ")

            if action == '1':
                clear_screen()
                damage = 20  # Basic attack
                boss_hp -= damage
                print(f"You attack Zeus for {damage} damage.")
            elif action == '2':
                clear_screen()
                print("Available Skills:")
                for i, skill in enumerate(self.character.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")
                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                skill_name = self.character.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                boss_hp -= skill_damage
                print(f"You use {skill_name} for {skill_damage} damage.")
            elif action == '3':
                clear_screen()
                heal_amount = 25
                self.character.hp = min(self.character.hp + heal_amount, self.character.max_hp)
                print(f"You healed for {heal_amount} HP. Current HP: {self.character.hp}/{self.character.max_hp}.")
            elif action == '4':
                clear_screen()
                input("You fled from the battle.")
                return
            elif action == '5':
            	clear_screen()
            	if self.aura:
            	   aura_damage = self.use_aura_skill()
            	   monster_hp -= aura_damage
            	else:
            	   print("You don't have any aura equipped.")
            	   continue
            else:
                print("Invalid choice.")
                

            if boss_hp > 0:
                zeus_attack = 15
                self.character.hp -= zeus_attack
                print(f"Zeus attacks you for {zeus_attack} damage.")
                if self.character.hp <= 0:
                    input("You have been defeated by Zeus!")
                    return

        if boss_hp <= 0:
            print("You have defeated Zeus!")
            # Dropping rewards
            keys = random.randint(2, 3)
            gold_reward = random.randint(200, 500)
            experience_reward = random.randint(500, 1000)
            self.character.monster_keys += keys
            self.character.gold += gold_reward
            self.character.experience += experience_reward
            print(f"You received {keys} Monster Keys, {gold_reward} Gold, and {experience_reward} Experience!")
            
        print()
        input("Press Enter to return...")

    def hell_world(self):
        clear_screen()
        print("==============================")
        print("          Hell World         ")
        print("==============================")
        print()
        print("1. The Hell Battle against Lucifer (HP: 2500, Attack: 25)")
        print()
        print("==============================")
        
        print()
        choice = input("Choose an option: ")

        if choice == '1':
            self.hell_battle()
        else:
            clear_screen()
            print("Invalid choice.")
            print()
            input("Press Enter to return to menu")

    def hell_battle(self):
        clear_screen()
        print("You are fighting Lucifer!")
        boss_hp = 2500
        while boss_hp > 0 and self.character.hp > 0:
            print(f"\nYour HP: {self.character.hp}")
            print(f"Lucifer's HP: {boss_hp}")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Heal")
            print("4. Flee")
            print("5. Use Aura Skill")
            print()

            action = input("Choose your action: ")

            if action == '1':
                clear_screen()
                damage = 30  # Basic attack
                boss_hp -= damage
                print(f"You attack Lucifer for {damage} damage.")
            elif action == '2':
                clear_screen()
                print("Available Skills:")
                for i, skill in enumerate(self.character.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")
                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                skill_name = self.character.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                boss_hp -= skill_damage
                print(f"You use {skill_name} for {skill_damage} damage.")
            elif action == '3':
                clear_screen()
                heal_amount = 25
                self.character.hp = min(self.character.hp + heal_amount, self.character.max_hp)
                print(f"You healed for {heal_amount} HP. Current HP: {self.character.hp}/{self.character.max_hp}.")
            elif action == '4':
                clear_screen()
                input("You fled from the battle.")
                return
            elif action == '5':
            	clear_screen()
            	if self.aura:
            	   aura_damage = self.use_aura_skill()
            	   monster_hp -= aura_damage
            	else:
            	   print("You don't have any aura equipped.")
            	   continue
            else:
                print("Invalid choice.")

            if boss_hp > 0:
                lucifer_attack = 25
                self.character.hp -= lucifer_attack
                print(f"Lucifer attacks you for {lucifer_attack} damage.")
                if self.character.hp <= 0:
                    print("You have been defeated by Lucifer!")
                    return

        if boss_hp <= 0:
            print("You have defeated Lucifer!")
            # Dropping rewards
            keys = random.randint(3, 5)
            gold_reward = random.randint(600, 800)
            experience_reward = random.randint(500, 1000)
            self.character.monster_keys += keys
            self.character.gold += gold_reward
            self.character.experience += experience_reward
            print()
            print(f"You received {keys} Monster Keys, {gold_reward} Gold, and {experience_reward} Experience!")
        
        input("Press Enter to return...")

    def dwarf_world(self):
        clear_screen()
        print("==============================")
        print("          Dwarf World        ")
        print("==============================")
        print()
        print("1. Craft Skill (Cost: 500 Gold)")
        print()
        print("==============================")
        
        print()
        choice = input("Choose an option: ")

        if choice == '1':
            self.craft_skill()
        else:
            clear_screen()
            print("Invalid choice.")
            print()
            input("Press Enter to return to menu")

    def craft_skill(self):
        clear_screen()
        if self.character.gold < 500:
            print("You do not have enough gold to craft a skill.")
            print()
            input("Press Enter to return to menu")
            return

        if len(self.character.skills) < 2:
            print("You need at least 2 skills to craft a new skill.")
            input("Press Enter to return...")
            return

        print("Current Skills:")
        print("Note : Only Skill in list 1-5!")
        print()
        for i, skill in enumerate(self.character.skills, start=1):
            print(f"{i}. {skill}")
            
        print()
        skill_choices = input("Choose two skills to sacrifice (comma separated numbers): ")
        skill_indices = [int(i) - 1 for i in skill_choices.split(',')]
        
        if len(skill_indices) != 2 or any(i < 0 or i >= len(self.character.skills) for i in skill_indices):
            print("Invalid skills chosen.")
            input("Press Enter to return...")
            return

        self.character.gold -= 500
        new_skill = random.choice(['Dweller Sword', 'Sky Palace', 'Dwarf Aura', 'Enhance', 'Gathering Together'])
        for index in skill_indices:
            self.character.skills.remove(self.character.skills[index])

        self.character.skills.append(new_skill)
        clear_screen()
        print(f"You have crafted a new skill: {new_skill}!")
        
        print()
        input("Press Enter to return to menu")

    def elf_world(self):
        clear_screen()
        print("==============================")
        print("          Elf World          ")
        print("==============================")
        print()
        print("1. NPC: Raph")
        print()
        print("==============================")
        
        print()
        choice = input("Choose an option: ")

        if choice == '1':
            self.elf_npc()
        else:
            clear_screen()
            print("Invalid choice.")
            print()
            input("Press Enter to return to menu")

    def elf_npc(self):
        clear_screen()
        print("You meet Raph, the NPC.")
        print("1. Market")
        print("2. Defeat The Ogre")
        print()

        choice = input("Choose an action: ")

        if choice == '1':
            self.market()
        elif choice == '2':
            self.defeat_ogre()
        else:
            print("Invalid choice.")
            input("Press Enter to return...")

    def market(self):
        clear_screen()
        print("Available Skills for Sale:")
        print("- Arrow of Silence (30 Damage) - 500 Gold")
        print("- See in the dark (0 Damage) - 500 Gold")
        print()

        skill_choice = input("Choose a skill to buy (1-2): ")
        skill_list = ['Arrow of Silence', 'See in the dark']
        
        if skill_choice in ['1', '2']:
            skill_index = int(skill_choice) - 1
            if self.character.gold >= 500:
                self.character.gold -= 500
                self.character.skills.append(skill_list[skill_index])
                clear_screen()
                print(f"You have purchased {skill_list[skill_index]}!")
            else:
                clear_screen()
                print("You do not have enough gold.")
        else:
            print("Invalid skill choice.")

        input("Press Enter to return...")
             
    def defeat_ogre(self):
        clear_screen()
        print("You are fighting an Ogre!")
        ogre_hp = 800
        
        while ogre_hp > 0 and self.character.hp > 0:
            print(f"\nYour HP: {self.character.hp}")
            print(f"Ogre's HP: {ogre_hp}")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Flee")
            print("4. Use Aura Skill")
            print()

            action = input("Choose your action: ")
            clear_screen()

            if action == '1':
                clear_screen()
                damage = 10  # Basic attack damage
                ogre_hp -= damage
                print(f"You attack the Ogre for {damage} damage.")
            elif action == '2':
                clear_screen()
                print("Available Skills:")
                for i, skill in enumerate(self.character.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")
                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                skill_name = self.character.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                ogre_hp -= skill_damage
                print(f"You use {skill_name} for {skill_damage} damage.")
            elif action == '3':
                clear_screen()
                input("You fled from the battle.")
                return
            elif action == '4':
            	clear_screen()
            	if self.aura:
            	   aura_damage = self.use_aura_skill()
            	   monster_hp -= aura_damage
            	else:
            	   print("You don't have any aura equipped.")
            	   continue
            else:
                input("Invalid choice.")
                clear_screen()

            if ogre_hp > 0:
                ogre_attack = 12
                self.character.hp -= ogre_attack
                print(f"Ogre attacks you for {ogre_attack} damage.")
                if self.character.hp <= 0:
                    print("You have been defeated by the Ogre!")
                    return

        if ogre_hp <= 0:
            print("You have defeated the Ogre!")
            reward_gold = random.randint(100, 300)
            self.character.gold += reward_gold
            print()
            print(f"You gained {reward_gold} Gold!")

        input("Press Enter to return...")

                                
class Guild:
    def __init__(self, name, leader):
        self.name = name
        self.leader = leader  # Ini harus menggunakan parameter leader yang sudah diberikan
        self.members = [leader]
        self.guardian = {'name': 'Guardian', 'hp': 1000, 'attack': 20}
        self.reward_skill = 'Tower of Hall Break'  # Skill reward for the guild (100 Damage)
        self.reward_gold = 250  # Gold reward for the guild
        self.aura = leader.aura  # Pastikan merujuk ke leader, bukan character
             	
    def show_profile(self):
        clear_screen()
        print(f"Guild Name: {self.name}")
        print(f"Leader: {self.leader.name}")
        print("Members:")
        for member in self.members:
            print(f"- {member.name}")
        print()
        input("Press Enter to return to menu")

    def guild_battle(self):
        clear_screen()
        guardian_hp = self.guardian['hp']

        while guardian_hp > 0 and self.leader.hp > 0:
            print(f"\n{self.leader.name}'s HP: {self.leader.hp}")
            print(f"{self.guardian['name']}'s HP: {guardian_hp}")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Heal")
            print("4. Flee")
            print("5. Use Aura Skill")
            print()
            action = input("Choose your action: ")

            if action == '1':
                clear_screen()
                damage = self.leader.attack
                print(f"You attack {self.guardian['name']} for {damage} damage.")
                guardian_hp -= damage
            elif action == '2':
                clear_screen()
                if not self.leader.skills:
                    print("You have no skills to use.")
                    continue
                print("Available skills:")
                for i, skill in enumerate(self.leader.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")
                print()    
                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                if skill_choice < 0 or skill_choice >= len(self.leader.skills):
                    print("Invalid choice.")
                    continue
                skill_name = self.leader.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                print(f"You use {skill_name} for {skill_damage} damage.")
                guardian_hp -= skill_damage
            elif action == '3':
                clear_screen()
                heal_amount = 25
                if self.leader.hp >= self.leader.max_hp:
                    print("You are already at full health.")
                else:
                    self.leader.hp = min(self.leader.max_hp, self.leader.hp + heal_amount)
                    print(f"You healed for {heal_amount} HP. Current HP: {self.leader.hp}/{self.leader.max_hp}.")
            elif action == '4':
                clear_screen()
                print("You fled from the battle.")
                input("Back to the menu")
                return
            elif action == '5':
            	clear_screen()
            	if self.aura:
            	   aura_damage = self.use_aura_skill()
            	   monster_hp -= aura_damage
            	else:
            	   print("You don't have any aura equipped.")
            	   continue
            else:
                print("Invalid choice.")
                continue

            # Guardian attacks back if still alive
            if guardian_hp > 0:
                print(f"{self.guardian['name']} attacks you for {self.guardian['attack']} damage.")
                self.leader.hp -= self.guardian['attack']
                if self.leader.hp <= 0:
                    print("You have been defeated by the guardian!")
                    print()
                    input("Back to the menu")
                    return

        if guardian_hp <= 0:
            print(f"You have defeated the {self.guardian['name']}!")
            self.leader.gold += self.reward_gold
            self.leader.skills.append(self.reward_skill)
            print(f"You received {self.reward_gold} gold")
            print(f"You received the skill: {self.reward_skill}!")
            print()
            input("Back to the menu")
            
#class Pet taruh sini
                            
class HunterFestival:
    def __init__(self, character):
        self.character = character
        self.hunter_medals = character.hunter_medals
        self.claimed_rewards = False  # Flag to track if rewards have been claimed
        self.aura = character.aura
    

    def hunter_festival_menu(self):
        while True:
            clear_screen()
            print("==============================")
            print("       Hunter Festival        ")
            print("==============================")
            print()
            print("1. Hunter Inventory")
            print("2. Market")
            print("3. Free Gold/XP")
            print("4. Spending")
            print("5. Hunter Battle")
            print("6. Hunter Draw")
            print("7. Special Deals")
            print("8. Exit Festival")
            print()
            print("==============================")
            print()
            choice = input("Choose an option: ")

            if choice == '1':
                self.show_hunter_inventory()
            elif choice == '2':
                self.hunter_market()
            elif choice == '3':
                self.free_gold_xp()
            elif choice == '4':
                self.spending()
            elif choice == '5':
                self.hunter_battle()
            elif choice == '6':
                self.hunter_draw()
            elif choice == '7':
                self.special_deals()
            elif choice == '8':
                break
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")
     
    def free_gold_xp(self):
        clear_screen()
        print("Note : goods for farming if you want to need!")
        print()
        print("To Exit just force close to this!")
        print()
        print("1. Gold' to receive 5 Gold")
        print("2. Xp to receive 8 XP")
        print("3. Exit")
        print()
        choice = input("Typing number : ")
        if choice == '1':
            self.character.gold += 5
            clear_screen()
            print("You received 5 Gold!")
        elif choice == '2':
            self.character.experience += 8
            clear_screen()
            print("You received 8 XP!")
        elif choice == '3':
        	main()
        else:
            clear_screen()
            print("Invalid choice.")
            
        print()
        input("Press Enter to return")
        self.free_gold_xp
                                               
    def show_hunter_inventory(self):
        clear_screen()
        print(f"Hunter Medals: {self.character.hunter_medals}")  # Access from character
        print()
        input("Press Enter to return to menu")

    def hunter_market(self):
        clear_screen()
        print("==============================")
        print("          Hunter Market       ")
        print("==============================")
        print()
        print("1. Buy Gold (10 hunter medals for 200 Gold)")
        print("2. Buy XP (25 hunter medals for 200 XP)")
        print("3. Buy Monster Key ( 300 hunter medals for 1 Monster Keys )")
        print("4. Buy Monster Keys ( 600 hunter medals for 2 Monster Keys )")
        print()
        print("==============================")
        print()
        choice = input("Choose an option: ")

        if choice == '1':
            clear_screen()
            if self.character.hunter_medals >= 10:
                self.character.hunter_medals  -= 10
                self.character.gold += 200
                print("You bought 200 Gold!")
            else:
                print("Not enough hunter medals!")
        elif choice == '2':
            clear_screen()
            if self.character.hunter_medals  >= 25:
                self.character.hunter_medals  -= 25
                self.character.experience += 200
                print("You bought 200 XP!")
            else:
                print("Not enough hunter medals!")
        elif choice == '3':
            clear_screen()
            if self.character.hunter_medals  >= 300:
                self.character.hunter_medals  -= 300
                self.character.monster_keys += 1
                print("You bought 1 Monster Keys!")
        elif choice == '4':
            clear_screen()
            if self.character.hunter_medals  >= 600:
                self.character.hunter_medals  -= 600
                self.character.monster_keys += 2
                print("You bought 2 Monster Keys!")
            else:
                print("Not enough hunter medals!")
        else:
            clear_screen()
            print("Invalid choice.")
        
        input("Press Enter to return...")                        
    def spending(self):
        clear_screen()
        print("==============================")
        print("           Spending           ")
        print("==============================")
        print()
        print("Welcome to Spending!")
        print("Each purchase costs 10 hunter medals")
        print("and you must buy each item 25 times.")
        print()
        print("==============================")
        
        total_gold_purchases = 0
        total_xp_purchases = 0
        
        while total_gold_purchases < 25 or total_xp_purchases < 25:
            print(f"\nTotal Gold Purchases: {total_gold_purchases}/25")
            print(f"Total XP Purchases: {total_xp_purchases}/25")
            print()
            choice = input("Choose an option:\n1. Buy Gold\n2. Buy XP\n\nType 'back' to exit: ").strip().lower()
            clear_screen()

            if choice == '1':  # Buy Gold
                if  self.character.hunter_medals  >= 10:
                    self.character.hunter_medals  -= 10
                    self.character.gold += 50
                    total_gold_purchases += 1
                    print("You purchased 50 Gold!")
                else:
                    clear_screen()
                    print("Not enough hunter medals!")
                    
            elif choice == '2':  # Buy XP
                if self.character.hunter_medals  >= 10:
                    self.character.hunter_medals  -= 10
                    self.character.experience += 50
                    total_xp_purchases += 1
                    print("You purchased 50 XP!")
                else:
                    clear_screen()
                    print("Not enough hunter medals!")
                    
            elif choice == 'back':
                break
            else:
                clear_screen()
                print("Invalid command.")

        # Check if both purchases were completed
        if total_gold_purchases >= 25 and total_xp_purchases >= 25:
            self.skills.append("Gold Smash")
            Character.SKILLS["Gold Smash"] = 130
            self.monster_keys += 5
            clear_screen()
            print("Congratulations! You earned the skill: Gold Smash (Damage: 130) and 5 Monster Keys!")

            # Show the new skill after earning it
            print("Skills:", ", ".join(self.skills) if self.skills else "None")

        print()
        clear_screen()
        input("Press Enter to return...")
    
    
    def hunter_battle(self):
        clear_screen()
        print("==============================")
        print("         Hunter Battle        ")
        print("==============================")
        lich_hp = 250
        while lich_hp > 0 and self.character.hp > 0:
            print(f"\nYour HP: {self.character.hp}")
            print(f"Lich's HP: {lich_hp}")
            print()
            print("==============================")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Heal")
            print("4. Flee")
            print("5. Use Aura Skill")
            print()
            action = input("Choose your action: ")

            if action == '1':
                clear_screen()
                damage = 10  # Basic attack damage
                lich_hp -= damage
                print("==============================")
                print()
                print(f"You attack the Lich for {damage} damage.")
            elif action == '2':
                clear_screen()
                print("Available Skills:")
                for i, skill in enumerate(self.character.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")
                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                skill_name = self.character.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                lich_hp -= skill_damage
                print("==============================")
                print()
                print(f"You use {skill_name} for {skill_damage} damage.")
            elif action == '3':
                clear_screen()
                heal_amount = 25
                self.character.hp = min(self.character.hp + heal_amount, self.character.max_hp)
                print("==============================")
                print()
                print(f"You healed for {heal_amount} HP. Current HP: {self.character.hp}/{self.character.max_hp}.")
            elif action == '4':
                clear_screen()
                input("You fled from the battle.")
                return
            elif action == '5':
            	clear_screen()
            	if self.aura:
            	   aura_damage = self.use_aura_skill()
            	   monster_hp -= aura_damage
            	else:
            	   print("You don't have any aura equipped.")
            	   continue
            else:
                print("Invalid choice.")
                continue

            if lich_hp > 0:
                lich_attack = 10
                self.character.hp -= lich_attack
                print(f"The Lich attacks you for {lich_attack} damage.")
                if self.character.hp <= 0:
                    print("You have been defeated by the Lich!")
                    print()
                    input("Press Enter to return...")
                    return
        
        if lich_hp <= 0:
            print("You have defeated the Lich!")
            self.character.hunter_medals += random.randint(6, 8)  # Reward some hunter medals
            print("You received 6-8 Hunter Medals!")
            
        print()
        input("Press Enter to return...")

    def hunter_draw(self):
        clear_screen()
        print("==============================")
        print("         Hunter Draw         ")
        print("==============================")
        print()
        print("10 Hunter Medals for 1 Draw")
        print("30 Hunter Medals for 3 Draws")
        print()
        print("==============================")
        
        print()
        choice = input("Type '1' for 1 Draw or '3' for 3 Draws: ")
        if choice == '1':
            if self.character.hunter_medals  >= 10:
                self.character.hunter_medals  -= 10
                self.perform_draw()
            else:
                clear_screen()
                print("Not enough Hunter Medals!")
        elif choice == '3':
            if self.character.hunter_medals  >= 30:
                self.character.hunter_medals  -= 30
                for _ in range(3):
                    self.perform_draw()
            else:
                clear_screen()
                print("Not enough Hunter Medals!")
        else:
            clear_screen()
            print("Invalid choice.")
            
        print()
        input("Press Enter to return...")

    def perform_draw(self):
        outcome = random.choices(
            ["Gold", "XP", "Hunter Medal", "Skill - Grave Stab", "Monster Key"],
            weights=[50, 30, 10, 8, 2],
            k=1
        )[0]

        if outcome == "Gold":
            self.character.gold += 100
            clear_screen()
            print("You received 100 Gold!")
        elif outcome == "XP":
            self.character.experience += 50
            clear_screen()
            print("You received 50 Experience!")
        elif outcome == "Hunter Medal":
            self.character.hunter_medals  += 2
            clear_screen()
            print("You received 2 Hunter Medals!")
        elif outcome == "Skill - Grave Stab":
            if "Grave Stab" not in self.character.skills:
                self.character.skills.append("Grave Stab")
                Character.SKILLS["Grave Stab"] = 60
                clear_screen()
                print("You received the skill: Grave Stab (Damage: 60)!")
            else:
                print("You already have the skill: Grave Stab.")
        elif outcome == "Monster Key":
            self.character.skills.append("Grave Stab")
            Character.SKILLS["Grave Stab"] = 60
            self.character.monster_keys += 1
            clear_screen()
            print("You received 1 Monster Key!")
            print("You received the skill: Grave Stab (Damage: 60) !")
                      
    def special_deals(self):
        clear_screen()
        print("==============================")
        print("        Special Deals         ")
        print("==============================")
        print()
        print("1. Buy 'Summoning: Zombie Strike' (Damage: 50) - 800 Gold")
        print("2. Buy 'Dual Blade Slash' (Damage: 70) - 1200 Gold")
        print("3. Buy 'Air Shield' (Damage: 0) - 500 Gold")
        print()
        print("==============================")
        
        print()
        choice = input("Choose an option: ")

        if choice == '1':
            if self.character.gold >= 800:
                self.character.gold -= 800
                self.character.skills.append("Summoning: Zombie Strike")
                Character.SKILLS["Summoning: Zombie Strike"] = 50
                print("You have purchased 'Summoning: Zombie Strike'!")
            else:
                clear_screen()
                print("You do not have enough gold.")
        elif choice == '2':
            if self.character.gold >= 1200:
                self.character.gold -= 1200
                self.character.skills.append("Dual Blade Slash")
                Character.SKILLS["Dual Blade Slash"] = 70
                print("You have purchased 'Dual Blade Slash'!")
            else:
                clear_screen()
                print("You do not have enough gold.")
        elif choice == '3':
            if self.character.gold >= 500:
                self.character.gold -= 500
                self.character.skills.append("Air Shield")
                Character.SKILLS["Air Shield"] = 0
                print("You have purchased 'Air Shield'!")
            else:
                clear_screen()
                print("You do not have enough gold.")
        else:
            clear_screen()
            print("Invalid choice.")
            
        print()
        input("Press Enter to return...")

class Aura:
    def __init__(self, name, price, skill, skill_damage, passive_effect, attack_bonus=0, hp=0):
        self.name = name
        self.price = price
        self.skill = skill
        self.skill_damage = skill_damage
        self.passive_effect = passive_effect
        self.attack_bonus = attack_bonus  # This can be used for character attack modification
        self.hp = hp                      # This can be used for character HP modification
        self.uses = 0                      # Tracks how many times the skill has been used

    def use_skill(self):
        self.uses += 1
        return self.skill_damage

    def ultimate_skill(self):
        if self.uses >= 5:
            return self.get_ultimate_damage()
        return 0  # No ultimate skill can be used

    def get_ultimate_damage(self):
        if self.name == "Aura of Demonic":
            return 100  # Ultimate skill damage
        elif self.name == "Aura of Heavenly":
            return 80
        elif self.name == "Aura of Mystical":
            return 50
        elif self.name == "Aura of Buddha":
            return 150
        return 0
        
class DailyLogin:
    def __init__(self, character):
        self.character = character
        self.login_days = 30
        self.rewards = [
            (25, 'gold'), (25, 'experience'), (20, 'hunter_medals'), (40, 'garuda_feathers'),
            (500, 'gold'), (500, 'experience'), ("Jiegu Burst", 'skill', 10),
            ("Carnival Sword", 'gear', {'damage': 10, 'hp': 15, 'mana': 0}), (10, 'hunter_medals'), (20, 'garuda_feathers'),
            (1, 'monster_keys'), ("Carnival Taiko", 'gear', {'damage': 15, 'hp': 20, 'mana': 10}),
            (1000, 'gold'), (1000, 'experience'), ("Firework Blaster", 'skill', 25),
            (100, 'garuda_feathers'), (50, 'hunter_medals'), (1, 'level'), (1, 'attack'),
            ("Carnival Leggings", 'gear', {'damage': 25, 'hp': 20, 'mana': 10}),
            (250, 'hunter_medals'), (300, 'garuda_feathers'), (2500, 'gold'),
            (2500, 'experience'), (3, 'monster_keys'), ("Body Step Cracker Fist", 'skill', 40),
            ("Blaster Sword", 'gear', {'damage': 25, 'hp': 50, 'mana': 50}),
            (5000, 'gold'), (2, 'level'), (5, 'monster_keys')
        ]

        self.load_login_data()

    def load_login_data(self):
        if os.path.exists(f"{self.character.name}_login_data.txt"):
            with open(f"{self.character.name}_login_data.txt", 'r') as file:
                lines = file.readlines()
                self.last_login = datetime.strptime(lines[0].strip(), '%Y-%m-%d %H:%M:%S')
                self.claimed_days = list(map(int, lines[1].strip().split(',')))
        else:
            self.last_login = datetime.now() - timedelta(days=1)  # setting it initially to allow immediate first claim
            self.claimed_days = []

    def save_login_data(self):
        with open(f"{self.character.name}_login_data.txt", 'w') as file:
            file.write(self.last_login.strftime('%Y-%m-%d %H:%M:%S') + '\n')
            file.write(','.join(map(str, self.claimed_days)))

    def daily_login_menu(self):
        clear_screen()
        current_time = datetime.now()

        print("Welcome to Daily Login")
        print()
        input("Press Enter to return menu")
        clear_screen()
        print(f"Hi {self.character.name} !")
        print()
        print("------------------------------")
        print()
        print(f"Your last login was on: {self.last_login.strftime('%Y-%m-%d %H:%M:%S')}")

        if self.is_eligible_for_login(current_time):
            day_number = self.get_next_login_day()
            print(f"Today is Day {day_number + 1}.")
            print()
            if day_number < self.login_days:
                print("Type 'Sign In' to claim your daily reward.")
                print()
                choice = input("--> ")
                if choice.lower() == 'sign in':
                    self.claim_reward(day_number)
            else:
                print("You have claimed all rewards for this 30-day cycle.")
        else:
            # Handle late sign-in logic
            if self.last_login.date() == current_time.date() and current_time.hour >= 19:
                fine = 0
                # Apply late sign-in penalty
                if current_time.hour <= 23:  # Only charge if it's up to 11 PM
                    self.character.gold -= 0
                    fine = 0
                
                next_login_time = self.last_login.replace(hour=19, minute=0, second=0) + timedelta(days=1)
                print(f"You can log in next on: {next_login_time.strftime('%Y-%m-%d %H:%M:%S')}")
                if fine > 0:
                    print("You were late for your sign in! You have been charged a 0 gold fine.")

            else:
                next_login_time = self.last_login.replace(hour=19, minute=0, second=0) + timedelta(days=1)
                print(f"You can log in next on: {next_login_time.strftime('%Y-%m-%d %H:%M:%S')}")
                print("------------------------------")

        print("\nOptions:")
        print()
        print("1. Check next reward")
        print("2. Exit Daily Login")

        print()
        choice = input("Choose an option : ")
        if choice == '1':
            self.check_next_reward()
        elif choice == '2':
            return

    def is_eligible_for_login(self, current_time):
        # Check eligibility based on the last login time
        return current_time >= self.last_login + timedelta(days=1)

    def get_next_login_day(self):
        return len(self.claimed_days)  # Return the count of claimed days

    def claim_reward(self, day_number):
        if day_number in self.claimed_days:
            print("You have already claimed this reward.")
            input("Press Enter to return...")
            return

        reward = self.rewards[day_number]
        if isinstance(reward[0], int):
            if reward[1] == 'gold':
                self.character.gold += reward[0]
                clear_screen()
                print(f"You received {reward[0]} Gold!")
                print()
                input("Press Enter to return menu")
            elif reward[1] == 'experience':
                self.character.experience += reward[0]
                clear_screen()
                print(f"You received {reward[0]} Experience!")
                print()
                input("Press Enter to return menu")
            elif reward[1] == 'hunter_medals':
                self.character.hunter_medals += reward[0]
                clear_screen()
                print(f"You received {reward[0]} Hunter Medals!")
                print()
                input("Press Enter to return menu")
            elif reward[1] == 'garuda_feathers':
                self.character.garuda_feathers += reward[0]
                clear_screen()
                print(f"You received {reward[0]} Garuda Feathers!")
                print()
                input("Press Enter to return menu")
            elif reward[1] == 'monster_keys':
                self.character.monster_keys += reward[0]
                clear_screen()
                print(f"You received {reward[0]} Monster Keys!")
                print()
                input("Press Enter to return menu")
        elif isinstance(reward[0], str):  # For gear and skills
            if reward[1] == 'gear':
                self.character.gear.append(reward[0])
                self.character.gear_dict[reward[0]] = reward[2]  # Assumed dict for gear stats
                clear_screen()
                print(f"You received the gear: {reward[0]}!")
                print()
                input("Press Enter to return menu")
            elif reward[1] == 'skill':
                self.character.skills.append(reward[0])
                clear_screen()
                print(f"You received the skill: {reward[0]}!")
                print()
                input("Press Enter to return menu")

        self.claimed_days.append(day_number)  # Log the claim
        self.last_login = datetime.now()  # Update last login time
        self.save_login_data()  # Save login data
        clear_screen()
        print(f"Next available login will be tomorrow at 7 PM.")

        input("Press Enter to continue...")

    def check_next_reward(self):
        day_number = self.get_next_login_day()
        if day_number < self.login_days:
            next_reward = self.rewards[day_number]
            clear_screen()
            print(f"Next reward on Day {day_number + 1}: {next_reward[0]} {next_reward[1].capitalize() if isinstance(next_reward[1], str) else 'Gear/Skill'}!")
            if isinstance(next_reward[0], str):
                print(f"Details: {next_reward[0]}")  # For gear or skills
        print()
        input("Press Enter to return to menu")

class TheScratch:
    def __init__(self, character):
        self.character = character
        self.aura = character.aura
        self.scratch_coins = character.scratch_coins
      
                
    def scratch_menu(self):
        while True:
            clear_screen()
            print("==============================")
            print("           The Scratch        ")
            print("==============================")
            print("1. Scratch")
            print("2. Claim Scratch Coin")
            print("3. Buy Scratch Coin")
            print("4. Scratch Inventory")
            print("5. Exit Scratch")
            print("==============================")
            print()
            choice = input("Choose an option: ")

            if choice == '1':
                self.scratch()
            elif choice == '2':
                self.claim_scratch_coin()
            elif choice == '3':
                self.buy_scratch_coins()
            elif choice == '4':
            	self.inventorycoins()
            elif choice == '5':
            	break
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")
                

    def scratch(self):
        if self.character.scratch_coins <= 0:
            clear_screen()
            print("You don't have enough Scratch Coins.")
            print()
            input("Press Enter to return to menu")
            return

        # Inform the player about the maximum possible distinct numbers
        max_distinct_numbers = min(self.character.scratch_coins, 9)
        clear_screen()
        numbers = input(f"Enter 2 to {max_distinct_numbers} distinct numbers (1-{max_distinct_numbers}) separated by hyphens (e.g., 1-2-3): ")
        number_list = numbers.split('-')
        clear_screen()

        # Check the length of the number list and distinct numbers entered
        if len(number_list) < 2 or len(number_list) > max_distinct_numbers or any(num not in map(str, range(1, max_distinct_numbers + 1)) for num in number_list):
            print(f"Invalid input. Please enter between 2 and {max_distinct_numbers} distinct numbers.")
            input("Press Enter to return to menu...")
            return

        # Deduct scratch coins based on the number of choices
        self.character.scratch_coins -= len(number_list)

        # Prize distribution based on defined chances
        rewards = []
        for number in number_list:
            roll = random.random()
            if roll < 0.30:  # 30% chance for Gold
                gold_amount = random.randint(10, 100)
                rewards.append(f"{gold_amount} Gold")
                self.character.gold += gold_amount  # Add gold to character's inventory
            elif roll < 0.32:  # 40% chance for Experience
                experience_amount = random.randint(20, 100)
                rewards.append(f"{experience_amount} Experience")
                self.character.experience += experience_amount  # Add experience to character's inventory
            elif roll < 0.29:  # 10% chance for "Scratcher" skill
                rewards.append("Skill: Scratcher")
                self.character.skills.append("Scratcher")
                self.character.SKILLS["Scratcher"] = 0  # Damage of skill
            elif roll < 0.25:  # 10% chance for "Scratcher Break" skill
                rewards.append("Skill: Scratcher Break")
                self.character.skills.append("Scratcher Break")
                self.character.SKILLS["Scratcher Break"] = 30  # Damage of skill
            elif roll < 0.38:  # 10% chance for 500 Gold
                rewards.append("500 Gold")
                self.character.gold += 500  # Add 500 Gold to character's inventory
            elif roll < 0.22:  # Correcting probability for "1 Monster Key"
                rewards.append("1 Monster Key")
                self.character.monster_keys += 1
            elif roll < 0.15:
                rewards.append("4 Scratch Coin")
                self.character.scratch_coins += 4
            else:
                rewards.append("1 Scratch Coin")
                self.character.scratch_coins += 1
            	

        # Display rewards to the player
        print(f"You won: {', '.join(rewards)}!")
        input("Press Enter to return to menu...")

    def claim_scratch_coin(self):
        clear_screen()
        print("==============================")
        print("         Free Scratch Coin        ")
        print()
        print("     But You Must Battle xD       ")
        print("==============================")
        scratch_man = 200
        while scratch_man > 0 and self.character.hp > 0:
            print(f"\nYour HP: {self.character.hp}")
            print(f"Scratch Man HP: {scratch_man}")
            print()
            print("==============================")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Heal")
            print("4. Flee")
            print("5. Use Aura Skill")
            print()
            action = input("Choose your action: ")

            if action == '1':
                clear_screen()
                damage = 10  # Basic attack damage
                scratch_man -= damage
                print("==============================")
                print()
                print(f"You attack the Scratch Man for {damage} damage.")
            elif action == '2':
                clear_screen()
                print("Available Skills:")
                for i, skill in enumerate(self.character.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")
                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                skill_name = self.character.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                scratch_man -= skill_damage
                print("==============================")
                print()
                print(f"You use {skill_name} for {skill_damage} damage.")
            elif action == '3':
                clear_screen()
                heal_amount = 25
                self.character.hp = min(self.character.hp + heal_amount, self.character.max_hp)
                print("==============================")
                print()
                print(f"You healed for {heal_amount} HP. Current HP: {self.character.hp}/{self.character.max_hp}.")
            elif action == '4':
                clear_screen()
                input("You fled from the battle.")
                return
            elif action == '5':
            	clear_screen()
            	if self.aura:
            	   aura_damage = self.use_aura_skill()
            	   monster_hp -= aura_damage
            	else:
            	   print("You don't have any aura equipped.")
            	   continue
            else:
                clear_screen()
                print("Invalid choice.")
                continue

            if scratch_man > 0:
                scratch_attack = 10
                self.character.hp -= scratch_attack
                print(f"The Scratch attacks you for {scratch_attack} damage.")
                if self.character.hp <= 0:
                    print("You have been defeated by the Scratch Man!")
                    print()
                    input("Press Enter to return...")
                    return
        
        if scratch_man <= 0:
            print("You have defeated the Scratch Man!")
            self.character.scratch_coins += random.randint(1, 5)
            print("You received 1-5 Scratch Coins!")
            
        print()
        input("Press Enter to return...")
       
    def inventorycoins(self):
            clear_screen()
            print("==============================")
            print("      Your Scratch Coin     ")
            print("==============================")
            print()
            print("=> Happy Farming <=")
            print()
            print("Your Scratch Coin is : ")
            print()
            print(f"Scratch Coins : {self.scratch_coins}")
            print()
            print("==============================")
            print()
            input("Press Enter return to menu")
            print("==============================")                    
    def buy_scratch_coins(self):
        clear_screen()
        print("==============================")
        print("Buy Scratch Coins:")
        print("==============================")
        print()
        print("1. 1 Scratch Coin for 2000 Gold")
        print("2. 3 Scratch Coins for 6000 Gold")
        print("3. 9 Scratch Coins for 12000 Gold")
        print("4. Exit")
        print()
        print("==============================")
        
        print()
        choice = input("Choose an option: ")

        if choice == '1':
            clear_screen()
            if self.character.gold >= 2000:
                self.character.gold -= 2000
                self.character.scratch_coins += 1
                print("You bought 1 Scratch Coin!")
            else:
                clear_screen()
                print("Not enough Gold.")
        elif choice == '2':
            clear_screen()
            if self.character.gold >= 6000:
                self.character.gold -= 6000
                self.character.scratch_coins += 3
                print("You bought 3 Scratch Coins!")
            else:
                clear_screen()
                print("Not enough Gold.")
        elif choice == '3':
            clear_screen()
            if self.character.gold >= 12000:
                self.character.gold -= 12000
                self.character.scratch_coins += 9
                print("You bought 9 Scratch Coins!")
            else:
                clear_screen()
                print("Not enough Gold.")
        elif choice == '4':
            return
        else:
            clear_screen()
            print("Invalid choice.")

        input("Press Enter to return to menu...")
        
                                                                                   
                                                                                                                            
class Character:
    AURAS = {
        'Aura of Demonic': Aura("Aura of Demonic", 5000, "Demonic Hand Claw", 80, "Increases strength by 5", 5),
        'Aura of Heavenly': Aura("Aura of Heavenly", 3500, "Heavenly Lightning Empress Strike", 60, "Increases HP by 50", 50),
        'Aura of Mystical': Aura("Aura of Mystical", 2000, "Clouds", 0, "Increases gacha and battle success rate by 2%", 2),
        'Aura of Buddha': Aura("Aura of Buddha", 8000, "Ten Thousands Strike", 120, "Increases defense by 10", 10)
    }
    MATERIALS = ['Flower Sky', 'Burn', 'Leather Armor', 'Chain Armor']
    SKILLS = {
        'Freezer Smash': 15,
        'Burnout Flame': 20,
        'Thunder Strike': 25,
        'Wind Cutter': 10,
        'Slash': 30,
        'Shield Bash': 25,
        'Charge': 20,
        'Fireball': 5,
        'Gate Breaker': 30,
        'Gate Open': 0,
        'Heavenly Sword Slash': 45,
        'Chaos Strike': 20,
        'Dragon Wave': 15,
        'Rage Titan Smasher': 42,
        'Water': 1,
        'Blueball': 8,
        'Teleport': 0,
        'Ice Shield': 5,
        'Backstab': 25,
        'Stealth': 0,
        'Bamboo Throw': 40,
        'Poison': 12,
        'Arrow Shot': 14,
        'Trap': 0,
        'Camouflage': 0,
        'Summon Undead': 0,
        'Life Drain': 20,
        'Dark Magic': 30,
        'Meteor': 40,
        'Lightning Storm Fire': 30,
        'Arcane Blast': 35,
        'Create Portal': 0,
        'Divine Shield': 0,
        'Time Stop': 0,
        'Step Kick': 12,
        'Ground Smash': 22,
        'Quick Slash': 8,
        'Fire Whirlwind': 25,
        'Lightning Strike': 15,
        'Fire Beam': 30,
        'Universe!': 250,
        'Firestorm Chaser': 25,
        'Combination Skill: Fire Storm (Fire-Wind)': 45,
        'Combination Skill: Earth Storm (Earth-Wind)': 35,
        'Heavenly Demonic Blaster': 25,
        'Anti Magic': 75,
        'Earth Blow': 30,
        'Rage': 0,
        'Swing': 50,
        'Tower of Hall Break': 100,
        'Heavenly Aura': 0,
        'Heavenly Sky Kick': 80,
        'Sky Hammer': 50,
        'Sky Force': 30,
        'Sky Initiate': 70,
        'Domination': 0,
        'Dweller Sword': 30,
        'Sky Palace': 50,
        'Dwarf Aura': 0,
        'Enchance 0': 0,
        'Gathering Together': 0,
        'Arrow of Silence': 30,
        'See in the dark': 0,
        'Gold Smash': 130,
        'Grave Stab': 60,
        'Summoning: Zombie Strike': 50,
        'Dual Blade Slash': 70,
        'Air Shield': 0,
        'Fire Charge': 17,
        'Dragon Gale': 25,
        'Electro Strike': 40,
        'Frosty Smash': 20,
        'Bamboo Arrow': 22,
        'Inferno Spin': 45,
        'Barrier Break': 105,
        'Cursed Drain': 50,
        'Meteoric Fire': 65,
        'Sneak Slash': 33,
        'Chaotic Rage': 20,
        'Undead Frenzy': 60,
        'Storm Beam': 60,
        'Arcane Slash': 80,
        'Toxic Bash': 20,
        'Demonic Firestorm': 55,
        'Sky Barrage': 55,
        'Thunderbolt': 40,
        'Meteoric Wave': 55,
        'Raging Gate': 80,
        'Dual Demonic Slash': 70,
        'Sky Smash': 72,
        'Whirling Inferno': 50,
        'Kicking Charge': 26,
        'Earthbreaker Storm': 75,
        'Grave Gravity': 68,
        'Golden Sky Smash': 180,
        'Exploding Steps': 50,
        
        # Note : Event seperti Garuda War atau Hunter Festival tidak perlu skill nya di tambahkan disini!
        
        'Break Sky Hammer': 40,
        'Scratcher Break': 30,
        'Bite': 15,
        'Haze Claw': 35,
        'Dust Blaster': 10,
        'Brute Force': 60,
        'Summoning : Soul Abductor': 70,
        'Water Gun': 50,
        'Breeze Sky Kick': 200
        #'Tentacle Smash': 60,
        #'Two Claw': 25,
        #'Bijuu Dama': 40,
        #'Gyuki Shield': 0,
        #'Ying Yang Segel': 80
                        
    }
    GEARS = {
    'Iron Sword': {'damage': 10, 'hp': 0, 'mana': 0},
    'Steel Shield': {'damage': 0, 'hp': 20, 'mana': 0},
    'Magic Staff': {'damage': 15, 'hp': 0, 'mana': 10},
    'Leather Boots': {'damage': 0, 'hp': 5, 'mana': 5},
    'Golden Helm': {'damage': 0, 'hp': 10, 'mana': 0},
    'Iron Shield': {'damage': 15, 'hp': 15, 'mana': 0},
    'Mystic Robe': {'damage': 0, 'hp': 15, 'mana': 20},
    'Dragon Claws': {'damage': 25, 'hp': 0, 'mana': 0},
    'Bronze Axe': {'damage': 20, 'hp': 0, 'mana': 0},
    'Crystal Wand': {'damage': 10, 'hp': 0, 'mana': 15},
    'Leather Armor': {'damage': 0, 'hp': 30, 'mana': 0},
    'Plate Mail': {'damage': 0, 'hp': 40, 'mana': 0},
    'Demon Horns': {'damage': 5, 'hp': 0, 'mana': 10},
    'Phoenix Feather': {'damage': 0, 'hp': 10, 'mana': 25},
    'Warrior Gauntlets': {'damage': 5, 'hp': 10, 'mana': 0},
    'Elderwood Staff': {'damage': 18, 'hp': 0, 'mana': 12},
    'Shadow Cloak': {'damage': 0, 'hp': 10, 'mana': 5},
    'Titan Gauntlet': {'damage': 30, 'hp': 0, 'mana': 0},
    'Elven Boots': {'damage': 0, 'hp': 8, 'mana': 7},
    'Giant Shield': {'damage': 10, 'hp': 50, 'mana': 0},
    'Celestial Circlet': {'damage': 0, 'hp': 5, 'mana': 30},
    'Vampiric Dagger': {'damage': 12, 'hp': 2, 'mana': 5},
    'Frost Bracers': {'damage': 0, 'hp': 15, 'mana': 8},
    'Warlocks Robe': {'damage': 0, 'hp': 20, 'mana': 18},
    'Ancient Spear': {'damage': 22, 'hp': 0, 'mana': 2},
    'Storm Shield': {'damage': 5, 'hp': 25, 'mana': 10},
    'Abyssal Ring': {'damage': 0, 'hp': 0, 'mana': 15},
    'Garuda Chestplate': {'damage': 30, 'hp': 40, 'mana': 0},
    'Tombak': {'damage': 20, 'hp': 15, 'mana': 10},
    'Baju Asep': {'damage': 10, 'hp': 8, 'mana': 5},
    'Garuda Feather Sword': {'damage': 15, 'hp': 30, 'mana': 30},
    'Gaining Amulet': {'damage': 20, 'hp': 10, 'mana': 0},
    'Tutorial Chestplate': {'damage': 5, 'hp': 10, 'mana': 0},
    'Holy Gearbeast': {'damage': 15, 'hp': 50, 'mana': 25},
    'Great Golden Beast Armor': {'damage': 12, 'hp': 75, 'mana': 60},
    'Carnival Sword': {'damage': 10, 'hp': 15, 'mana': 0},
    'Carnival Taiko': {'damage': 15, 'hp': 20, 'mana': 10}
}

    GOD_POWERS = {
        'Zeus Lightning': {'damage': 50},
        'Time Manipulation': {'damage': 30},
        'Gravity Control': {'damage': 40},
        'Poseidon Waves': {'damage': 45},
        'Hades Shadows': {'damage': 55},
        'Aphrodite Charm': {'damage': 20},
        'Athena Wisdom': {'damage': 25},
        'Amaterasu Sun': {'damage': 60},
        'Tsukuyomi Moon': {'damage': 35},
        'Susanoo Strike': {'damage': 50},
        'Demeter Harvest': {'damage': 30},
        'Hephaestus Forge': {'damage': 40},
        'Hermes Speed': {'damage': 15},
        'Shinto Shrines': {'damage': 20},
        'Raijin Thunder': {'damage': 55},
        'Fujin Wind': {'damage': 45},
        'Inari Rice Blessing': {'damage': 0},
        'Ares War Cry': {'damage': 50},
        'Hecate Magic': {'damage': 40},
        'Kyubi no Kitsune Trickery': {'damage': 35},
        'Nana-ya Grace': {'damage': 30},
        'Chiron Healing': {'damage': 40},
        'Kaguya Moonlight': {'damage': 45},
        'Mikazuki Thunder': {'damage': 50},
        'Athena Shield': {'damage': 0},
        'Kannon Compassion': {'damage': 20},
        'Heimdall Sight': {'damage': 30},
        'Nemean Lion Strength': {'damage': 50},
        'Benten Music': {'damage': 35},
        'Soul of Yggdrasil': {'damage': 0},
        'Kappa Water Manipulation': {'damage': 30},
        'Tengu Flight': {'damage': 25},
        'Olympian Unity': {'damage': 60},
        'Asura Sky Hammer': {'damage': 80},
        'Great Heaven Creation Palm': {'damage': 60},
        'Yellow Spring Finger': {'damage': 70}
    }
    
    CLASSES = {
        'Warrior': {'hp': 120, 'attack': 15, 'defense': 10, 'skills': ['Slash', 'Shield Bash', 'Charge']},
        'Berserker': {'hp': 130, 'attack': 20, 'defense': 20, 'skills': ['Earth Blow', 'Rage', 'Swing']},
        'Mage': {'hp': 80, 'attack': 20, 'defense': 3, 'skills': ['Fireball', 'Teleport', 'Ice Shield']},
        'Rogue': {'hp': 90, 'attack': 18, 'defense': 5, 'skills': ['Backstab', 'Stealth', 'Poison']},
        'Ranger': {'hp': 100, 'attack': 17, 'defense': 6, 'skills': ['Arrow Shot', 'Trap', 'Camouflage']},
        'Necromancer': {'hp': 100, 'attack': 22, 'defense': 5, 'skills': ['Summon Undead', 'Life Drain', 'Dark Magic']},
        'Wizard': {'hp': 90, 'attack': 25, 'defense': 4, 'skills': ['Meteor', 'Arcane Blast', 'Teleport']},
        'Creator': {'hp': 110, 'attack': 18, 'defense': 8, 'skills': ['Create Portal', 'Divine Shield', 'Time Stop']},
        'God': {'hp': 200, 'attack': 15, 'defense': 20,
 'skills': ['Heavenly Aura', 'Heavenly Sky Kick', 'Sky Hammer']}
 
    }
    DEFAULT_SKILLS = ['Fireball', 'Lightning Strike', 'Fire Whirlwind']
    REDEEM_CODES = {
        'SKIL-BARU-FIRE-BEAM': ('skill', 'Fire Beam'),
        'SKIL-HEVN-DEMN-BLST': ('skill', 'Heavenly Demonic Blaster')
    }
    MARKET_ITEMS = {
        'Materials': {
            'Flower Sky': 200,
            'Burn': 250,
            'Leather Armor': 300,
            'Chain Armor': 500
        },
        'Skills': {
            'Life Drain': 150,
            'Ground Smash': 400,
            'Wind Cutter': 85,
            'Meteor': 700,
            'Anti Magic': 1250,
            'Breeze Sky Kick': 9000
        },
        'Gold': {
            '20 Gold': 15,
            '50 Gold': 150,
            '250 Gold': 750,
            '500 Gold': 1500
        },
        'Classes': {
            'Warrior': 1500,
            'Mage': 1000,
            'Rogue': 800,
            'Ranger': 1200,
            'Necromancer': 4000,
            'Wizard': 6000,
            'Creator': 8000,
            'Berserker': 3000
    }
    }
    
    def __init__(self, name, class_type=None):
        self.name = name
        self.last_claim_time = None
        self.class_type = class_type
        self.gear = []
        self.garuda_feathers = 0
        self.scratch_coins = 0
        if class_type:
            self.hp = Character.CLASSES[class_type]['hp']
            self.attack = Character.CLASSES[class_type]['attack']
            self.defense = Character.CLASSES[class_type]['defense']
            self.skills = Character.CLASSES[class_type]['skills']
        else:
            self.hp = 100
            self.attack = 10
            self.defense = 5
            self.skills = Character.DEFAULT_SKILLS.copy()
        self.level = 1
        self.experience = 0
        self.gear = []
        self.inventory = []
        self.crystal_keys = 0
        self.monster_keys = 0
        self.hunter_medals = 0
        self.gold = 0
        self.max_hp = self.hp
        self.monsters = {
            "Goblin": {'hp': 30, 'skills': {'Bite': 5}},
            "Tutorial Goblin": {'hp': 50, 'skills': {'Haste': 8}},
            "Skeleton": {'hp': 40, 'skills': {'Bone Crush': 8}},
            "Oni": {'hp': 60, 'skills': {'Club Smash': 12}},
            "Tengu": {'hp': 50, 'skills': {'Wind Slash': 15}},
            "Kappa": {'hp': 45, 'skills': {'Water Jet': 10}},
            "Jorogumo": {'hp': 70, 'skills': {'Web Trap': 20}},
            "Yuki-onna": {'hp': 65, 'skills': {'Frostbite': 18}},
            "Dragon": {'hp': 100, 'skills': {'Fire Breath': 25}},
            "Kitsune": {'hp': 55, 'skills': {'Illusion': 14}},
            "Shinigami": {'hp': 75, 'skills': {'Death Scythe': 22}},
            "Awakened Goblin": {'hp': 35, 'skills': {'Savage Bite': 7}},
            "Awakened Skeleton": {'hp': 50, 'skills': {'Skeleton Strike': 11}},
            "Mini Goblin": {'hp': 90, 'skills': {'Bite X': 5}},
            "Dungeon Wraith": {'hp': 55, 'skills': {'Soul Drain': 16}},
            "Tower Guardian": {'hp': 80, 'skills': {'Shield Slam': 20}},
            "Cave Troll": {'hp': 70, 'skills': {'Rock Throw': 15}},
            "Golem": {'hp': 90, 'skills': {'Earthquake': 25}},
            "Phantom Knight": {'hp': 65, 'skills': {'Dark Strike': 18}},
            "Demon": {'hp': 75, 'skills': {'Infernal Fire': 22}},
            "Giant Spider": {'hp': 50, 'skills': {'Venom Bite': 12}},
            "Shadow Beast": {'hp': 40, 'skills': {'Shadow Claw': 10}},
            "Shadow Lich": {'hp': 60, 'skills': {'Necrotic Touch': 19}},
            "Fire Elemental": {'hp': 55, 'skills': {'Flame Burst': 17}},
            "Ice Elemental": {'hp': 55, 'skills': {'Frost Blast': 17}}
        }
        
        self.skills_dict = {}
        self.gear_dict = {}
        self.aura = None
        self.god_power = None

    def god_challenger(self):
        clear_screen()
        
        gods = [
            {'name': 'Thor', 'hp': 600, 'attack': 12},
            {'name': 'Odin', 'hp': 800, 'attack': 25},
            {'name': 'Hamiel', 'hp': 1200, 'attack': 8},
            {'name': 'Chronos', 'hp': 1500, 'attack': 20},
            {'name': 'Chaos', 'hp': 500, 'attack': 5},
            {'name': 'Hermes', 'hp': 600, 'attack': 14},
            {'name': 'God of Destruction', 'hp': 2500, 'attack': 30},
        ]

        print("==============================")
        print("        God Challenger        ")
        print("==============================")
        print("Choose your opponent to battle :")
        print()
        for i, god in enumerate(gods, start=1):
            print(f"{i}. {god['name']} (HP: {god['hp']}, Attack: {god['attack']})")
            
        print()
        choice = int(input("Select a god to challenge (1-7): ")) - 1
        selected_god = gods[choice]
        
          
        god_hp = selected_god['hp']
        god_attack = selected_god['attack']
        
        clear_screen()
        print(f"\nYou are fighting {selected_god['name']}!")
        
        while god_hp > 0 and self.hp > 0:
            print(f"\nYour HP: {self.hp}")
            print(f"{selected_god['name']}'s HP: {god_hp}")
            print()
            print("Choose your action:")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Heal")
            print("4. Use Aura Skill")
            print("5. Flee")
            
            print()
            action = input("Your choice: ")
            clear_screen()

            if action == '1':
                clear_screen()
                damage = 10  # Basic attack damage
                god_hp -= damage
                print(f"You attack {selected_god['name']} for {damage} damage.")
                
            elif action == '2':
                clear_screen()
                if not self.skills:
                    print("You have no skills to use.")
                    continue
                print("Available Skills:")
                for i, skill in enumerate(self.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")

                skill_choice = int(input("Choose a skill to use (Enter the number): ")) - 1
                clear_screen()
                skill_name = self.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                god_hp -= skill_damage
                print(f"You use {skill_name} for {skill_damage} damage.")
                
            elif action == '3':
                clear_screen()
                heal_amount = 25
                self.hp = min(self.hp + heal_amount, self.max_hp)
                print(f"You healed for {heal_amount} HP. Current HP: {self.hp}/{self.max_hp}.")
                
            elif action == '4':
                clear_screen()
                if self.aura:
                    damage = self.use_aura_skill()
                    god_hp -= damage
                    print(f"You deal {damage} damage with your aura skill!")
                else:
                    print("You don't have any aura equipped.")
                    continue
                    
            elif action == '5':
            	clear_screen()
            	flees = random.choice([True, False])
            	if flees:
            		print("You fled from the battle successfully!")
            		print()
            		input("Press Enter to return menu")
            		return
            	else:
            		print("You couldn't flee and face your punishment!")
            		self.hp -= 25  # Penalty for fleeing
            		print("You lose 25 HP due to failed escape!")
            		# Ensure that the health does not go below 0
            		self.hp = max(self.hp, 0)  # Make sure hp doesn't go negative


            # God attacks back if still alive
            if god_hp > 0:
                print(f"{selected_god['name']} attacks you for {god_attack} damage.")
                print()
                print("===================================================================")
                print()
                self.hp -= god_attack

                if self.hp <= 0:
                    print("You have been defeated!")
                    self.hp = 0
                    return
        
        if god_hp <= 0:
            print(f"You have defeated {selected_god['name']}!")
            reward = random.choices(
                ['Gold', 'Experience', 'Monster Key', 'Odin Breaker Sky Smasher', 'Light Judgement', 
                 'Time Sky Lance', 'Void Destruction', 'Tribe Aura', '3-5 Monster Keys'],
                weights=[20, 20, 5, 5, 2, 2, 2, 3, 1],
                k=1)[0]

            if reward == 'Gold':
                gold_amount = random.randint(200, 500)
                self.gold += gold_amount
                print(f"You received {gold_amount} Gold!")
            elif reward == 'Experience':
                exp_amount = random.randint(200, 500)
                self.experience += exp_amount
                print(f"You gained {exp_amount} Experience!")
            elif reward == 'Monster Key':
                self.monster_keys += 1
                print("You found a Monster Key!")
            elif reward == 'Odin Breaker Sky Smasher':
                self.skills.append("Odin Breaker Sky Smasher")
                Character.SKILLS["Odin Breaker Sky Smasher"] = 70
                print("You received the skill: Odin Breaker Sky Smasher!")
            elif reward == 'Light Judgement':
                self.skills.append("Light Judgement")
                Character.SKILLS["Light Judgement"] = 80
                print("You received the skill: Light Judgement!")
            elif reward == 'Time Sky Lance':
                self.skills.append("Time Sky Lance")
                Character.SKILLS["Time Sky Lance"] = 100
                print("You received the skill: Time Sky Lance!")
            elif reward == 'Void Destruction':
                self.skills.append("Void Destruction")
                Character.SKILLS["Void Destruction"] = 120
                print("You received the skill: Void Destruction!")
            else:  # 3-5 Monster Keys
                keys_found = random.randint(3, 5)
                self.monster_keys += keys_found
                print(f"You received {keys_found} Monster Keys!")
        
        input("Press Enter to return to menu...")        
    def daily_gacha(self):
        clear_screen()
        current_time = datetime.now()

        # Check if the 24-hour period has passed
        if self.last_claim_time and current_time < self.last_claim_time + timedelta(days=1):
            clear_screen()
            print("You can only attempt the Daily Gacha once a day.")
            print("Please try again tomorrow.")
            print()
            input("Press Enter to return to menu")
            return
            
        clear_screen()    
        print("Attempting to Daily Gacha...")
        print()
        input("Press Enter to Gacha!")
        
        # Implementing reward logic
        reward_type = random.choices(['Gold', 'Experience', 'Skill', 'Gold/Experience', 'MonsterKey'],
                                      weights=[40, 40, 10, 9, 1],
                                      k=1)[0]

        if reward_type == 'Gold':
            reward_amount = random.randint(50, 150)
            self.gold += reward_amount
            clear_screen()
            print(f"You received {reward_amount} Gold!")

        elif reward_type == 'Experience':
            reward_amount = random.randint(50, 150)
            self.experience += reward_amount
            clear_screen()
            print(f"You gained {reward_amount} Experience!")

        elif reward_type == 'Skill':
            skill_name = "Water Gun"  # Fixed skill for this reward
            if skill_name not in self.skills:
                self.skills.append(skill_name)
                Character.SKILLS[skill_name] = 50  # Setting the skill damage
                clear_screen()
                print(f"You received the skill: {skill_name} with damage 50!")
            else:
                print(f"You already have the skill: {skill_name}.")

        elif reward_type == 'Gold/Experience':
            choice = random.choice(['Gold', 'Experience'])
            reward_amount = random.randint(500, 750)
            if choice == 'Gold':
                self.gold += reward_amount
                clear_screen()
                print(f"You received {reward_amount} Gold!")
            else:
                self.experience += reward_amount
                clear_screen()
                print(f"You gained {reward_amount} Experience!")

        elif reward_type == 'MonsterKey':
            self.monster_keys += 1
            clear_screen()
            print("You found 1 Monster Key!")

        self.last_claim_time = current_time  # Update the time of the last gacha
        
        print()
        print("Daily Gacha attempt completed.")
        input("Press Enter to return to menu")                                                    
    def announcements_guild(self):
    	clear_screen()
    	print("This guild on beta phase!")
    	print()
    	input("Press Enter to return menu")
    
    def equip_aura(self, aura_name):
        if aura_name in Character.AURAS and self.gold >= Character.AURAS[aura_name].price:
        	self.aura = Character.AURAS[aura_name]
        	self.gold -= self.aura.price
        	# Terapkan bonus serangan dari aura
        	self.attack += self.aura.attack_bonus  # Misalkan Aura Of Demonic memiliki attack_bonus = 5
        	self.max_hp += self.aura.hp  # Terapkan bonus HP dari aura
        	print(f"You have equipped {self.aura.name}!")
        	print(f"Passive Effect: {self.aura.passive_effect}")
        else:
        	print(f"You don't have enough gold to equip {aura_name} or you has been bugged please to return and re enter again!")
    
    def use_aura_skill(self):
        if self.aura:
            damage = self.aura.use_skill()
            print(f"You used {self.aura.skill} for {damage} damage!")
            ultimate_damage = self.aura.ultimate_skill()
            if ultimate_damage > 0:
                print(f"Ultimate Skill: {self.aura.get_ultimate_damage()} activated!")
            return damage
        else:
            print("You don't have any aura equipped.")
            return 0
            
    def aura_shop(self):
        clear_screen()
        print("==============================")
        print("          Aura Shop          ")
        print("==============================")
        for aura_name, aura in Character.AURAS.items():
            print(f"{aura_name}: {aura.price} Gold - Skill: {aura.skill} (Damage: {aura.skill_damage})")
            print(f"Passive Effect: {aura.passive_effect}")
            print()
        
        print("==============================")
        print()
        choice = input("Enter the name of the aura you wish to buy: ")
        clear_screen()
        self.equip_aura(choice)
        print()
        input("Press Enter to return to menu")
                  
    def treasure_hunt(self):
        clear_screen()
        input("??? : Are You Ready?")
        input("You : Yes Captain!")
        print()
        input("Press to Enter!")
        clear_screen()
        print("==============================")
        print("       Treasure Hunt         ")
        print("==============================")
        print("You are embarking on a treasure hunt!")
        print("Be cautious, as there may be challenges ahead!")
        print("==============================")

        # Randomly select between encountering challenges or special events
        event = random.choice(['challenge', 'treasure_man', 'treasury_sales'])

        if event == 'challenge':
            challenges = random.randint(1, 3)  # 1 to 3 challenges
            total_treasure = 0

            for i in range(challenges):
                print(f"\nChallenge {i + 1}:")
                challenge_success = random.choice([True, False])  # Randomly determine success
                if challenge_success:
                    treasure_found = random.randint(50, 200)  # Treasure range
                    total_treasure += treasure_found
                    print(f"You overcame the challenge and found {treasure_found} Gold!")
                else:
                    loss = random.randint(10, 50)  # Gold loss range
                    self.gold -= loss
                    print(f"You faced a setback and lost {loss} Gold!")

            # Final treasure collection
            if total_treasure > 0:
                self.gold += total_treasure
                print(f"\nYour total treasure earned: {total_treasure} Gold!")

        elif event == 'treasure_man':
            self.treasure_man_battle()

        elif event == 'treasury_sales':
            self.treasury_sales()
        
        print()       
        print("Hunt is complete! Thank you for participating.")
        print()
        input("Press Enter to return to menu")

    def treasure_man_battle(self):
        clear_screen()
        print("==============================")
        print("       You Encountered        ")
        print("         Treasure Man!       ")
        print("==============================")
        print()
        print("Prepare for battle!")
        print()
        print("==============================")
        
        treasure_man_hp = 500
        while treasure_man_hp > 0 and self.hp > 0:
            effective_attack = self.attack + (self.aura.attack_bonus if self.aura else 0)
            print(f"\nYour HP: {self.hp}")
            print(f"Treasure Man's HP: {treasure_man_hp}")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Heal")
            print("4. Flee")
            print("5. Use Aura Skill")
            print()
            action = input("Choose your action: ")

            if action == '1':
                clear_screen()
                damage = effective_attack
                treasure_man_hp -= damage
                print(f"You attack Treasure Man for {damage} damage.")
            elif action == '2':
                clear_screen()
                if not self.skills:
                    print("You have no skills to use.")
                    continue
                print("Available skills:")
                for i, skill in enumerate(self.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")

                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                skill_name = self.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                treasure_man_hp -= skill_damage
                print(f"You use {skill_name} for {skill_damage} damage.")

            elif action == '3':
                clear_screen()
                heal_amount = 25
                self.hp = min(self.hp + heal_amount, self.max_hp)
                print(f"You healed for {heal_amount} HP. Current HP: {self.hp}/{self.max_hp}.")
            elif action == '4':
                clear_screen()
                input("You fled from the battle.")
                return
            elif action == '5':
            	clear_screen()
            	if self.aura:
            	   aura_damage = self.use_aura_skill()
            	   monster_hp -= aura_damage
            	else:
            	   print("You don't have any aura equipped.")
            	   continue
            else:
                clear_screen()
                print("Invalid choice.")
            
            # Treasure Man attacks back
            if treasure_man_hp > 0:
            	evade_chance = random.randint(1, 100)
            	if evade_chance <= self.defense:
            	   print("You dodged the attack!")
            	else:
            	   attack_damage = 15
            	   self.hp -= attack_damage
            	   print(f"Treasure Man attacks you for {attack_damage} damage.")

            if self.hp <= 0:
                print("You have been defeated by the Treasure Man!")
                self.hp = 0
                return

        if treasure_man_hp <= 0:
            print("You have defeated the Treasure Man!")
            reward_choice = random.choice(['gold', 'skill'])
            if reward_choice == 'gold':
                reward_gold = 200
                self.gold += reward_gold
                print(f"You received {reward_gold} Gold!")
            else:
                self.skills.append("Treasury Break")
                Character.SKILLS["Treasury Break"] = 30
                print("You received the skill: Treasury Break (Damage: 30)!")
                
        print()
        input("Press Enter to return to menu.")

    def treasury_sales(self):
        clear_screen()
        print("==============================")
        print("        Treasury Sales        ")
        print("==============================")
        
        chance = random.randint(1, 100)
        if chance <= 1:  # 1% chance for the rare skill
            self.skills.append("Golden Rich Punch")
            Character.SKILLS["Golden Rich Punch"] = 50
            print("You found the rare skill: Golden Rich Punch (Damage: 50)! Congratulations!")
        else:
            gold_found = random.randint(100, 300)
            experience_found = random.randint(50, 150)
            self.gold += gold_found
            self.experience += experience_found
            print()
            print(f"You found {gold_found} Gold and gained {experience_found} Experience!")
            
        print()
        input("Press Enter to return to menu.")
        
    def upgrade_skill(self):
        clear_screen()
        
        if not self.skills:
            clear_screen()
            print("You have no skills to upgrade.")
            input("Press Enter to return to menu...")
            return
        
        print("Available Skills for Upgrade:")
        print()
        for i, skill in enumerate(self.skills, start=1):
            print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")
        
        print()
        skill_choice = int(input("Choose a skill to upgrade (enter the number): ")) - 1
        
        if skill_choice < 0 or skill_choice >= len(self.skills):
            clear_screen()
            print("Invalid skill selected.")
            input("Press Enter to return to menu...")
            return
        
        skill_name = self.skills[skill_choice]
        current_damage = Character.SKILLS[skill_name]
        next_level_damage = current_damage + 10  # Increase damage by 10 for each upgrade
        
        # Determine the upgrade cost - starts at 200 and doubles for each level
        upgrade_level = 1
        while (skill_name + f" II") in Character.SKILLS or (skill_name + f" III") in Character.SKILLS or \
              (skill_name + f" IV") in Character.SKILLS or (skill_name + f" V") in Character.SKILLS:
            upgrade_level += 1
            skill_name = f"{skill_name[:-1]} {upgrade_level}" if upgrade_level < 5 else skill_name
        
        cost = 200 * (2 ** (upgrade_level - 1))  # Calculate upgrade cost

        if self.gold < cost:
            clear_screen()
            print(f"You do not have enough gold to upgrade! Upgrade cost: {cost} Gold.")
            input("Press Enter to return to menu...")
            return
        
        # Perform the upgrade
        self.gold -= cost
        new_skill_name = f"{self.skills[skill_choice]} {upgrade_level}" if upgrade_level < 5 else self.skills[skill_choice]
        Character.SKILLS[new_skill_name] = next_level_damage
        self.skills[skill_choice] = new_skill_name  # Update skill name in the skill list
        clear_screen()
        print(f"You have upgraded to {new_skill_name} (Damage: {next_level_damage})!")
        
        input("Press Enter to return to menu...")
        
    def buy_stats(self):
        clear_screen()
        print("==============================")
        print("         Stats Shop")
        print("==============================")
        print()
        print("Available Stats : ")
        print()
        print("1. UP Strength - Increase Attack by 1 (4000 Gold)")
        print("2. UP Health - Increase HP by 15 (2000 Gold)")
        print("3. UP Growth - Increase Level by 1 and HP by 30 (8000 Gold)")
        print("4. UP Defense - Increase Defense by 1 (5000 Gold)")
        print()
        print("==============================")                                           
        print()      
        choice = input("Select a stats to buy (1-4) or 'exit' to leave: ")        

        if choice == '1':
            if self.gold >= 4000:
                self.attack += 1
                self.gold -= 4000
                clear_screen()
                print("You have purchased Strength!")
            else:
                clear_screen()
                print("You do not have enough gold.")
        elif choice == '2':
            if self.gold >= 2000:
                self.hp += 15  # Heal current HP too
                self.gold -= 2000
                clear_screen()
                print("You have purchased Health!")
            else:
                clear_screen()
                print("You do not have enough gold.")
        elif choice == '3':
            if self.gold >= 8000:
                self.level += 1
                self.hp += 30        # Increase max HP
                self.gold -= 8000
                clear_screen()
                print("You have purchased Level!")
            else:
                clear_screen()
                print("You do not have enough gold.")
        elif choice == '4':
            if self.gold >= 5000:
                self.defense += 1
                self.gold -= 5000
                clear_screen()
                print("You have purchased Defense!")
            else:
                clear_screen()
                print("You do not have enough gold.")
        else:
            clear_screen()
            print("Invalid choice.")

        input("Press Enter to return")
            
    def create_guild(self):
        clear_screen()
        if self.gold < 1000:  # Update check for creating guild
            print("You do not have enough gold to create a guild.")
            print()
            print("Need 1000 Gold")
            print()
            input("Press Enter to return to menu")
            return

        guild_name = input("Enter the name of your guild: ")
        clear_screen()
        self.gold -= 1000  # Deduct the cost for creating a guild
        self.guild = Guild(guild_name, self)  # Create a new guild
        print(f"Guild '{guild_name}' created successfully!")
        print()
        input("Press Enter to return to menu")

    def join_guild(self, guild):
        if hasattr(self, 'guild'):
            print("You are already in a guild. Leave your current guild to join a new one.")
            input("Press Enter to return to menu...")
            return

        guild.members.append(self)
        self.guild = guild
        print(f"You have joined the guild: {guild.name}!")

    def leave_guild(self):
        if not hasattr(self, 'guild'):
            print("You are not a member of any guild.")
            input("Press Enter to return to menu")
            return

        guild_name = self.guild.name
        self.guild.members.remove(self)  # Remove from guild members
        del self.guild  # Remove the guild from the character
        clear_screen()
        print(f"You have left the guild: {guild_name}")
        print()
        input("Press Enter to return to menu")
       
                     
    def arena(self):
        clear_screen()
        
        print("Welcome to the Arena! You can fight monsters in a row.")
        print()
        monster_count = int(input("How many monsters do you want to fight (5-20) : "))
        
        if monster_count < 5 or monster_count > 20:
            clear_screen()
            print("Invalid number of monsters. Please choose between 5 and 20!")
            print()
            input("Press Enter to return to menu")
            return
        
        total_gold = 0
        total_monster_keys = 0
        
        for i in range(monster_count):
            clear_screen()
            print(f"Round {i + 1} of {monster_count}")

            # Randomly select a monster from the available ones
            monster_name, monster = random.choice(list(self.monsters.items()))
            monster_hp = monster['hp']
            
            while monster_hp > 0 and self.hp > 0:
                # Get effective attack considering aura
                effective_attack = self.attack + (self.aura.attack_bonus if self.aura else 0)
                print(f"\nYour HP: {self.hp}")
                print(f"{monster_name}'s HP: {monster_hp}")
                print()
                print("1. Attack")
                print("2. Use Skill")
                print("3. Flee")
                print("4. Use Aura Skill")
                print()
                action = input("Choose your action: ")

                if action == '1':
                    clear_screen()
                    damage = effective_attack
                    print(f"You attack {monster_name} for {damage} damage.")
                    monster_hp -= damage
                elif action == '2':
                    clear_screen()
                    if not self.skills:
                        print("You have no skills to use.")
                        continue
                    print("Available skills:")
                    for i, skill in enumerate(self.skills, start=1):
                        print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")

                    skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                    clear_screen()
                    skill_name = self.skills[skill_choice]
                    skill_damage = Character.SKILLS.get(skill_name, 0)
                    print(f"You use {skill_name} for {skill_damage} damage.")
                    monster_hp -= skill_damage
                elif action == '3':
                    clear_screen()
                    print("You fled from the battle.")
                    return
                elif action == '4':
                	clear_screen()
                	if self.aura:
                		aura_damage = self.use_aura_skill()
                		monster_hp -= aura_damage
                	else:
                		print("You don't have any aura equipped.")
                		continue
                else:
                    print("Invalid choice.")

                # Monster attacks back
                if monster_hp > 0:
                    evade_chance = random.randint(1, 100)
                    if evade_chance <= self.defense:
                    	print("You dodged the attack!")
                
                    monster_attack = monster['skills'].get('Bite', 5)
                    print(f"{monster_name} attacks you for {monster_attack} damage.")
                    self.hp -= monster_attack

                if self.hp <= 0:
                    print("You have been defeated in the arena!")
                    self.hp = 0
                    return

            if monster_hp <= 0:
                print(f"You have defeated {monster_name}!")
                if random.random() < 0.04:  # 0.04% chance to get rewards
                    gold_reward = random.randint(50, 200) * (i + 1)
                    monster_key_reward = random.randint(1, 3) * (i + 1)
                    total_gold += gold_reward
                    total_monster_keys += monster_key_reward
                    print(f"You have received {gold_reward} Gold and {monster_key_reward} Monster Keys!")
                else:
                    experience_reward = random.randint(100, 500)
                    self.experience += experience_reward
                    print(f"You gained {experience_reward} experience!")
                
        # Final results after all rounds
        if total_gold > 0 or total_monster_keys > 0:
            self.gold += total_gold
            self.monster_keys += total_monster_keys

        input("Press Enter to return to menu...")
        
    def pvp_battle(self):
        clear_screen()
        player_hp = 100
        print("You are now fighting against the PVP Bot : Player")
        
        while player_hp > 0 and self.hp > 0:
            # Get effective attack considering aura
            effective_attack = self.attack + (self.aura.attack_bonus if self.aura else 0)
            print(f"\nYour HP: {self.hp}")
            print(f"Player's HP: {player_hp}")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Flee")
            print("4. Use Aura Skill")
            print()
            action = input("Choose your action: ")

            if action == '1':
                clear_screen()
                damage = effective_attack  # your basic attack damage
                print(f"You attack Player for {damage} damage.")
                player_hp -= damage
            elif action == '2':
                clear_screen()
                if not self.skills:
                    print("You have no skills to use.")
                    continue
                print("Available skills:")
                for i, skill in enumerate(self.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")

                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                skill_name = self.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                print(f"You use {skill_name} for {skill_damage} damage.")
                player_hp -= skill_damage
            elif action == '3':
                clear_screen()
                print("You fled from the battle.")
                return
            elif action == '4':
                	clear_screen()
                	if self.aura:
                		aura_damage = self.use_aura_skill()
                		monster_hp -= aura_damage
                	else:
                		print("You don't have any aura equipped.")
                		continue
            else:
                print("Invalid choice.")

            # Player (the bot) attacks back
            if player_hp > 0:
            	evade_chance = random.randint(1, 100)
            	if evade_chance <= self.defense:
            	   print("You dodged the attack!")
            	else:
            	   player_attack = 15  # Fixed damage for bot's basic attack
            	   print(f"Player attacks you for {player_attack} damage.")
            	   self.hp -= player_attack

            if self.hp <= 0:
                print("You have been defeated by the Player!")
                self.hp = 0
                break

        if player_hp <= 0:
            print("You have defeated the Player!")
            experience_reward = random.randint(1, 10)
            self.experience += experience_reward
            print(f"You gained {experience_reward} experience!")
            print("You've won the PVP battle!")
        input("Press Enter to return to menu...")
         
    def open_package(self):
        clear_screen()
        
        if self.last_claim_time:
                if datetime.now() < self.last_claim_time + timedelta(hours=12):
                	print("You can only claim again after 12 hours from your last claim.")
                	input("Press Enter to return to menu")
                	return
        print("==============================")
        print("         Packages")
        print("==============================")
        print()
        print("Available Packages:")
        print()
        print("Experience Package")
        print("Gold Package")
        print("Skill Package")
        print("Monster Key Package")
        print("Special Key Package")
        print()
        print("==============================")

        packages = {
            "Experience Package": (5, 500),  # Level 5, 500 Experience
            "Gold Package": (10, 1000),       # Level 10, 1000 Gold
            "Skill Package": (30, "Bamboo Throw"),  # Level 30, Skill "Bamboo Throw"
            "Monster Key Package": (40, 5),  # Level 40, 5 Monster Keys
            "Special Key Package": (60, 10), # Level 60, 10 Monster Keys
        }

        for package_name, (required_level, reward) in packages.items():
            if self.level >= required_level:
                print()
                print(f"- {package_name} (Unlocks at Level {required_level})")

        print()
        choice = input("Enter the name of the package you want to open or type 'exit' to leave: ").strip()

        if choice in packages:
            required_level, reward = packages[choice]
            if self.level >= required_level:
                if isinstance(reward, int):
                    
                    if choice == "Experience Package":
                        self.last_claim_time = datetime.now()
                        self.experience += reward
                        clear_screen()
                        print(f"You received {reward} Experience!")
                    elif choice == "Gold Package":
                        self.last_claim_time = datetime.now()
                        self.gold += reward
                        clear_screen()
                        print(f"You received {reward} Gold!")
                    elif "Monster Key Package" in choice:
                        self.last_claim_time = datetime.now()
                        self.monster_keys += reward
                        clear_screen()
                        print(f"You received {reward} Monster Keys!")
                    
                    elif "Special Key Package" in choice:
                        self.last_claim_time = datetime.now()
                        self.monster_keys += reward
                        clear_screen()
                        print(f"You received {reward} Monster Keys!")

                elif reward == "Bamboo Throw":  # Skill reward
                    if reward not in self.skills:
                        self.last_claim_time = datetime.now()
                        self.skills.append(reward)
                        clear_screen()
                        Character.SKILLS[reward] = 40  # Add damage for the new skill
                        print(f"You have received the skill: {reward} (Damage: 40)!")
            else:
                clear_screen()
                print(f"You need to be at least level {required_level} to open this package.")
        else:
            clear_screen()
            print("Invalid package name.")

        print()
        input("Press Enter to return to menu")
             
    def battle_boss(self):
        clear_screen()
        boss_name = "God of Tower"
        boss_hp = 2000
        
        print(f"Boss: {boss_name}")
        
        while boss_hp > 0 and self.hp > 0:
            # Get effective attack considering aura
            effective_attack = self.attack + (self.aura.attack_bonus if self.aura else 0)
            print(f"\nYour HP: {self.hp}")
            print(f"{boss_name}'s HP: {boss_hp}")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Flee")
            print("4. Use Aura Skill")
            print()
            action = input("Choose your action: ")

            if action == '1':
                clear_screen()
                damage = effective_attack
                print(f"You attack {boss_name} for {damage} damage.")
                boss_hp -= damage
            elif action == '2':
                clear_screen()
                if not self.skills:
                    print("You have no skills to use.")
                    continue
                print("Available skills:")
                for i, skill in enumerate(self.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")

                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                skill_name = self.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                print(f"You use {skill_name} for {skill_damage} damage.")
                boss_hp -= skill_damage
            elif action == '3':
                clear_screen()
                print("You flee from the battle.")
                break
            elif action == '4':
                	clear_screen()
                	if self.aura:
                		aura_damage = self.use_aura_skill()
                		monster_hp -= aura_damage
                	else:
                		print("You don't have any aura equipped.")
                		continue
            else:
                print("Invalid choice.")

            # Boss attacks back
            if boss_hp > 0:
            	evade_chance = random.randint(1, 100)
            	if evade_chance <= self.defense:
            		print("You dodged the attack!")
            	else:
            	       boss_skill = random.choice(list(Character.SKILLS.keys()))
            	       boss_damage = Character.SKILLS[boss_skill]
            	       print(f"{boss_name} uses {boss_skill} for {boss_damage} damage.")
            	       self.hp -= boss_damage

            if self.hp <= 0:
                print("You have been defeated by the boss!")
                self.hp = 0
                break

        if boss_hp <= 0:
            print(f"You have defeated the {boss_name}!")
            print("You've received the skill 'Universe!' with damage of 250!")
            self.skills.append("Universe!")
            Character.SKILLS["Universe!"] = 250  # Add skill to the SKILLS dictionary.
            # Add rewards if necessary.

        input("Press Enter to return to menu...")
        
    def fusion_skill(self):
        clear_screen()
        if len(self.skills) < 2:
            print("You need at least 2 skills to fuse.")
            input("Press Enter to return to menu...")
            return

        print("Available Skills to Fuse:")
        print()
        for i, skill in enumerate(self.skills, start=1):
            print(f"{i}. {skill}")
            
        print()
        skill1_index = int(input("Choose the first skill (enter the number): ")) - 1
        skill2_index = int(input("Choose the second skill (enter the number): ")) - 1

        if skill1_index == skill2_index or skill1_index < 0 or skill1_index >= len(self.skills) or skill2_index < 0 or skill2_index >= len(self.skills):
            print("Invalid selection for skills.")
            input("Press Enter to return to menu...")
            return

        skill1 = self.skills[skill1_index]
        skill2 = self.skills[skill2_index]

        # New skill mappings based on combinations
        fusion_mapping = {
            ('Fireball', 'Water'): 'Blueball',
            ('Ice Shield', 'Fireball'): 'Blazing Shield',
            ('Fireball', 'Lightning Strike'): 'Lightning Storm Fire',
            ('Fire Whirlwind','Fire Beam'): 'Firestorm Chaser',
            ('Fireball', 'Charge'): 'Fire Charge',
            ('Dragon Wave', 'Wind Cutter'): 'Dragon Gale',
            ('Thunder Strike', 'Lightning Strike'): 'Electro Strike',
            ('Freezer Smash', 'Ice Shield'): 'Frosty Smash',
            ('Bamboo Throw', 'Arrow Shot'): 'Bamboo Arrow',
            ('Burnout Flame', 'Fire Whirlwind'): 'Inferno Spin',
            ('Gate Breaker', 'Anti Magic'): 'Barrier Break',
            ('Life Drain', 'Dark Magic'): 'Cursed Drain',
            ('Meteor', 'Fire Storm Chaser'): 'Meteoric Fire',
            ('Backstab', 'Quick Slash'): 'Sneak Slash',
            ('Chaos Strike', 'Rage'): 'Chaotic Rage',
            ('Summon Undead', 'Summoning: Zombie Strike'): 'Undead Frenzy',
            ('Ground Smash', 'Titan Smash'): 'Rage Titan Smasher',
            ('Fire Beam', 'Lightning Storm Fire'): 'Storm Beam',
            ('Arcane Blast', 'Heavenly Sword Slash'): 'Arcane Slash',
            ('Poison', 'Shield Bash'): 'Toxic Bash',
            ('Heavenly Demonic Blaster', 'Firestorm Chaser'): 'Demonic Firestorm',
            ('Sky Force', 'Heavenly Sky Kick'): 'Sky Barrage',
            ('Lightning Strike', 'Thunder Strike'): 'Thunderbolt',
            ('Meteor', 'Dragon Wave'): 'Meteoric Wave',
            ('Swing', 'Gate Breaker'): 'Raging Gate',
            ('Dual Blade Slash', 'Heavenly Demonic Blaster'): 'Dual Demonic Slash',
            ('Sky Hammer', 'Ground Smash'): 'Sky Smash',
            ('Fire Whirlwind', 'Burnout Flame'): 'Whirling Inferno',
            ('Step Kick', 'Charge'): 'Kicking Charge',
            ('Earth Storm', 'Gate Breaker'): 'Earthbreaker Storm',
            ('Gravity Stab', 'Grave Stab'): 'Grave Gravity',
            ('Sky Palace', 'Gold Smash'): 'Golden Sky Smash',
        }
        
        new_skill = fusion_mapping.get((skill1,skill2))

        if new_skill:
            if new_skill not in self.skills:
                self.skills.append(new_skill)
                clear_screen()
                print(f"You have successfully fused {skill1} and {skill2} to create {new_skill}!")
            else:
                clear_screen()
                print(f"You already have the skill: {new_skill}.")
        else:
            clear_screen()
            print("This combination does not yield a new skill.")
        print()
        input("Press Enter to return to menu")

    def equip_class(self):
        clear_screen()
        if not hasattr(self, 'purchased_classes') or len(self.purchased_classes) == 0:
            print("You don't have any classes to equip.")
            print()
            input("Press Enter to return to menu")
            return
        print("Purchased classes to equip:")
        print()
        for class_name in self.purchased_classes:
            print(f"- {class_name}")

        print()
        choice = input("Enter the class name to equip: ")
        clear_screen()

        if choice in self.purchased_classes:
            self.class_type = choice
            self.hp = Character.CLASSES[choice]['hp']
            self.attack = Character.CLASSES[choice]['attack']
            self.defense = Character.CLASSES[choice]['defense']

            new_skills = Character.CLASSES[choice]['skills']
            for skill in new_skills:
                if skill not in self.skills:
                    self.skills.append(skill)
            print(f"You have equipped the {choice} class!")
            print()
            input("Press Enter to return to menu")
        else:
            print("Invalid class name.")
            print()
            input("Press Enter to return to menu")

    def gain_rewards(self):
        clear_screen()
        print("Gaining rewards... please wait 5 seconds")
        time.sleep(5)  # Wait for 5 seconds
        clear_screen()

        # Define reward types and their probabilities
        reward_type = random.choices(
            ['Gold', 'Experience', 'Skill', 'Hunter Medals', 'Garuda Feathers', 'Gear', 'Monster Key'],
            weights=[40, 30, 10, 5, 5, 9, 1],
            k=1
        )[0]

        if reward_type == 'Gold':
            reward_amount = random.randint(20, 50)  # Gold range
            self.gold += reward_amount
            print(f"You received {reward_amount} Gold!")
            
        elif reward_type == 'Experience':
            reward_amount = random.randint(20, 50)  # Experience range
            self.experience += reward_amount
            print(f"You gained {reward_amount} Experience!")
            
        elif reward_type == 'Skill':
            skill_name = "Body Movement Strike"
            if skill_name not in self.skills:
                self.skills.append(skill_name)
                Character.SKILLS[skill_name] = 30  # Set damage for the new skill
                print(f"You have received the skill: {skill_name} (Damage: 30)!")
            else:
                print(f"You already have the skill: {skill_name}.")
                
        elif reward_type == 'Hunter Medals':
            medals = random.randint(2, 3)  # Range for Hunter Medals
            self.hunter_medals += medals
            print(f"You received {medals} Hunter Medals!")

        elif reward_type == 'Garuda Feathers':
            feathers = random.randint(4, 5)  # Range for Garuda Feathers
            self.garuda_feathers += feathers
            print(f"You received {feathers} Garuda Feathers!")

        elif reward_type == 'Gear':
            gear_name = "Gaining Amulet"
            if gear_name not in self.gear:
                self.gear.append(gear_name)
                print(f"You received the gear: {gear_name} (Damage: 20, HP: 10, Mana: 0)!")
            else:
                print(f"You already have the gear: {gear_name}.")

        elif reward_type == 'Monster Key':
            self.monster_keys += 1
            print("You received 1 Monster Key!")

        print()  # Add extra space
        input("Press Enter to return to menu")

    def market(self):
        if self.level < 10:
            clear_screen()
            print("You need to be level 10 to unlock the market.")
            print()
            input("Press Enter to return to menu")
            return

        clear_screen()
        print("==============================")
        print("   Welcome to the Market")
        print("==============================")

        for category, items in Character.MARKET_ITEMS.items():
            print()
            print("Note : 20 Gold to invest!")
            print()
            print("==============================")
            print(f"\n{category}:")
            for item, price in items.items():
                print(f"- {item}: {price} Gold")

        print()
        print("==============================")
        print()
        choice = input("Enter the item name to buy or type 'exit' to leave: ").strip()

        # Check if the choice is valid
        bought = False
        for category, items in Character.MARKET_ITEMS.items():
            if choice in items:
                if self.gold >= items[choice]:
                    self.gold -= items[choice]

                    if category == 'Skills':
                        clear_screen()
                        if choice not in self.skills:
                            self.skills.append(choice)
                            self.skills_dict[choice] = 1
                            print(f"You have received the skill: {choice}!")
                        else:
                            print("You already have this skill.")
                    elif category == 'Materials':
                        clear_screen()
                        self.inventory.append(f"{choice} Material")
                        print(f"You have received {choice} material.")
                    elif category == 'Classes':
                        clear_screen()
                        if choice not in Character.CLASSES:
                            print("Invalid class purchase.")
                        else:
                            if hasattr(self, 'purchased_classes'):
                                self.purchased_classes.append(choice)
                            else:
                                self.purchased_classes = [choice]
                            print(f"You have purchased the class: {choice}!")

                    elif category == 'Gold':
                        clear_screen()
                        additional_gold = int(choice.split()[0])
                        self.gold += additional_gold
                        print(f"You have received {additional_gold} gold.")
                    bought = True
                else:
                    clear_screen()
                    print("You don't have enough gold.")
                break

        if not bought:
            print()
            print(f"Your Gold : {self.gold}")

        print()
        input("Press Enter to return to menu")

    def exchange(self):
        clear_screen()
        if self.level < 5:
            print("You need to reach level 5 to unlock exchange (sell your items).")
            print()
            input("Press Enter to return to menu...")
            return

        print("Available Exchange: ")
        print()
        print("1. Exchange a Material for rewards")
        print("2. Exchange a Skill for rewards")
        print()

        choice = input("Choose an exchange (enter the number): ")

        if choice == '1':
            self.exchange_material()
        elif choice == '2':
            self.exchange_skill()
        else:
            clear_screen()
            print("Invalid commands.")
            print()
            input("Press Enter to return to menu...")

    def exchange_material(self):
        clear_screen()
        materials = [item for item in self.inventory if item.endswith('Material')]
        if not materials:
            print("You don't have any materials to exchange.")
            print()
            input("Press Enter to return to menu")
            return

        print("Available materials to exchange:")
        for i, material in enumerate(materials, start=1):
            print(f"{i}. {material}")

        choice = int(input("Choose a material to exchange (enter the number): ")) - 1
        selected_material = materials[choice]
        self.inventory.remove(selected_material)

        # Exchange Rewards
        gold_reward = random.randint(100, 500)
        experience_reward = random.randint(50, 200)

        self.gold += gold_reward
        self.experience += experience_reward
        print()
        clear_screen()

        print(f"Exchange successful! You received:")
        print(f"- Gold: {gold_reward}")
        print(f"- Experience: {experience_reward}")
        print()

        input("Press Enter to return to menu...")

    def exchange_skill(self):
        clear_screen()
        if not self.skills:
            print("You don't have any skills to exchange.")
            input("Press Enter to return to menu...")
            return

        print("Available skills to exchange:")
        print()
        for i, skill in enumerate(self.skills, start=1):
            print(f"{i}. {skill}")

        print()
        choice = int(input("Choose a skill to exchange (enter the number): ")) - 1
        selected_skill = self.skills[choice]
        self.skills.remove(selected_skill)

        # Exchange Rewards
        gold_reward = random.randint(100, 500)
        experience_reward = random.randint(50, 200)

        self.gold += gold_reward
        self.experience += experience_reward
        print()
        clear_screen()

        print(f"Exchange successful! You received:")
        print(f"- Gold: {gold_reward}")
        print(f"- Experience: {experience_reward}")
        print()

        input("Press Enter to return to menu...")

    def buy_monster_keys(self):
        clear_screen()
        cost_per_key = 3500
        print(f"Each Monster Key costs {cost_per_key} gold.")
        print()
        print(f"Your Gold: {self.gold}")
        print()
        keys_to_buy = int(input(f"How many Monster Keys would you like to buy? : "))

        total_cost = keys_to_buy * cost_per_key
        if total_cost > self.gold:
            clear_screen()
            print("You do not have enough gold to buy Monster Keys.")
            print()
            input("Press to Back")
        else:
            self.gold -= total_cost
            self.monster_keys += keys_to_buy
            clear_screen()
            print(f"You have successfully bought {keys_to_buy} Monster Keys.")
            print()
            input("Press Enter to return to menu...")

    def heal(self):
    	clear_screen()
    	
    	if self.hp >= self.max_hp:
    	   print("HP sudah penuh.")
    	   input("Tekan Enter untuk kembali ke menu...")
    	   return
    	   
    	heal_amount = 25
    	self.hp = min(self.max_hp, self.hp + heal_amount)
    	print(f"Recover {heal_amount} HP. Sekarang HP Anda: {self.hp}/{self.max_hp}.")
    	input("Tekan Enter untuk kembali")



    def level_up(self):
        required_exp = 400  # EXP yang dibutuhkan untuk level up
        if self.experience < required_exp:
            clear_screen()
            print("Experience mu kurang. Diperlukan 400 EXP untuk naik level!")
            print()
            input("Press Enter to return menu")
            return

        self.experience -= required_exp
        self.level += 1
        self.hp += min(self.max_hp, self.hp + 5)
        clear_screen()
        print(f"{self.name} naik level ke {self.level}!")
        print()
        input("Tekan Enter untuk melanjutkan...")

    def show_profile(self):
        clear_screen()
        
        effective_attack = self.attack + (self.aura.skill_damage if self.aura else 0)
        effective_hp = self.hp + (self.aura.hp if self.aura else 0)
        effective_defense = self.defense
        
        total_attack = self.attack
        effective_attack = total_attack
        total_attack = effective_attack
        effective_defense = self.defense
        total_heal = self.hp
        total_heal = effective_hp
        total_hp = self.max_hp
        total_damage = 0
        
        for gear in self.gear:
        	stats = Character.GEARS.get(gear, {})
        	total_attack += stats.get('damage', 0)
        	total_hp += stats.get('hp', 0)
        	self.mana = stats.get('mana', 0)
        	
        effective_hp = self.hp if self.hp < total_hp else total_hp

        print(f"Name: {self.name}")
        print(f"Class: {self.class_type if self.class_type else 'None'}")
        print(f"Level: {self.level}")
        print(f"HP: {total_heal}/{total_hp}")
        print(f"Attack: {total_attack} ( its must +5 use with aura, but maybe bug. so dont worry! )")
        print(f"Defense: {effective_defense}")
        print(f"Experience: {self.experience}")
        print(f"Gold: {self.gold}")
        print("Skills:", ", ".join(self.skills) if self.skills else "None")
        print(f"Aura: {self.aura.name if self.aura else 'None'}")
        print(f"Passive Aura: {self.aura.passive_effect if self.aura else 'None'}")
        print("Gear:")
        for gear in self.gear:
            stats = Character.GEARS[gear]
            print(f"- {gear} (HP: {stats['hp']}, Mana: {stats['mana']}, Damage: {stats['damage']})")
        print()
        input("Press Enter to return to menu...")

    def show_gear(self):
        clear_screen()
        print("Gear equipped:")
        print()
        if not self.gear:
            print("No gear equipped.")
        else:
            for item in self.gear:
            	stats = Character.GEARS[item]
            	print(f"- {item} (HP: {stats['hp']}, Mana: {stats['mana']}, Damage: {stats['damage']})")
            	
        print()
        input("Press Enter to return to menu,")

    def show_inventory(self):
        clear_screen()
        print(f"Your Gacha Keys : {self.monster_keys}")
        print(f"Your Gold : {self.gold}")
        print(f"Hunter Medals : {self.hunter_medals}")
        print(f"Garuda Feathers : {self.garuda_feathers}")
        print(f"Scratch Coins : {self.scratch_coins}")
        print()
        input("Press Enter to return to menu")

    def show_skills(self):
        clear_screen()
        print("Skills:")
        print()
        for skill in self.skills:
            if skill in Character.SKILLS:
                print(f"- {skill} (Damage: {Character.SKILLS.get(skill, 'N/A')})")
            elif skill in Character.GOD_POWERS:
                print(f"- {skill} (Damage: {Character.GOD_POWERS[skill]['damage']})")
            else:
                print(f"- {skill} (Damage: {Character.SKILLS.get(skill, 'N/A')})")
        print()
        input("Press Enter to return to menu...")

    def use_gacha(self):
        clear_screen()
        if self.monster_keys <= 0:
            print(f"Your Keys: {self.monster_keys}")
            print()
            print("You don't have any Monster Keys. You can buy keys or hunting on monsters!")
            print()
            input("Press Enter to return to menu")
            return

        self.monster_keys -= 1
        base_gacha_rate = 0.1  # Base gacha rate of 10%
        # Apply the aura effect
        if self.aura and self.aura.passive_effect == "Increases gacha and battle success rate by 2%":
            gacha_rate = base_gacha_rate * (1 + 0.02)  # 2% increase
        else:
            gacha_rate = base_gacha_rate
        result = random.choices(['Gear', 'Material', 'Skill', 'God Power'], weights=[0.3 * (gacha_rate), 0.6 * (gacha_rate), 0.1 * (gacha_rate), 0.1 * (gacha_rate)])[0]

        if result == 'Gear':
            new_gear = random.choice(list(Character.GEARS.keys()))
            if len(self.gear) < 1000:
                if new_gear in self.gear:
                    self.gear_dict[new_gear] += 1
                else:
                    self.gear.append(new_gear)
                    self.gear_dict[new_gear] = 1

                gear_stats = Character.GEARS[new_gear]
                self.attack += gear_stats['damage']
                self.max_hp += gear_stats['hp']
                self.hp = min(self.hp + gear_stats['hp'], self.max_hp)
            else:
                print("You have reached the maximum capacity for gear.")

        elif result == 'Material':
            new_material = random.choice(Character.MATERIALS)
            self.inventory.append(f"{new_material} Material")
        elif result == 'Skill':
            new_skill = random.choice(list(Character.SKILLS.keys()))
            if len(self.skills) < 1000:
                if new_skill not in self.skills:
                    self.skills.append(new_skill)
                    self.skills_dict[new_skill] = 1
                else:
                    print("You already have this skill.")
            else:
                print("You have reached the maximum capacity for skills.")

        elif result == 'God Power':
            new_god_power = random.choice(list(Character.GOD_POWERS.keys()))
            if new_god_power not in self.skills:
                if len(self.skills) < 1000:
                    self.skills.append(new_god_power)
                    print(f"You have received the God Power: {new_god_power}!")
                else:
                    print("You have reached the maximum number of skills.")

        print(f"Received: {result}")
        input("Press Enter to return to menu...")

    def craft_gear(self):
        clear_screen()
        if not any(item.endswith('Material') for item in self.inventory):
            print("You don't have any materials to craft gear.")
            input("Press Enter to return to menu...")
            return

        print("Available materials:")
        materials = [item for item in self.inventory if item.endswith('Material')]
        for i, material in enumerate(materials, start=1):
            print(f"{i}. {material}")

        choice = int(input("Choose a material to use (enter the number): ")) - 1
        selected_material = materials[choice]
        material_name = selected_material.replace(" Material", "")

        # Define gear attributes
        hp = random.randint(5, 20)
        mana = random.randint(0, 15)
        damage = random.randint(5, 30)

        # Create new gear item
        new_gear_name = f"Crafted {material_name} Gear"
        new_gear = {'damage': damage, 'hp': hp, 'mana': mana}

        # Add the gear to the character's gear
        if len(self.gear) < 5:
            if new_gear_name in self.gear:
                self.gear_dict[new_gear_name] += 1
            else:
                self.gear.append(new_gear_name)
                self.gear_dict[new_gear_name] = 1
            print(f"Crafted new gear: {new_gear_name} - HP: {hp}, Mana: {mana}, Damage: {damage}")

            # Add a chance to receive a skill with the new gear
            if random.random() < 0.02:
                new_skill = random.choice(list(Character.SKILLS.keys()))
                if len(self.skills) < 5:
                    if new_skill not in self.skills:
                        self.skills.append(new_skill)
                        self.skills_dict[new_skill] = 1
                        print(f"You also received a new skill: {new_skill}!")
        else:
            print("You have reached the maximum capacity for gear.")

        # Remove used material from inventory
        self.inventory.remove(selected_material)
        input("Press Enter to return to menu...")

    def redeem_code(self):
        clear_screen()
        code = input("Enter your redeem code: ").strip()

        # Validate the redeem code format
        if not re.match(r'^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$', code):
            print("Invalid redeem code format.")
            input("Press Enter to return to menu...")
            return

        reward = Character.REDEEM_CODES.get(code)
        if reward:
            reward_type, reward_value = reward
            if reward_type == 'skill':
                if reward_value not in self.skills:
                    if len(self.skills) < 5:
                        self.skills.append(reward_value)
                        print(f"You have received the skill: {reward_value}!")
                    else:
                        print("You have reached the maximum number of skills.")
                else:
                    print(f"You already have the skill: {reward_value}.")
            # Handle other reward types...
            print(f"Redeemed: {reward_value}")
        else:
            print("Invalid redeem code.")
        input("Press Enter to return to menu...")

    def battle_monster(self):
        clear_screen()
        print("Available monsters to fight:")
        for i, (monster_name, details) in enumerate(self.monsters.items(), start=1):
            print(f"{i}. {monster_name} (HP: {details['hp']})")

        print()
        choice = int(input("Choose a monster to fight (enter the number): ")) - 1
        monster_name = list(self.monsters.keys())[choice]
        monster = self.monsters[monster_name]
        monster_hp = monster['hp']

        clear_screen()
        print(f"BOSS : {monster_name}")
        while monster_hp > 0 and self.hp > 0:
            # Get effective attack considering aura
            effective_attack = self.attack + (self.aura.attack_bonus if self.aura else 0)
            for gear in self.gear:
            	stats = Character.GEARS.get(gear, {})
            	effective_attack += stats.get('damage', 0)
            print(f"\nYour HP: {self.hp}")
            print(f"{monster_name}'s HP: {monster_hp}")
            print()
            print("1. Attack")
            print("2. Use Skill")
            print("3. Flee")
            print("4. Use Aura Skill")
            print()
            action = input("Choose your action: ")

            if action == '1':
                clear_screen()
                damage = self.attack
                print(f"You attack {monster_name} for {damage} damage.")
                monster_hp -= effective_attack
            elif action == '2':
                clear_screen()
                if not self.skills:
                    print("You have no skills to use.")
                    continue
                print("Available skills:")
                for i, skill in enumerate(self.skills, start=1):
                    print(f"{i}. {skill} (Damage: {Character.SKILLS[skill]})")

                skill_choice = int(input("Choose a skill to use (enter the number): ")) - 1
                clear_screen()
                skill_name = self.skills[skill_choice]
                skill_damage = Character.SKILLS.get(skill_name, 0)
                print(f"You use {skill_name} for {skill_damage} damage.")
                monster_hp -= skill_damage
            elif action == '3':
                clear_screen()
                print("You flee from the battle.")
                break
            elif action == '4':
            	clear_screen()
            	if self.aura:
            	   aura_damage = self.use_aura_skill()
            	   monster_hp -= aura_damage
            	else:
            	   print("You don't have any aura equipped.")
            	   continue
            else:
                print("Invalid choice.")

            if monster_hp > 0:
            	evade_chance = random.randint(1, 100)
            	if evade_chance <= self.defense:
            	   print("You dodged the attack!")
            	else:
            	   monster_attack = monster['skills'].get('Bite', 5)
            	   print(f"{monster_name} attacks you for {monster_attack} damage.")
            	   self.hp -= monster_attack

            if self.hp <= 0:
                print("You have been defeated!")
                self.hp = 0
                break

        if monster_hp <= 0:
            print(f"You have defeated the {monster_name}!")
            # Add experience reward
            experience_reward = random.randint(20, 100)  # Example experience range
            self.experience += experience_reward
            print(f"You gained {experience_reward} experience!")
            reward = random.randint(10, 50)
            self.gold += reward
            if random.random() < 0.03:  # 3% chance to drop a monster key
                self.monster_keys += 1
                print("You found a Monster Key!")
            print(f"You received {reward} gold.")
        input("Press Enter to return to menu...")

    def repeat_battle(self):
        clear_screen()
        if self.gold < 10:
            print("You don't have enough gold to repeat the battle.")
            input("Press Enter to return to menu...")
            return

        self.gold -= 10
        monster_name, monster = random.choice(list(self.monsters.items()))
        monster_hp = monster['hp']

        print(f"Auto-battle against {monster_name}...")
        while monster_hp > 0 and self.hp > 0:
            damage = self.attack
            monster_hp -= damage

            if monster_hp > 0:
                monster_attack = monster['skills'].get('Bite', 5)
                self.hp -= monster_attack

        if monster_hp <= 0:
            print(f"You have defeated the {monster_name}!")
            # Add experience reward
            experience_reward = random.randint(20, 100)  # Example experience range
            self.experience += experience_reward
            print(f"You gained {experience_reward} experience!")
            reward = random.randint(10, 50)
            self.gold += reward
            if random.random() < 0.01:  # 1% chance to drop a monster key
                self.monster_keys += 1
                print("You found a Monster Key!")
            print(f"You received {reward} gold.")
        elif self.hp <= 0:
            print("You have been defeated in the auto-battle!")
            self.hp = 0
        input("Press Enter to return to menu...")

def load_character():
    if os.path.exists('your_account.pkl'):
        with open('your_account.pkl', 'rb') as f:
            character = pickle.load(f)
            if not hasattr(character, 'garuda_feathers'):
                character.garuda_feathers = 0
            if not hasattr(character, 'last_claim_time'):
                character.last_claim_time = None
            if not hasattr(character, 'scratch_coins'):  # Add this line
                character.scratch_coins = 0  # Initialize it
            return character
    return None

def main():
    clear_screen()
    saved_character = load_character()
    if saved_character:
        print("Previous save found. Loading...")
        character = saved_character
    else:
        name = input("Enter your character's name: ")
        character = Character(name)
        
    travel = Travel(character)  # Initialize Travel class
    daily_login = DailyLogin(character) # Initialize Daily Login class

    while True:
        clear_screen()
        print("1. Show Profile")
        print("2. Show Gear")
        print("3. Show Inventory")
        print("4. Show Skills")
        print("5. Use Gacha")
        print("6. Fight Monster")
        print("7. Repeat Battle")
        print("8. Save and Exit or just typing 'exit'")
        print("9. Redeem Code")
        print("10. Craft Gear")
        print("11. Announcements")
        print("12. Report Bugs")
        print("13. Heal")
        print("14. Level UP")
        print("15. Buy Monster Keys")
        print("16. Exchange")
        print("17. Market")
        print("18. Gain Rewards (AFK)")
        print("19. Equip Class")
        print("20. Fusion Skill")
        print("21. Bosses")
        print("22. Packages")
        print("23. PVP (Bot)")
        print("24. Arena")
        print("25. Guild")
        print("26. Travel")
        print("27. Stats Shop")
        print("28. Hunter Festival (Event)")
        print("29. Upgrade Skill")
        print("30. Treasure Hunt")
        print("31. Aura Shop")
        print("32. Garuda War (Event)")
        print("33. Daily Login")
        print("34. The Scratch")
        print("35. Daily Gacha")
        print("36. God Challenger")
        print()
        choice = input("Choose an option: ")

        if choice == '1':
            character.show_profile()
        elif choice == '2':
            character.show_gear()
        elif choice == '3':
            character.show_inventory()
        elif choice == '4':
            character.show_skills()
        elif choice == '5':
            character.use_gacha()
        elif choice == '6':
            character.battle_monster()
        elif choice == '7':
            character.repeat_battle()
        elif choice == '8' or choice == 'exit':
            with open('your_account.pkl', 'wb') as f:
                pickle.dump(character, f)
                print()
            clear_screen()
            print("Game saved... ")
            print()
            input("Press to Enter to return menu")
            continue
        elif choice == '9':
            character.redeem_code()
        elif choice == '10':
            character.craft_gear()
        elif choice == '11':
            announcements()
        elif choice == '12':
            report_bugs()
        elif choice == '13':
            character.heal()
        elif choice == '14':
            character.level_up()
        elif choice == '15':
            character.buy_monster_keys()
        elif choice == '16':
            character.exchange()
        elif choice == '17':
            character.market()
        elif choice == '18':  # Call gain_rewards method when option 18 is chosen
            character.gain_rewards()
        elif choice == '19':
            character.equip_class()
        elif choice == '20':
        	character.fusion_skill()
        elif choice == '21':  # Panggil metode battle_boss saat opsi 21 dipilih
            character.battle_boss()
        elif choice == '22':  # Panggil metode open_package saat opsi 22 dipilih
            character.open_package()
        elif choice == '23':  # Call pvp_battle when option 23 is selected
            character.pvp_battle()
        elif choice == '24':  # Call arena method when option 24 is selected
            character.arena()
        elif choice == '25':  # Add guild option
            if hasattr(character, 'guild'):
                clear_screen()
                # If already in a guild, show options
                print("You are currently in a guild.")
                print()
                print("1. View Guild Profile")
                print("2. Battle Guardian")
                print("3. Leave Guild")
                print("4. Guild Announcements")
                print()
                guild_option = input("Choose an option: ")
                if guild_option == '1':
                    character.guild.show_profile()
                elif guild_option == '2':
                    character.guild.guild_battle()
                elif guild_option == '3':
                    character.leave_guild()
                elif guild_option == '4':
                	character.announcements_guild()
            else:
                character.create_guild()
        elif choice == '26':
            if character.gold < 0:
                clear_screen()
                print()
            else:
                character.gold -= 0
                travel.travel_menu()  # Call the travel method
        elif choice == '27':
        	character.buy_stats()
        elif choice == '28':
        	festival = HunterFestival(character)
        	festival.hunter_festival_menu()
        elif choice == '29':
        	character.upgrade_skill()
        elif choice == '30':  # New option for Treasure Hunt
            character.treasure_hunt()
        elif choice == '31':
            character.aura_shop()
        elif choice == '32':
        	garuda_war = GarudaWar(character)
        	garuda_war.garuda_war_menu()
        elif choice == '33':
            daily_login.daily_login_menu()  # Call Daily Login Menu
        elif choice == '34':
            scratch_game = TheScratch(character)
            scratch_game.scratch_menu()
        elif choice == '35':  # Call daily_gacha when option 35 is selected
            character.daily_gacha()
        elif choice == '36':
            character.god_challenger()
        else:
            print()
            input("Invalid Commands!")
            continue

if __name__ == "__main__":
    main()
