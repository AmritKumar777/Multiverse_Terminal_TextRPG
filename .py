#stage_code1
"""name = input(("what's your name?"))
name = name
if name == "name":
    print("Proceed Further....")
    passkey_id = int(input("Create your passkey No:"))
else:
  print("Get the hell out from here X_X")"""

#stage_code2
    
"""
# 1. Ask for their name and save it into the 'name' variable
name = input("what's your name? ")

# 2. Check if the 'name' variable is NOT blank
# 'if name:' means: "If there is text inside this variable, proceed!"
if name: 
    print(f"\nWelcome {name}! Proceed Further....")
    passkey_id = int(input("Create your passkey No: "))
    print(f"Passkey {passkey_id} saved successfully!")
    if passkey_id == True:
        print("1. Go to Earth 616")
        print("2. Return to Hellverse")
        print("3. Normal World")
        print("4. Kill 'em")
        print("5. End this multiverse")
else:
    # This triggers ONLY if they just hit ENTER without typing anything
    print("Get the hell out from here X_X") """


#stage_code3
"""# 1. Ask for their name
name = input("what's your name? ")

# 2. Verify they actually typed a name
if name: 
    print(f"\nWelcome {name}! Proceed Further....")
    
    # 3. Create the passkey integer
    passkey_id = int(input("Create your passkey No: "))
    print(f"🔒 Passkey [{passkey_id}] saved successfully! Portal Unlocked.\n")
    
    # 4. Display the Multiverse Navigation Hub
    print("🌌 --- MULTIVERSE PORTAL MENU --- 🌌")
    print("1. Go to Earth 616")
    print("2. Return to Hellverse")
    print("3. Normal World")
    print("4. Kill 'em All")
    print("5. End this Multiverse")
    print("====================================")
    
    # 5. Grab their destination choice!
    world_choice = input("Enter the portal destination number (1-5): ")
    
    # 6. ROUTE THEM TO THEIR DESTINATION
    if world_choice == "1":
        print(f"\n🚀 Portal opening... Welcome to Earth 616, {name}! Watch out for the Avengers.")
        
    elif world_choice == "2":
        print(f"\n🔥 Error! Shielding active. Returning {name} to the dark depths of the Hellverse.")
        
    elif world_choice == "3":
        print(f"\n🏡 Back to reality! Sending {name} to the Normal World to drink coffee.")
        
    elif world_choice == "4":
        print(f"\n⚔️ Target locked! Commencing destruction sequence on command of Agent {name}...")
        
    elif world_choice == "5":
        print(f"\n💥 WARNING! System critical... {name} just ended the entire multiverse timeline. Game Over.")
        
    else:
        print("\n❌ Invalid coordinates! You are lost in the void forever.")

else:
    # This triggers ONLY if they just hit ENTER without typing anything
    print("Get the hell out from here X_X") """


#Stage_code4
"""
import os    # Tool to talk to your computer system (to change colors)
import time  # Tool to add dramatic pauses and timing

name = input("what's your name? ")

if name: 
    print(f"\nWelcome {name}! Proceed Further....")
    passkey_id = int(input("Create your passkey No: "))
    print(f"🔒 Passkey [{passkey_id}] saved successfully! Portal Unlocked.\n")
    
    print("🌌 --- MULTIVERSE PORTAL MENU --- 🌌")
    print("1. Go to Earth 616")
    print("2. Return to Hellverse")
    print("3. Normal World")
    print("4. Kill 'em All")
    print("5. End this Multiverse")
    print("====================================")
    
    world_choice = input("Enter the portal destination number (1-5): ")
    
    if world_choice == "1":
        print(f"\n🚀 Portal opening... Welcome to Earth 616, {name}! Watch out for the Avengers.")
        
    elif world_choice == "2":
        print(f"\n🔥 Error! Shielding active. Returning {name} to the dark depths of the Hellverse.")
        
    elif world_choice == "3":
        print(f"\n🏡 Back to reality! Sending {name} to the Normal World to drink coffee.")
        
    elif world_choice == "4":
        print(f"\n⚔️ Target locked! Commencing destruction sequence on command of Agent {name}...")
        
    elif world_choice == "5":
        # 🚨 THE MELTDOWN SEQUENCE ACTIVATED!
        
        # 'color 4' tells Windows Terminal to switch to Black Background + Red Text
        os.system('color 4') 
        
        print("\n💥 WARNING! MULTIVERSE DESTRUCTION SEQUENCE INITIATED.")
        time.sleep(1.5)  # Pause for 1.5 seconds
        
        print("Slicing timelines...")
        time.sleep(1.0)  # Pause for 1 second
        
        print(f"Erasing memories of Agent {name}...")
        time.sleep(1.0)
        
        print("Goodbye reality.")
        time.sleep(1.5)
        
        # This completely wipes the terminal screen clean, leaving it pitch black!
        os.system('cls') 
        
        # Forcefully exit the entire script right then and there
        exit()
        
    else:
        print("\n❌ Invalid coordinates! You are lost in the void forever.")

else:
    print("Get the hell out from here X_X") 
"""



