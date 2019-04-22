questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

q_list = list(questions.values()) # split values, we don't need those keys
ing_list = list(ingredients.values()) # split values, we don't need those keys

def ask_customer():
    """ Ask customers what their tastes are"""
    while True:
        for i in q_list:
            print(i)
            n = str(input())
            if n.lower() == "y":
                show_off()
                return False

def show_off():
    """ Show off your bartender skills to the naive customer"""
    import random
    random.shuffle(ing_list) # shuffle random ingredients list
    print(ing_list[0])

ask_customer()
