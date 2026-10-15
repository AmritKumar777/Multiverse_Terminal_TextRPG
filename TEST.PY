# =====================================================================
# 🌌 SEQUENCE 1: SYSTEM SETUP & MECHANICAL AUDIO ENGINE
# =====================================================================

# 'os' gives Python direct hooks to talk to your computer's Operating System (Windows).
# We use it to wipe screens clear ('cls') and execute background color shifts.
import os

# 'time' is our temporal engine. We use it to pause the execution line 
# to create cinematic pacing, typewriter scrolling, and suspense delays.
import time

# 'random' is our gaming calculation tool. It allows the computer to pick 
# unpredictable numerical values on the fly to simulate combat damage variances.
import random

# 'sys' stands for System. It handles how text streams move out of Python.
# We use its 'stdout.write' to force text to draw pixel-by-pixel onto your monitor.
import sys

# 'winsound' is a native Windows library that sends raw sound wave instructions 
# straight to your computer's hardware motherboard speaker chassis.
import winsound  

def typewriter_print(text, speed=0.04, pitch=1200):
    """
    THE MECHANICAL TYPEWRITER AUDIO CORE
    This function splits any string of text into isolated characters, 
    printing them one-by-one while snapping a match beep frequency for every letter.
    """
    # This loop isolates every single character (letters, punctuation, numbers) in your string
    for char in text:
        # sys.stdout.write prints the current character without forcing an automatic "Enter" key hit
        sys.stdout.write(char)
        
        # Normally, Python waits for a sentence to finish before drawing it. 
        # .flush() forces Windows to instantly paint that specific letter on the monitor.
        sys.stdout.flush() 
        
        # Safety Check: If the character is a real letter or number, blare a keystroke click!
        # If it's just an empty space " " or a line break, stay silent so the audio flows naturally.
        if char != " " and char != "\n":
            # winsound.Beep(frequency_hz, duration_in_milliseconds)
            # Duration is locked at 15ms so the click noise doesn't stall the typing speed.
            winsound.Beep(pitch, 15)
        else:
            # If it's a blank space, apply a micro delay to simulate human typing gaps
            time.sleep(speed)
            
        # Apply a micro-second rest before moving onto the next character in the string
        time.sleep(speed)
        
    # Once the entire sentence finishes typing out, this prints a clean "Enter" row shift
    print() 

def render_image_in_terminal(image_path, target_width=85):
    """
    THE CONSOLE GRAPHICS GRAPH RENDER ENGINE
    This function breaks down your 'helis.jpg' photograph, reads its pixels, 
    and reconstructs it inside a scrolling text box using grayscale blocks.
    """
    try:
        # We import the Pillow image decoder only inside this function to keep memory low
        from PIL import Image  
        
        # Tell Pillow to scan the hard drive and lock onto your image asset
        img = Image.open(image_path)
        
        # Math Check: Calculate the exact proportional ratio so HELIS doesn't look stretched or warped
        aspect_ratio = img.height / img.width
        # Vertical characters are taller than they are wide. 
        # Multiplying by 0.45 squishes the row heights down to create a perfect square shape on text console boxes.
        target_height = int(target_width * aspect_ratio * 0.45) 
        
        # Resize the photo dimensions and convert it into Grayscale mode ("L" stands for Luminance/Lightness)
        # This strips out colors and leaves us with pure brightness values from 0 (Black) to 255 (White).
        img = img.resize((target_width, target_height)).convert("L") 
        pixels = img.load() # Load the raw pixel coordinate stream into local memory
        
        # This is our shading palette. It maps black to empty spaces and bright gray to solid blocks.
        chars = [" ", "░", "▒", "▓", "█"]
        
        # Print a solid separating boundary line across the terminal window width
        print("\n" + "─" * target_width)
        
        # Loop vertically row-by-row through the height grid of the picture
        for y in range(target_height):
            line = "" # Create a completely blank string container for the current line
            
            # Loop horizontally item-by-item across the columns of that row
            for x in range(target_width):
                pixel_val = pixels[x, y] # Grab the numeric brightness score (0 - 255) of this single coordinate
                
                # Turn that 0-255 score into an index number from 0 to 4 to match our character palette array
                char_index = int((pixel_val / 255) * (len(chars) - 1))
                
                # Append that specific shading block character to our text line string
                line += chars[char_index]
                
            # Print that entire completed row out to the terminal log screen
            print(line)
            
        # Print a solid closing boundary line across the bottom width of the drawing
        print("─" * target_width + "\n")
    except Exception:
        # If the file was moved or deleted, catch the crash and display a descriptive game warning!
        print("\n⚠️ [Visual Link Offline]: Ensure 'helis.jpg' is saved inside your project folder!")

