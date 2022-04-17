


# class
# rank(1,2....) , value, suit( cLub,spade,heart,dimaond)

# deck

# player(choose card from deck)
import random
suits={"club","heart","spade","diamond"}
ranks={"Two", "three","four","five","six","seven",
        "eight","nine","ten","jack","queen","king","ace"}
values={"Two":2, "three":3,"four":4,"five":5,"six":6,"seven":7,
        "eight":8,"nine":9,"ten":10,"jack":11,"queen":12,"king":13,"ace":14}


# In[2]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit= suit
        self.rank= rank
        self.value= values[rank]
    def __str__(self):
        return self.suit + "  of  " +  self.rank
    


# In[3]:


myfun=Card("heart" , "Two")


# In[4]:


myfun


# In[5]:


print(myfun)


# In[6]:


myfun.suit


# In[7]:


myfun.rank


# In[8]:


values={"Two":2, "three":3,"four":4,"five":5,"six":6,"seven":7,
        "eight":8,"nine":9,"ten":10,"jack":11,"queen":12,"king":13,"ace":14}


# In[9]:


values[myfun.rank]


# In[10]:


myfun1=Card("club","three")


# In[11]:


myfun1.value


# In[12]:


myfun.value<myfun1.value


# In[ ]:



        


# In[13]:


class Deck:
    def __init__(self):
        self.allcards= []
        
        for suit in suits:
            for rank in ranks:
                
                created_list =Card(suit,rank)
                self.allcards.append(created_list)
                
    def shuffle(self):
        random.shuffle(self.allcards)
        
    def deal_one(self):
        return self.allcards.pop()


# In[14]:


new_deck= Deck()


# In[15]:


first_card= new_deck.allcards[1]


# In[16]:


print(first_card)


# In[17]:


new_deck.shuffle()


# In[18]:


print(new_deck.allcards[1])


# In[19]:


new_deck.shuffle()


# In[20]:


mycard= new_deck.deal_one()


# In[21]:


print(mycard)


# In[22]:


len(new_deck.allcards)


# In[23]:


class Player:
    
    def __init__(self,name):
        
        self.name=name
        self.allcards=[]
        
    def remove_one(self):
        return self.allcards.pop(0)
    
    def add_card(self,new_card):
        if type(new_card)== type([]):
            # for multiple 
            return self.allcards.extend(new_card)
        else:
            # for single
            return self.allcards.append(new_card)
    
    def __str__(self):
        return f' player {self.name} has {len(self.allcards)} cards'
        
        


# In[24]:


new_player= Player("amisha")


# In[25]:


print(new_player)


# In[26]:


print(mycard)


# In[27]:


new_player.add_card(mycard)


# In[28]:


print(new_player)


# In[29]:


new_player.add_card([mycard,mycard,mycard])


# In[30]:


print(new_player)


# In[31]:


new_player.remove_one()


# In[44]:


print(new_player)


# In[45]:


player_one= Player("One")
player_two= Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range (26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())
    


# In[46]:


len(player_one.allcards)


# In[47]:


print(player_one)


# In[48]:


print(player_one.allcards[0])


# In[49]:


game_on = True


# In[52]:


round_num=0
while game_on:
    round_num+=1
    print(f"round{round_num}")
    
    if len(player_one.allcards)==0:
        print('player loose and second wins')
        game_on= False
        break
        
    if len(player_two.allcards)==0:
        print('player loose and one wins')
        game_on= False
        break
        
      #start a new round
    
    player_one_card=[]
    player_one_card.append(player_one.remove_one())
    
    player_two_card=[]
    player_two_card.append(player_two.remove_one())
    
    
    # while at_war
    
    at_war=True
    while at_war:
        
        if player_one_card[-1].value> player_two_card[-1].value:
            player_one.add_card(player_one_card)
            player_one.add_card(player_two_card)
            
            at_war=False
            
        elif player_one_card[-1].value< player_two_card[-1].value:
            player_two.add_card(player_one_card)
            player_two.add_card(player_two_card)
            
            at_war=False
            
            
        else:
            print('war')
            
            
            if len(player_one.allcards)<5:
                print('player second loose')
                game_on=False
                break
                
                
            elif len(player_two.allcards)<5:
                print('player first loose')
                game_on=False
                break
                
                
            else:
                for num in range(5):
                    player_one_card.append(player_one.remove_one())
                    player_two_card.append(player_two.remove_one())
    


# In[ ]:




