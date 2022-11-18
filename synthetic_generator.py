####Synthetic Generator####
#Libaries
import csv
import random
from random import randint
import pandas as pd

##########################Stop Words,numbers,punctuation#######################
#Creating punctuation stop set

my_punct = {'=', '-', '/', '{', '#', '"', '(', '@', '$', '`', ',', ')', '+', '?', '.', '|', '}', '[', '_', '^', ';', '%', '&', '<', '>', ':', '\\', '~', '*', '!', ']', "'", "1","2","3","4","5","6","7","8","9","0"}
my_stopwords = {'out', 'we', 'was', 'how', 'myself', 'for', 'they', 'about', "hasn't", 'then', 'both', 'so', 're', 'don', 'm', 'as', 'any', 'mightn', 'after', 'you', 'wouldn', 'why', 'been', 'where', 'by', "isn't", 'yourself', 'wasn', 'a', "haven't", 'did', "hadn't", 'their', 'hasn', 'doing', 'be', 'further', 'ours', 'now', 'am', 'her', "you'll", 'yourselves', 'that', 'my', 'what', 'to', 'd', 'not', "won't", "couldn't", 'own', 'there', 'this', 'each', 'all', 'haven', 'more', 'me', 've', 'weren', 'which', 'himself', 'nor', 'other', "shouldn't", 'who', "should've", 'same', 'at', 'such', 't', 'up', 'than', 'can', "you've", 'too', 'these', 'while', "wasn't", 'ourselves', 'before', 'i', 'he', "didn't", 'our', 'its', 'but', 'with', "wouldn't", 'those', 'because', 'the', 'y', 'shouldn', 'it', 'mustn', 'hers', 'just', 'doesn', 'ain', 'between', 'over', 'had', 'aren', "mightn't", 'does', 'have', 'and', 'or', 'some', "mustn't", 'only', 'won', 'when', 'needn', 'below', 'in', 'if', 'theirs', "needn't", "aren't", 'isn', 'again', 'his', 'whom', 'll', 'hadn', 'above', 'should', 'itself', 'themselves', 'until', 'are', 'she', 'no', 'from', 'into', 'will', 'your', 'few', 'herself', 'of', 'has', 'down', 'were', 'once', 'ma', 'having', 'them', 'under', 'him', 'shan', 'couldn', 'do', 'on', 'an', "you'd", 'yours', 'being', 'off', 'o', "that'll", 'very', "weren't", 'didn', 'through', "you're", 'most', 'against', "it's", "doesn't", 'here', 'is', 's', "don't", "shan't", 'during', "she's"}
negative_ratings = pd.read_csv("https://raw.githubusercontent.com/success81/Veteran_Affairs_Synthetic_Data/main/Negative_VA_Reviews.csv")
positive_ratings = pd.read_csv("https://raw.githubusercontent.com/success81/Veteran_Affairs_Synthetic_Data/main/Positive_VA_Reviews%20.csv")
validation_data = pd.read_csv("https://raw.githubusercontent.com/success81/Veteran_Affairs_Synthetic_Data/main/VA_Validation_Data.csv")
neg_list = negative_ratings["Reviews"].tolist()
pos_list = positive_ratings["Reviews"].tolist()


    
###########################################################
#This is where you pull in CSV file
##################################################
#Importing excel
#NOTE: Filename is the name of the CSV file
filename = "syn_data.csv"
#Setting up lists for csv
fields = []
rows = []

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
######################################################

    











#####################FUNCTIONS#################################
###############################################
#csv_break- Breaks down a list into a string and list. Early steps
#Break list into strings for 0 index and list for second index for synonym
def csv_break(my_csv):
    capture_list = []
    output_list = []
    temp_syn_list = []
    for x in my_csv:
        output_list.append(x[0])
        temp_syn_list = x[1].split()
        capture_list.append(temp_syn_list)
        output_list.append(temp_syn_list)
        capture_list = []
        temp_syn_list = []
    return output_list
################################################
#string_break- Breaks down a single data input into a list containing each word in as a string
def string_break(input):
    blank_string = ""
    for x in input:
        if x not in my_punct:
            blank_string += x.lower()
    output = blank_string.split()
    return output