# =====================================================================
# 🌌 SEQUENCE 2: IDENTITY VERIFICATION & PORTAL INTERFACE
# =====================================================================

# input() pauses the code stream and waits for keyboard text input.
# .strip() removes any accidental leading or trailing empty spaces the user typed.
print("⚡ Identify yourself, Universe-Hopper: ", end="")
name = input().strip()

# Verification Gate: If 'name' has text inside it (it's not blank), let them proceed!
if name: 
    # SOUND ENGINE TRICK: An ascending three-note chime sequence indicating security access!
    winsound.Beep(600, 80)
    winsound.Beep(800, 80)
    winsound.Beep(1000, 150)
    
    # We call our typewriter driver to write out the data synchronization message dramatically
    typewriter_print(f"\nWelcome, Agent {name}. Syncing reality parameters...", speed=0.03, pitch=1500)
    time.sleep(0.5)
    
    print("🔐 Generate your Multiverse Passkey Number: ", end="")
    try:
        # Wrap input inside int() to convert text strings (like "123") into actual mathematical numbers (123)
        passkey_id = int(input())
    except ValueError:
        # EXCEPTION HANDLER SAFETY NET: If the user accidentally types letters (like "abc") instead of a number,
        # int() will throw a crash warning. This block catches that error, sounds a low alarm buzz, and sets a safety passkey!
        winsound.Beep(250, 400)
        print("🚨 Passkey sequence broken! Defaulting to emergency override number.")
        passkey_id = 999
        
    # SOUND ENGINE TRICK: A satisfying two-note lock confirmation sequence!
    winsound.Beep(900, 100)
    winsound.Beep(450, 200)
    
    print("🔒 Passkey registered. Cosmic coordinates unlocked.\n")
    time.sleep(1.0)
    
    # Render the central menu structure layout onto the console interface
    print("🌌 =========================================== 🌌")
    print("       --- MULTIVERSE PORTAL INTERFACE ---       ")
    print("🌌 =========================================== 🌌")
    print("1. Go to Earth 616")
    print("2. Enter the Hellverse [⚠️ EXTREME CELESTIAL THREAT]")
    print("3. Return to Normal World")
    print("4. End this Multiverse")
    print("=================================================")
    
    world_choice = input("Select destination coordinates (1-4): ").strip()
    
    # Option 1 Branch Selection
    if world_choice == "1":
        os.system('color 9') # 'color 9' turns the terminal background black and font to Light Blue
        print(f"\n🚀 Portal stabilized! Welcome to Earth 616, {name}. Watch the skies for the Avengers.")
