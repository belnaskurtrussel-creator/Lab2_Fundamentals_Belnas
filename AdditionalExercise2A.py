# Setup
target_name = "BELNAS".upper()   # Replace with your surname
SEED_NUM = int("TUPM-25-0291"[-1]) # Last digit of your student ID
redacted_name = ""

# Logic
for ch in target_name:
    if ch in "AEIOU":
        redacted_name += str(SEED_NUM)
    else:
        redacted_name += ch

# Output
print("Original Surname:", target_name)
print("SEED_NUM Used:", SEED_NUM)
print("Redacted Output:", redacted_name)