################################################
#non_stopwords- a list of non-stopwords
def non_stopwords(x):
    temp_list= []
    full_list= []
    final_output = []
    for num, word in enumerate(x):
        temp_list.append(num)
        temp_list.append(word)
        full_list.append(temp_list)
        temp_list = []
    for x in full_list:
        if x[1] not in my_stopwords:
            final_output.append(x[0])
    return final_output

#################################################
#This is will get you the dictionary of synonyms
def clean_dict(rows):
    my_dict = {}
    capture_list = []
    final_list = []
    my_run_count = 0
    compare_count = 0
    index_0 = 0
    index_1 = 1
    csv_test = csv_break(rows)  #This is the Csv file broken down
    run_count = int(len(csv_test)/2) #Halfing the count the loop will run
    while run_count != compare_count:
        capture_list.append(csv_test[index_0])
        capture_list.append(csv_test[index_1])
        final_list.append(capture_list)
        capture_list = []
        index_0 += 2
        index_1 += 2
        compare_count += 1
    for x in final_list:
        if x[0] not in my_dict:
            my_dict[x[0]]=x[1]
    return my_dict

#################synonym dictionary################
#This is a broken down dictionary of synonym
syn_dict = {}
transfer_list = []
transition_list = []
my_dict_list = rows

for x in rows:
    transfer_list.append(x[0])
    transfer_list.append(string_break(x[1]))
    transition_list.append(transfer_list)
    transfer_list = []
    
for x in transition_list:
    if x[0] not in syn_dict:
        syn_dict[x[0]] = x[1]
######################################################
#Function to return string back to normal from string Break
def reverse_string(x):
    plain_return = ""
    for word in x:
            plain_return += word
            plain_return += " "
    return plain_return
#####################################################
#####TEST AREA####
neg_validation_list = []
neg_string_break = []
neg_capture_list = []
neg_counter = 0
for x in neg_list:
    neg_validation_list.append(string_break(x))

for x in neg_validation_list:
    for word in x:
        if word in syn_dict:
            neg_counter += 1
    if neg_counter == 0:
        neg_capture_list.append(x)
    neg_counter = 0

        


    
######################################################
mini_test = "This is a test of the waiting complete complete va system"
    
def main_go(sent, cycles, small_run_var):
    temp_list = []
    temp_list_b = []
    word_and_num = []
    key_synonym_dict = {}
    working_sent = string_break(sent)
    master_syn_list = []
    keyword_index_list = [] 
    check_counter = 0
##word_and_num is the synonym word and index number 
    for num,word in enumerate(working_sent):
        temp_list.append(word)
        temp_list.append(num)
        word_and_num.append(temp_list)
        temp_list = []
        
##master_syn_list## is a list of all the synonyms attached to words in the string
    for x in word_and_num:
        if x[0] in syn_dict:
            temp_list_b.append(syn_dict[x[0]])
    for x in temp_list_b:
        for word in x:
            master_syn_list.append(word)
            
##key_synonym_dict## is a dictionary of the index of key words in the string and its associated synonyms
    for x in word_and_num:
        for k,v in syn_dict.items():
            if x[0] == k:
                key_synonym_dict[x[1]] = v
    
                

#####################################################
##keyword_index_list. This is a list of the indices that are in the syn library
    for k,v in key_synonym_dict.items():
        keyword_index_list.append(k)

    
        
#################################################

####################Letter Delete Action#################### 
#Function to remove one letter from one random word that isn't a key word and 3 or more letters
    def letter_delete_action(sent):
        index_capture = []
        def delete_random_letter(word):
            word = list(word)
            word.pop(random.randint(0, len(word) - 1))
            return ''.join(word)
        sent = string_break(sent)
        for num,word in enumerate(sent):
            if len(word) >= 3 and word not in syn_dict:
                index_capture.append(num)
        
        random_index = (random.choice(index_capture))
        rep_word = delete_random_letter(sent[random_index])
        sent[random_index] = rep_word
        
        return reverse_string(sent)
############################################################