# =====================================================================
# 🌌 SEQUENCE 3: STORYTELLING MODE & CHIPTUNE SIREN ALARMS
# =====================================================================

    # Option 2 Branch Selection — Entering the main combat map arena
    elif world_choice == "2":
        os.system('color 4') # 'color 4' shifts the font color to Blood Red for instant danger warning
        print("\n🚨 WARNING: EXTREME MASS CONCENTRATION DETECTED AHEAD.")
        time.sleep(1.5)
        
        # --- THE LORE ACCOUNT CACHE ---
        print("\n📜 --- INTEL FILE: AGENT BACKSTORY CACHE ---")
        print("-----------------------------------------------------")
        typewriter_print("Years ago, you were just a normal builder skimming through old data files.", speed=0.03, pitch=1300)
        time.sleep(0.8)
        typewriter_print("Then, the reality shift happened. You learned to command variables.", speed=0.03, pitch=1300)
        time.sleep(0.8)
        typewriter_print("You became an elite Agent—the only programmer capable of shifting timelines.", speed=0.03, pitch=1300)
        time.sleep(0.8)
        typewriter_print(f"Now, the ultimate trial has arrived. Your entire life's journey has led to this.", speed=0.03, pitch=1300)
        print("-----------------------------------------------------")
        
        # THE SPEED-BUMP MECHANISM: input() acts as a temporary brake. 
        # Python freezes here and won't proceed until you physically click the "Enter" key on your board.
        input("\n[Press ENTER to accept the mission and descend...]")
        
        # THE HORIZONTAL CHAR LEVEL PROGRESSION ANIMATION
        # end="\r" prevents the text from hitting the "Enter" key under the hood. 
        # It forces the console cursor to sprint back to the far left of the row, overwriting the same line!
        print("\n[░░░░░░░░░░] 0% Ripping fabric of space-time...", end="\r")
        time.sleep(0.4)
        print("[████░░░░░░] 40% Resisting gravitational pull...", end="\r")
        time.sleep(0.5)
        print("[████████░░] 80% Shielding biological vital markers...", end="\r")
        time.sleep(0.4)
        print("[██████████] 100% DISPATCH COMPLETE. BRACE FOR IMPACT.", end="\r")
        time.sleep(1.0)
        
        os.system('cls') # Wipe the entire console frame buffer totally clean for a fresh visual impact frame
        
        # MOTHERBOARD AUDIO TRICK: A rapid oscillating siren whistle loop!
        for _ in range(3):
            winsound.Beep(800, 150)
            winsound.Beep(600, 150)
        
        # THE CORRECTED GRAPHIC SKULL ACCU-BANNERS
        # The 'r' before the string quotes means "Raw String". 
        # It commands Python to completely ignore backslash formatting codes so our ASCII art slashes don't break the compiler!
        print(r"""
             ______  
          .-'      '-.   ████████ ██    ██ ████████ ████████ ████████  ███    ██  ████████ 
         /            \  ██       ███   ██    ██    ██       ██     ██ ████   ██ ██        

        |              | ██████   ██ ██  ██   ██    ██████   ████████  ██ ██  ██ ██   ████ 
        |,  .-.  .-.  ,| ██       ██  ██ ██   ██    ██       ██   ██   ██  ██ ██  ██     ██ 
        | )(__/  \__)( | ████████ ██   ████   ██    ████████ ██    ██  ██   ████  ████████ 
        |/     /\     \| 
        (_     ^^     _) ██     ██ ████████ ██       ██       ██     ██ ████████ ████████ ████████ 
         \  '____'  /    ██     ██ ██       ██       ██       ██     ██ ██       ██     ██ ██       
          '========='    █████████ ██████   ██       ██       ██     ██ ██████   ████████  ██████   
                         ██     ██ ██       ██       ██        ██   ██  ██       ██   ██   ██       
                         ██     ██ ████████ ████████ ████████   █████   ████████ ██    ██  ████████ 
        """)
        print("=========================================================================================")
        print(f"   Dimensional Gateway Absolute Breached. Agent {name} has entered the dark sector.")
        print("=========================================================================================\n")
        time.sleep(1.5)
