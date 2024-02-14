from readchar import readkey, key

v = """Keep me safe, my God, for in you I take refuge.
I say to the LORD, “You are my Lord; apart from you I have no good thing.”
I say of the holy people who are in the land, “They are the noble ones in whom is all my delight.”
Those who run after other gods will suffer more and more. I will not pour out libations of blood to such gods or take up their names on my lips.
LORD, you alone are my portion and my cup; you make my lot secure.
The boundary lines have fallen for me in pleasant places; surely I have a delightful inheritance.
I will praise the LORD, who counsels me; even at night my heart instructs me.
I keep my eyes always on the LORD. With him at my right hand, I will not be shaken.
Therefore my heart is glad and my tongue rejoices; my body also will rest secure,
because you will not abandon me to the realm of the dead, nor will you let your faithful one see decay.
You make known to me the path of life; you will fill me with joy in your presence, with eternal pleasures at your right hand."""



words = v.split()

index = 0

while(index < len(words)):
    k = readkey().lower()
    
    if(k == key.DOWN):
        index = len(words)+1

    word = words[index]

    if(k.lower() == word[0].lower()):
        print(word, end=" ")
    else:
        print(word+"*", end=" ")

    index += 1