############################################################
################Replace_Action##############################
    """"
    def replace_action(sent):
        check_counter = 0
        a_temp_list = []
        transfer_temp_list = []
        b_temp_list = []
        b_master_list = []
        key_synonym_dict = {}
        keyword_index_list = []
        sent = string_break(sent)
        
        for num,word in enumerate(sent):
            a_temp_list.append(word)
            a_temp_list.append(num)
            transfer_temp_list.append(temp_list)
            a_temp_list = []
            
        for x in transfer_temp_list:
            if x[0] in syn_dict:
                b_temp_list.append(syn_dict[x[0]])
        for x in b_temp_list:
            for word in x:
                b_master_list.append(word)

        for x in transfer_temp_list:
            for k,v in syn_dict.items():
                if x[0] == k:
                    key_synonym_dict[x[1]] = v

        for k,v in key_synonym_dict.items():
            keyword_index_list.append(k)
      
        random_index = (random.choice(keyword_index_list))
        sent[random_index] = (random.choice(key_synonym_dict[random_index]))
        sent = reverse_string(sent)
        return sent
        """
    def replace_action(sent):
        temp_list = []
        transition_list = []
        sent = string_break(sent)
        for num,word in enumerate(sent):
            if word in syn_dict:
                transition_list.append(word)
        random_word = (random.choice(transition_list))
        for i in range(len(sent)):
            if sent[i] == random_word:
                sent[i] = (random.choice(syn_dict[random_word]))
        sent = reverse_string(sent)
        return sent
                
        
############################################################=

############################################################
######################Insert Action#########################
    def insert_action(sent):
        sent = string_break(sent)
        random_index = (random.choice(keyword_index_list))
        quick_insert = (random.choice(key_synonym_dict[random_index]))
        sent.insert(randint(0,len(sent)), quick_insert)
        sent = reverse_string(sent)
        return sent
############################################################

############################################################
###################Word Delete Action#######################
    def word_delete_action(sent):
        index_capture = []
        sent = string_break(sent)
        for num,word in enumerate(sent):
            if word not in syn_dict:
                index_capture.append(num)
        random_index = (random.choice(index_capture))
        del sent[random_index]
        sent = reverse_string(sent)
        return sent
#############################################################
    """
    if len(string_break(sent)) <= 30:
        small_run_count = 3
    if len(string_break(sent)) >= 31 and len(string_break(sent)) < 60:
        small_run_count = 6
    if len(string_break(sent)) >= 61:
        small_run_count = 9
    """

    
    def my_dice_roll(text):
        small_run_counter = 0
        small_run_count = small_run_var  #delete
        while small_run_count != small_run_counter:
            dice_options=[1,2,3,4]
            #if len(keyword_index_list) > 2:
            #    dice_options=[1,3,4]
            #if len(keyword_index_list) == 0:
            #    dice_options=[1,3,4]
            dice_roll = random.choice(dice_options)
    
            #Dice Roll 1
            if dice_roll == 1:
                if small_run_counter == 0:
                    first = letter_delete_action(text)
                if small_run_counter == 1:
                    second = letter_delete_action(first)
                if small_run_counter == 2:
                    third = letter_delete_action(second)
                if small_run_counter == 3:
                    fourth = letter_delete_action(third)
                if small_run_counter == 4:
                    fifth = letter_delete_action(fourth)
                if small_run_counter == 5:
                    sixth = letter_delete_action(fifth)
                if small_run_counter == 6:
                    seventh = letter_delete_action(sixth)
                if small_run_counter == 7:
                    eighth = letter_delete_action(seventh)
                if small_run_counter == 8:
                    ninth = letter_delete_action(eighth)
                if small_run_counter == 9:
                    tenth = letter_delete_action(ninth)
                small_run_counter += 1

                #Dice Roll 2
            if dice_roll == 2:
                if small_run_counter == 0:
                    first = replace_action(text)
                if small_run_counter == 1:
                    second = replace_action(first)
                if small_run_counter == 2:
                    third = replace_action(second)
                if small_run_counter == 3:
                    fourth = replace_action(third)
                if small_run_counter == 4:
                    fifth = replace_action(fourth)
                if small_run_counter == 5:
                    sixth = replace_action(fifth)
                if small_run_counter == 6:
                    seventh = replace_action(sixth)
                if small_run_counter == 7:
                    eighth = replace_action(seventh)
                if small_run_counter == 8:
                    ninth = replace_action(eighth)
                if small_run_counter == 9:
                    tenth = replace_action(ninth)
                small_run_counter += 1
                
                    
                #Dice Roll 3
            if dice_roll == 3:
                if small_run_counter == 0:
                    first = insert_action(text)
                if small_run_counter == 1:
                    second = insert_action(first)
                if small_run_counter == 2:
                    third = insert_action(second)
                if small_run_counter == 3:
                    fourth = insert_action(third)
                if small_run_counter == 4:
                    fifth = insert_action(fourth)
                if small_run_counter == 5:
                    sixth = insert_action(fifth)
                if small_run_counter == 6:
                    seventh = insert_action(sixth)
                if small_run_counter == 7:
                    eighth = insert_action(seventh)
                if small_run_counter == 8:
                    ninth = insert_action(eighth)
                if small_run_counter == 9:
                    tenth = insert_action(ninth)
                small_run_counter += 1

            #Dice Roll 4
            if dice_roll == 4:
                if small_run_counter == 0:
                    first = word_delete_action(text)
                if small_run_counter == 1:
                    second = word_delete_action(first)
                if small_run_counter == 2:
                    third = word_delete_action(second)
                if small_run_counter == 3:
                    fourth = word_delete_action(third)
                if small_run_counter == 4:
                    fifth = word_delete_action(fourth)
                if small_run_counter == 5:
                    sixth = word_delete_action(fifth)
                if small_run_counter == 6:
                    seventh = word_delete_action(sixth)
                if small_run_counter == 7:
                    eighth = word_delete_action(seventh)
                if small_run_counter == 8:
                    ninth = word_delete_action(eighth)
                if small_run_counter == 9:
                    tenth = word_delete_action(ninth)
                small_run_counter += 1
                        

        if small_run_count == 3:
            return third
        if small_run_count == 6:
            return sixth
        if small_run_count == 9:
            return ninth

    cycle_counter = 0
    output_list = []

    while cycle_counter != cycles:
        temp = my_dice_roll(sent)
        if temp in output_list:
            pass
        if temp not in output_list:
            output_list.append(temp)
            cycle_counter += 1
    
    return output_list