# =====================================================================
# 🌌 SEQUENCE 4: TACTICAL WEAPON SELECTION & COMBAT RESOLUTION
# =====================================================================

        print("Sky distortion active... HELIS MANIFESTS IN THE TERMINAL FEED!")
        time.sleep(1.0)
        
        # Fire our graphics engine function to draw your saved 'helis.jpg' file right inside the log logs!
        render_image_in_terminal("helis.jpg", target_width=85)
        
        print("Its face is a churning black hole, radiating blinding neutron star energy.")
        print("Your combat suit powers up, initializing your heavy weapons systems...")
        time.sleep(3.5)
        
        # Establish structural starting metric variables for health tracks
        player_hp = 100
        boss_hp = 150  
        
        # THE TURN-BASED ENGINE LOOP: As long as BOTH fighters are alive (> 0 HP), keep the round options rolling!
        while player_hp > 0 and boss_hp > 0:
            # Display current running score allocations using f-string evaluation injectors
            print(f"\n📊 STATUS: [Agent {name}: {player_hp} HP]  |  [HELIS: {boss_hp} HP]")
            print("-----------------------------------------------------")
            print("1. Fire Iron Man Union Beam ⚡ (High critical potential)")
            print("2. Deploy Custom Missile Punch Blaster 🥊🚀 (Heavy impact damage)")
            print("3. Spray Electric Ice Glue ❄️🧪 (Deals damage + minor tactical heal)")
            print("4. Retreat through the dimensional rift 🏃‍♂️")
            
            action = input("\nSelect your weapon matrix option (1-4): ").strip()
            
            # Weapon Option 1 Selection Branch
            if action == "1":
                # AUDIO ATTACK NOTES: Three rising chiptune frequency sweeps to sound like a laser charging!
                winsound.Beep(400, 100)
                winsound.Beep(600, 100)
                winsound.Beep(1200, 300)
                
                # Unpredictable wide damage variance calculations
                damage = random.randint(15, 50)
                boss_hp -= damage # Subtract that damage tracking from HELIS's health pool balance
                print(f"\n⚡ UNLEASHED! Your chest core fires a massive Union Beam! You burn HELIS for {damage} cosmic damage!")
                time.sleep(1.0)
                
            # Weapon Option 2 Selection Branch
            elif action == "2":
                # AUDIO ATTACK NOTES: A heavy, elongated low-frequency thud to replicate a rocket recoil blow!
                winsound.Beep(250, 400)
                
                # Steady, high-impact localized structural damage
                damage = random.randint(25, 35)
                boss_hp -= damage
                print(f"\n🚀 BOOM! Your mechanical gauntlet launches rocket-fists! You punch HELIS for {damage} heavy kinetic damage!")
                time.sleep(1.0)
                
            # Weapon Option 3 Selection Branch
            elif action == "3":
                # AUDIO ATTACK NOTES: A rapid upward zip sound to indicate healing/system recovery!
                winsound.Beep(900, 80)
                winsound.Beep(1100, 80)
                
                damage = random.randint(10, 20) # Lower defensive damage score
                heal = random.randint(10, 15)   # Recovery health value generator
                boss_hp -= damage
                player_hp += heal               # Add that health value score straight back to your player character pool
                
                # BOUNDARY CAPPING: Ensures your nanite suit can never accidentally overcharge your health past 100 HP!
                if player_hp > 100:
                    player_hp = 100
                print(f"\n❄️ GLUED! Electrified Ice pins the black hole face! HELIS takes {damage} damage, and your suit diagnostics restore {heal} HP!")
                time.sleep(1.0)
                
            # Flee Escape Selection Branch
            elif action == "4":
                print("\n🏃‍♂️ Rift destabilized! You execute an emergency backwards jump out of the system!")
                break # Shatters the current while loop explicitly and exits the battle map map
                
            else:
                # Catch-all filter if the user presses letters or typing mistakes during their battle turn
                print("\n❌ System override error! You fumbled your controls and missed a turn!")
                time.sleep(1.0)
            
            # THE BOSS RETALIATION SEQUENCE
            # Safety Check: Only let HELIS strike back if its health didn't hit 0 from your action!
            if boss_hp > 0 and action in ["1", "2", "3", ""]:
                # AUDIO BOSS NOTES: A terrifyingly deep, prolonged low grumble!
                winsound.Beep(180, 500)
                
                boss_attack = random.randint(15, 30)
                player_hp -= boss_attack # Deduct the claw blow from your personal running health track
                print(f"🌌 HELIS distorts gravity! A gamma-ray burst from its neutron eyes burns you for {boss_attack} HP!")
                time.sleep(1.5)
        
        # --- BATTLE TERMINATION OUTCOME EVALUATOR ---
        
        # Victory Outcome Branch
        if boss_hp <= 0:
            os.system('color A') # Flash the entire background theme to bright hacker green for triumph!
            
            # TRIUMPH FREQUENCIES: A classic, fast ascending arcade victory scale fanfare!
            winsound.Beep(500, 200)
            winsound.Beep(600, 200)
            winsound.Beep(800, 200)
            winsound.Beep(1000, 400)
            print(f"\n🏆 UNIVERSE SAVED! Agent {name} collapsed the black hole! HELIS has been completely evaporated!")
            print("Your life's journey as an Agent is complete. You have achieved peak legendary status.")
            
        # Failure Outcome Branch
        elif player_hp <= 0:
            # DEATH FREQUENCIES: A slow, depressing descending tone sequence to signal game over!
            winsound.Beep(300, 300)
            winsound.Beep(200, 300)
            winsound.Beep(120, 600)
            print(f"\n💀 SPAGHETTIFIED. Agent {name} was crushed by the absolute gravitational pull of HELIS. Game Over.")

    # Option 3 Branch Selection from the main hub menu
    elif world_choice == "3":
        print(f"\n🏡 Reality sync complete. Sending {name} safely home to drink warm coffee.")

    # Option 4 Branch Selection — The system erasure termination code
    elif world_choice == "4":
        os.system('color 4')
        print("\n💥 SYSTEM CRITICAL: TERMINATION OF TIMELINES INITIALIZED.")
        time.sleep(1.0)
        os.system('cls') # Visual wipe
        exit()          # Hard stop execution engine command
        
    else:
        # Safety net fallback if the user types a menu choice outside 1 - 4
        print("\n❌ Invalid coordinates! Your atoms scatter across the void.")

else:
    # Trigger fallback if someone tries to breach the system without typing a registration handle name
    print("Access Denied. Anonymous entities are expelled X_X")
