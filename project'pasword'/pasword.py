import random
import string

def read_from_file(name_file):
    with open(name_file,encoding='utf-8')as file:
        all_text = ""
        for element in file:
            all_text+=element
        return all_text.split('\n')
 
adj=read_from_file("adj.txt")
noun=read_from_file("nouns.txt")
num_adj=len(adj)
num_noun=len(noun)
adj_for_pass=random.randint(0,num_adj)
noun_for_pass=random.randint(0,num_noun)
def generate():
    global noun, adj
    num_adj=len(adj)
    num_noun=len(noun)
    adj_for_pas=random.randint(0,num_adj)
    noun_for_pas=random.randint(0,num_noun)
    num=random.randint(0,999)
    pasword=('Пароль: '+str(num)+adj[adj_for_pas]+noun[noun_for_pas])
    return pasword
print(generate())