va_entry = "If you have been in the military you know it's hurry up and wait.  If you need help there is a very easy way to get it.  Go to the patient advocates office.  They do help."
va_entry_long = "I go to this Hospital OFTEN, probably 20-30 visits a year. My Dad was a WWII vet and we utilize this facility for all his medical needs. EVERYONE at this hospital is fantastic. This is from the cafeteria people, coffee cart, store, nurses, Doctors, appoint setters, pharmacy, every department and every person we have encountered are the nicest people and there to ensure your visit is memorable. My Dad gets first rate care and the interactions with all personnel is red carpet. He has been to other VA facilities in New York and Arizona and they pale in comparison.  Every time we come to the La Jolla VA he marvels at the care (and competency of the personnel) he receives. You have no idea how lucky you are to be working for one of the finest facilities in the Nation. If you have been in the military you know it's hurry up and wait.  If you need help there is a very easy way to get it.  Go to the patient advocates office.  They do help. If you have been in the military you know it's hurry up and wait.  If you need help there is a very easy way to get it.  Go to the patient advocates office.  They do help."
neg_list = negative_ratings["Reviews"].tolist()
pos_list = positive_ratings["Reviews"].tolist()

#a = main_go(va_entry_long,200)

#print (a)
#print (a)

a = main_go(va_entry,1,6)
print(a)

###This is how you submit the queries 
"""
big_neg = []
for x in neg_list:
    if len(string_break(x)) <= 30:
            small_run_var = 3
    if len(string_break(x)) >= 31 and len(string_break(x)) < 60:
            small_run_var = 6
    if len(string_break(x)) >= 61:
            small_run_var = 9
    big_neg.append(main_go(x,2,small_run_var))

for x in big_neg:
    print (x)
"""
"""
big_pos = []
for x in pos_list:
    if len(string_break(x)) <= 30:
            small_run_var = 3
    if len(string_break(x)) >= 31 and len(string_break(x)) < 60:
            small_run_var = 6
    if len(string_break(x)) >= 61:
            small_run_var = 9
    big_pos.append(main_go(x,2,small_run_var))

for x in big_pos:
    print (x)
"""