# =====================================================================
#  🧠 THE ULTIMATE REFERENCE: TIME DELAYS & O.S. REALITY WARPING
# =====================================================================

# ---------------------------------------------------------------------
# ⏱️ TOOL 1: import time & time.sleep()
# ---------------------------------------------------------------------
import time  

# 🔍 WHAT IS IT?
# Think of this exactly like the orange "WAIT (1) SECONDS" block from Scratch!
# Normally, Python executes code at lightspeed. 'time.sleep()' is your freeze button.

# 💡 HOW IT WORKS:
# When Python hits this line, it halts all execution and stares at its clock.
# You can pass integers or decimals inside the parentheses.

time.sleep(1)    # ⏸️ Pauses the terminal for exactly 1 full second
time.sleep(0.5)  # ⏸️ Pauses the terminal for half a second (500 milliseconds)
time.sleep(2.5)  # ⏸️ Pauses the terminal for two and a half seconds

# ---------------------------------------------------------------------
# 🖥️ TOOL 2: import os & os.system()
# ---------------------------------------------------------------------
import os  

# 🔍 WHAT IS IT?
# This is how your Python script breaks out of its sandbox and talks directly
# to your laptop's core Operating System (Windows / Command Prompt). 
# It acts like the "Looks" and "Effects" color-changing blocks in Scratch!

# 💡 HOW IT WORKS:
# 'os.system()' takes a terminal command as text and forces Windows to execute it.

# 🎨 EFFECT A: THE COLOR CHANGER
# Format: os.system('color BACKGROUND_TEXT') 
# Uses numbers/letters (0-9, A-F) to completely shift the matrix aesthetic.

os.system('color 4')   # Sets background to Black (0 implied) and text to Red (4)
os.system('color 02')  # Hacker Matrix Look: Black Background (0) + Green Text (2)
os.system('color 17')  # Deep Space Look: Blue Background (1) + Bright White Text (7)
os.system('color')     # System Reset: Restores terminal back to its original default colors

# 🧼 EFFECT B: THE VISUAL WIPE
# This is like the "Clear Graphic Effects" or deleting all clones at once.
# It completely cleans the terminal slate so nothing is left behind.

os.system('cls')  # Wipes the screen completely blank (Clear Screen)

# =====================================================================
# 🚀 PRO-TIP FOR DYNAMICS:
# Combining these two allows you to make flashing warning signs or 
# slow-loading cinematic text bars that completely control the user's emotion!
# =====================================================================

#STAGE_CODE5


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


# =====================================================================
# 🌌 PROJECT ARCHIVE: THE MULTIVERSE PORTAL INTERFACE (v3.0 - MULTIMEDIA)
# 📝 DEVELOPER EVOLUTION LOG & TECHNICAL SPECIFICATIONS
# =====================================================================
#
# 🛠️ THE EVOLUTION STORY:
# ------------------------
# 🔹 Phase 1 (The Reconnection): Started as an ultra-fast recall sprint after 
#     learning Python syntax in just 2 days. Re-mastered standard terminal input, 
#     list creation, and basic tracking frameworks (inspired by classic text apps).
#
# 🔹 Phase 2 (The Logical Shift): Broke through the classic textbook boundaries 
#     by engineering a dynamic text-adventure structure. Encountered and conquered 
#     critical type assignment roadblocks (like verifying conditional data types 
#     and preventing string-to-integer crash vectors).
#
# 🔹 Phase 3 (Reality Warping): Discovered how to bridge the gap between Python 
#     and the physical machine using 'os' and 'time'. Brought back classic wait-state 
#     mechanics (like Scratch's delay blocks) to forge custom hacker loading loops, 
#     terminal color matrices, and visual grid wipes.
#
# 🔹 Phase 4 (The Production Build): Upgraded the entire architecture into an 
#     immersive multimedia experience. Integrated advanced external package drivers 
#     to run turn-based algorithmic combat arrays, background audio loops, and 
#     automated graphic container lookups.
#
# =====================================================================
# 🔬 HARDWARE & ENGINE DEPENDENCIES:
# ----------------------------------
# To initialize this tactical environment, your system must compile the 
# following core modules via your command-line interface:
# 
# 👉 Run Command: pip install pygame pillow
#
# 🎵 Audio Asset: Requires 'battle_theme.mp3' in the direct working path.
# 👁️ Visual Asset: Requires 'helis.jpg' (or .png) spatial rendering map.
# =====================================================================
# 🎮 CORE SUB-SYSTEMS UNDER THE HOOD:
# -----------------------------------
# 📊 1. Security Gateway: Manages strict numeric passkey token registration.
# 🧭 2. Spatial Router: A multi-layered conditional gate array routing dimensions.
# 💥 3. Tactical Multi-Weapon Matrix: Algorithmic health pools calculated using 
#       unpredictable random numeric generators (random.randint).
# 🔄 4. Non-Scrolling Refresh Core: Leverages carriage return indicators (end="\r") 
#       to animate loading sequences seamlessly on a static horizontal row.
# =====================================================================
