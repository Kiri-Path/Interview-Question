# Write a program that counts the number of times the letters "S", "K" and "Y" appear in a string
# You can write in pseudo code or any language you are comfortable with
# Be prepared to discuss your solution and any improvements that can be made at the interview
# Bonus marks will be given for enabling the code to be run and demonstrated at interview using replit.com and incorporating some units tests
 


def count_letters(input_string):
    
    # here we make the set of letters we need to look for.
    
    letters_to_count = {'S', 'K', 'Y'}
    
    #this line below creates a dictionrty for every letter in letters to count and gives it a value of 0. 
    
    count_dict = {letter: 0 for letter in letters_to_count}
    
    # we remove case nuance by making everything upper case.
    
    for char in input_string.upper():
        if char in letters_to_count:
            count_dict[char] += 1
            
    return count_dict

count_letters("This is a sentence")


# now with this solution below, this is to return only the letters which have a value
# so this time we will start with an empty dicitonary and then we will add letters accordingly.


def count_letters(input_string):
    letters_to_count = {'S', 'K', 'Y'}
    count_dict = {}
    
    
    # first we loop through every character is in the string
    # if the character is in letters to count, i.e its one of the letters we want to count
    # then if that value in not in the dictionary assign 1 else incrmeent by 1
    
    for char in input_string.upper():
        if char in letters_to_count:
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
            
    return count_dict


# lets say if we had an array of sentences or words, we could call on our function to get the desired solution
# we call our function 'count_letters' and pass it every sentences in the array of sentences. 
# this then becomes our values and our sentence is the key. 


def count_sentences1(sentences):
    return {sent : count_letters(sent) for sent in sentences}


# now if we had an array of sentences and we wanted to get the total count across all sentences we would have to do this slightly different
# first set up an empty dictionary, 

# loop through every sentence in sentences


def count_sentences2(sentences):
    count_dict = {}
    for sent in sentences:
        
        #this create a dictionary for sent_count because remember count_letters is a dictionary
        sent_counts = count_letters(sent)
        
        # the char and count is the key and value
        
        for char, count in sent_counts.items():
            
            # this section now allows us to merge the sentences together.
            if char not in count_dict:
                count_dict[char] = count
            else:
                count_dict[char] += count
    return count_dict

count_sentences2(["sent1", "kys", "kkkkksssss"])
