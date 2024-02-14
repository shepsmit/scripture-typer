import sys
import msvcrt
import os



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

str_remove_list = ['“','"']
words = v.split()
index = 0

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def first_letter_matches(a:str, b:str):
    for char in str_remove_list:
        a = a.replace(char,'')
        b = b.replace(char,'')
    return (a[0].lower() == b[0].lower())

def std_print(msg:str):
        sys.stdout.write(msg)
        sys.stdout.flush()

def highlight_str(msg:str)-> str:
    msg = msg.upper()
    msg = '\033[1m' + msg + '\033[10'
    return(msg)


cls()
print("Psalm 16")
while(index < len(words)):
    k_bytes = msvcrt.getch()
    k_str = str(k_bytes, encoding='utf-8')

    # Exit Program
    if(k_str == "0"):
        index = len(words)+1
    
    else:
        word = words[index]

        if("." in word):
            delimiter = "\n"
        else:
            delimiter = " "

        # Correct guess displays as normal
        if(first_letter_matches(k_str,word)):
            std_print(word+delimiter)
        # Incorrect displays as bold and uppercase
        else:
            std_print(highlight_str(word+delimiter))

        index += 1
