import random

def generate_funny_name():
    prefixes = ["Fluffy", "Squishy", "Wacky", "Giggly", "Funky", "Silly", "Cheesy", "Bubbly", "Zany", "Goofy",
            "Snuggly", "Whacky", "Bouncy", "Dizzy", "Boinky", "Ziggy", "Nifty", "Fizzy", "Wiggly"]
    suffixes = ["McGee", "Fizzlebottom", "Wobblepants", "Noodleburger", "Bananaface", "Picklestein", "Pantsington",
                "Doodlebug", "Snickerdoodle", "Muffinman", "Jellybean", "TaterTot", "Biscuit", "Buttercup", "Cupcake",
                "Marshmallow", "Nugget", "Pudding", "Schnitzel", "Tootsie"]
    
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    return f"{prefix} {suffix}"