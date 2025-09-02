def emoji(list_mood):
    mood_list = {
        "Senang":"😊",
        "Biasa":"😒",
        "Sedih":"😢",
        "Marah":"🙂",
        "Muak":"😤"
    }
    return list(map(lambda m:mood_list.get(m,"🤔"),list_mood))
