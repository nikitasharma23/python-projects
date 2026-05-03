phonebook = {
    "AMIT": "9876543210",
    "RIYA": "9123456780"
}

def add_contact(name, number):
    name = name.upper()
    if name in phonebook:
        print(f"  [!] '{name}' already exists. Duplicate not allowed.")
    else:
        phonebook[name] = number
        print(f"  [+] Contact '{name}' added successfully.")

def search_contact(name):
    name = name.upper()
    # Exact match
    if name in phonebook:
        print(f"  [✓] {name} : {phonebook[name]}")
        return
    # Partial match (bonus)
    matches = {k: v for k, v in phonebook.items() if name in k}
    if matches:
        print(f"  [~] Partial matches found:")
        for k, v in matches.items():
            print(f"      {k} : {v}")
    else:
        print(f"  [✗] No contact found for '{name}'.")

def delete_contact(name):
    name = name.upper()
    if name in phonebook:
        del phonebook[name]
        print(f"  [-] Contact '{name}' deleted successfully.")
    else:
        print(f"  [✗] Contact '{name}' not found.")

def display_all():
    if not phonebook:
        print("  Phonebook is empty.")
    else:
        print(f"  {'NAME':<15} {'NUMBER'}")
        print("  " + "-" * 30)
        for name, number in phonebook.items():
            print(f"  {name:<15} {number}")


print("=" * 45)
print("         DICTIONARY PHONEBOOK")
print("=" * 45)

print("\n--- INITIAL CONTACTS ---")
display_all()

print("\n--- ADDING CONTACTS ---")
add_contact("Rahul", "9911223344")
add_contact("Priya", "9855667788")
add_contact("AMIT", "0000000000")  

print("\n--- PHONEBOOK AFTER ADDING ---")
display_all()

print("\n--- SEARCHING CONTACTS ---")
search_contact("Rahul")            
search_contact("ri")                
search_contact("Zara")              

print("\n--- DELETING A CONTACT ---")
delete_contact("Riya")
delete_contact("Zara")        

print("\n--- FINAL PHONEBOOK ---")
display_all()

print("\n" + "=" * 45)
print("          Phonebook Session End")
print("=" * 45)