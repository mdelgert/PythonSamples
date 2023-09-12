# https://tools.oratory.com/altcodes.html

import random
import string

def generate_password(length=148):
    # Define the character set that includes letters, digits, and the specified symbols
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-={}[]|\\:;'<>,.?/~`¬¢£€¥¤¦§©ªº°µ¶·×÷∆√∞≈≠≤≥∑∫∴∼≡⊂⊃⊆⊇⊕⊗⊥←→↔↑↓↔⇐⇒⇔⇑⇓⇐⇑⇒⇓⇐⇒∀∃∄∇∈∉⊄⊂⊃∪∩∅∆∊∍∗∴∵∶∷≈≡≢≣≤≥≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡⊢⊣⊤⊥⊦⊧⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱⋲⋳⋴⋵⋶⋷⋸⋹⋺⋻⋼⋽⋾⋿"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example
if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)

