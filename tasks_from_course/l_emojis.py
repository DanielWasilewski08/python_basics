def real_emojis_function(message):
    words = message.split(" ")
    emojis = {
        ":0": "😮",
        ":)": "🙂",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
print(real_emojis_function("I'm happy :)"))
print(real_emojis_function("I'm sad :("))
print(real_emojis_function("what's going on :0"))