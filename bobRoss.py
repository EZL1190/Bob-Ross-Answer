import webget
import re

#url = 'https://raw.githubusercontent.com/HawkDon/Python_Assignment1/master/BobRoss.txt'

if __name__ == '__main__':
    url = input("URL to download: ")

webget.download(url)

bob_ross_txt = open("BobRoss.txt", 'r') 
# får en fejl når jeg prøver at udskrive texten
#Traceback (most recent call last):
#  File "d:/Desktop/CPH/Sem4/Python/Bob-Ross-Answer/bobRoss.py", line 16, in <module>
#    bob_ross_lines = bob_ross_txt.read().splitlines()
#  File "C:\Users\Elias\Anaconda3\lib\encodings\cp1252.py", line 23, in decode
#    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 14074: character maps to <undefined>

#1.

bob_ross_lines = bob_ross_txt.read().splitlines()
print("Number of lines: " + len(bob_ross_lines))

#2.

word_ruined_list = re.findall(r'(RUINED)', bob_ross_txt)
print("Times 'RUINED' appears: " + word_ruined_list.lastindex)

#3.

#4.

username_list = re.findall(r'([a-z]\w.*\:)', bob_ross_txt)
usernames = {}
for username in username_list:
    usernames.setdefault(username, 0)

print("Usernames: \n")
print(usernames)

#5.

words = {}

for word in bob_ross_txt:
    words.setdefault(word, 0)
    words[word] += 1

words_sortet = sorted(words.items(), key=lambda kv: kv[1])
print("The wword tha appears most times: " + next(iter(words_sortet)))





