
import os
import time
import random

# 1. Identity Check
name = input("⚡ Identify yourself, Universe-Hopper: ").strip()

if name: 
    print(f"\nWelcome, Agent {name}. Syncing reality parameters...")
    time.sleep(1.2)
    
    passkey_id = int(input("🔐 Generate your Multiverse Passkey Number: "))
    print("🔒 Passkey registered. Cosmic coordinates unlocked.\n")
    time.sleep(1.0)
    
    # Main Interface
    print("🌌 =========================================== 🌌")
    print("       --- MULTIVERSE PORTAL INTERFACE ---       ")
    print("🌌 =========================================== 🌌")
    print("1. Go to Earth 616")
    print("2. Enter the Hellverse [⚠️ CRITICAL CELESTIAL THREAT]")
    print("3. Return to Normal World")
    print("4. End this Multiverse")
    print("=================================================")
    
    world_choice = input("Select destination coordinates (1-4): ").strip()
    
    if world_choice == "1":
        os.system('color 9')  # Light Blue sky theme
        print(f"\n🚀 Portal stabilized! Welcome to Earth 616, {name}. Watch the skies for the Avengers.")

    # ---------------------------------------------------------------------
    # DESTINATION 2: THE HELLVERSE VS HELIS
    # ---------------------------------------------------------------------
    elif world_choice == "2":
        os.system('color 4')  # Red alert warning theme
        print("\n🚨 WARNING: STELLAR MASS CONCENTRATION DETECTED AHEAD.")
        time.sleep(1.5)
        
        # Hacker Loading Bar sequence
        print("\n[░░░░░░░░░░] 0% Ripping fabric of space-time...", end="\r")
        time.sleep(0.6)
        print("[████░░░░░░] 40% Resisting gravitational pull...", end="\r")
        time.sleep(0.8)
        print("[████████░░] 80% Shielding biological vitals...", end="\r")
        time.sleep(0.5)
        print("[██████████] 100% DISPATCH COMPLETE. BRACE FOR IMPACT.", end="\r")
        time.sleep(1.5)
        
        os.system('cls') # Clear screen for the grand arrival
        
        # Giant ASCII Portal Graphics Drop
        print("""
        .     .       .  .   .       .     .       .
         \\   /       /    \\   \\     /     /       / 
          \\ /       /      \\   \\   /     /       /  
        ---X-------X--------X---X-X-----X-------X---
          / \\       \\      /   /   \\     \\       \\  
         /   \\       \\    /   /     \\     \\       \\ 
        .     .       .  .   .       .     .       .
        """)
        print("=====================================================")
        print(f"Agent {name} has breached the barrier of the Hellverse.")
        print("=====================================================\n")
        time.sleep(2.0)
        
        print("🌌 The fabric of space twists... Before you stands 🔥 HELIS 🔥!")
        print("Its face is a swirling dark black hole, and its eyes glare with intense neutron star energy.")
        print("Your combat suit powers up, initializing your heavy weapons systems...")
        time.sleep(3.0)
        
        # Combat setup
        player_hp = 100
        boss_hp = 150  # Helis has extra cosmic health!
        
        while player_hp > 0 and boss_hp > 0:
            print(f"\n📊 STATUS: [Agent {name}: {player_hp} HP]  |  [HELIS: {boss_hp} HP]")
            print("-----------------------------------------------------")
            print("1. Fire Iron Man Union Beam ⚡ (High critical potential)")
            print("2. Deploy Custom Missile Punch Blaster 🥊🚀 (Heavy impact damage)")
            print("3. Spray Electric Ice Glue ❄️🧪 (Deals damage + minor tactical heal)")
            print("4. Retreat through the dimensional rift 🏃‍♂️")
            
            action = input("\nSelect your weapon matrix option (1-4): ").strip()
            
            if action == "1":
                # High risk, high reward spread
                damage = random.randint(15, 50)
                boss_hp -= damage
                print(f"\n⚡ UNLEASHED! Your chest core fires a massive Union Beam! You burn HELIS for {damage} cosmic damage!")
                time.sleep(1.0)
                
            elif action == "2":
                # High steady punch damage
                damage = random.randint(25, 35)
                boss_hp -= damage
                print(f"\n🚀 BOOM! Your mechanical gauntlet launches rocket-fists! You punch HELIS for {damage} heavy kinetic damage!")
                time.sleep(1.0)
                
            elif action == "3":
                # Minor damage + freeze logic gives self heal
                damage = random.randint(10, 20)
                heal = random.randint(10, 15)
                boss_hp -= damage
                player_hp += heal
                if player_hp > 100:
                    player_hp = 100
                print(f"\n❄️ GLUED! Electrified Ice pins the black hole face! HELIS takes {damage} damage, and your suit diagnostics restore {heal} HP!")
                time.sleep(1.0)
                
            elif action == "4":
                print("\n🏃‍♂️ Rift destabilized! You execute an emergency backwards jump out of the system!")
                break
            else:
                print("\n❌ System override error! You stumbled over your suit controls and missed a turn!")
                time.sleep(1.0)
            
            # Helis counters if still breathing
            if boss_hp > 0 and action in ["1", "2", "3", ""]:
                boss_attack = random.randint(15, 30)
                player_hp -= boss_attack
                print(f"🌌 HELIS distorts gravity! A gamma-ray burst from its neutron eyes burns you for {boss_attack} HP!")
                time.sleep(1.5)
        
        # Victory conditions
        if boss_hp <= 0:
            os.system('color A') # Flash victorious matrix green color!
            print(f"\n🏆 UNIVERSE SAVED! Agent {name} collapsed the black hole! HELIS has been completely evaporated!")
        elif player_hp <= 0:
            print(f"\n💀 SPAGHETTIFIED. Agent {name} was crushed by the absolute gravitational pull of HELIS. Game Over.")

    elif world_choice == "3":
        print(f"\n🏡 Reality sync complete. Sending {name} safely home to drink warm coffee.")

    elif world_choice == "4":
        os.system('color 4')
        print("\n💥 SYSTEM CRITICAL: TERMINATION OF TIMELINES INITIALIZED.")
        time.sleep(1.0)
        os.system('cls')
        exit()
        
    else:
        print("\n❌ Invalid coordinates! Your atoms scatter across the void.")

else:
    print("Access Denied. Anonymous entities are expelled X_X")
"""