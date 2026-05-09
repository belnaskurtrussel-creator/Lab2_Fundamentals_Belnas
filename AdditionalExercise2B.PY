# Setup
engineer_name = "ENGR. BELNAS"   # Replace with your name
SEED_NUM = int("TUPM-25-0291"[-1]) # Last digit of your student ID
loops = 14                            # Example: total loop cycles from Task 14

# Logic
ascii_val = ord(engineer_name[0].upper())
verification_hash = (ascii_val * SEED_NUM) - loops

# Output
print("First Letter ASCII:", ascii_val)
print("SEED_NUM:", SEED_NUM)
print("Total Loops:", loops)
print("Verification Hash:", verification_hash)
