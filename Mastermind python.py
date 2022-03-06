#Mastermind game
import random

#Function 1
#2.0 Genertes 4 random colours from a list of colours (x) and then returns the generated colours in a list 
def generate_random():
    #Iterative 2 
    for i in range(4):
       random_generate=str(random.choice(x)) #2.1 Using random module to generate random 4 colours through looping of 4 times 
       list_random.append(random_generate) #2.2 Append the generated colours into a list 
    return list_random 

#Function 2
#3.0 Function that is welcome menu that mainly displays all necessary guidelines to play this game 
def welcome_menu():
    print ('Hope you have fun playing this game, '+str(input_name)+'\n') 
    print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUIDELINES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print ('  1. Colours will be randomly generated from a list of 6 colour and may occur more than once.')
    print ('  2. The list of possible colours are red, blue, green, yellow, violet and indigo.')
    print ('     In your input of colours, you must use the following abbreviations (DO NOT type the name of colour!):') 
    print ('     (a) Red: R')
    print ('     (b) Blue: B')
    print ('     (c) Green: G')
    print ('     (d) Yellow: Y')
    print ('     (e) Violet: V')
    print ('     (f) Indigo: I')
    print ('  3. You will need to guess the colour and its sequence correctly. There will be 6 colour choices and 4 colour sequence.')
    print ('  4. You will have 10 chances to guess the correct colour and its position before losing the game.')
    print ('  5. You will need to input your colour choice seperately by its position. ')
    print ('  6. An indicator will be displayed at the end of the game')
    print ('  7. Example :')
    print ('     Enter your guess for 1st colour in abbreviation: G')
    print ('     Enter your guess for 2nd colour in abbreviation: G')
    print ('     Enter your guess for 3rd colour in abbreviation: V')
    print ('     Enter your guess for 4th colour in abbreviation: Y')
    print ('     Your input of guess is GGVY \n')
    print ('     Indicator:')
    print ('     (1) Number of correct colour in correct position:1 ')
    print ('     (2) Number of correct colour but in wrong position:1')
    print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print ('Code is being generated')
    print ('All the best, '+str(input_name)+' in guessing :)\n')

#Function 3
#5.0 Function that allows users to input their guess seperately then combine them into a guess. It also validates wheter input is valid 
def input_check():
    guess_strdth=1
    print (str(input_name)+', this is your '+str(count_display)+' (st/rd/th) guess')
    print ('----- Choice of colours in abbreviation: R, G, B, Y, V, I -----')
    
    #5.1 User guess is collected through. User guess is converted to upppercase and combined as one answer
    for i in range (4):                        #Iterative 3 
      input_guess1=input('>>>Enter your guess for '+str(guess_strdth)+' [st/rd/th] colour in abbreviation:')
      convert_uppercase =input_guess1.upper()
      
      #5.2 If user answer is not R, G, B, Y, V or I, user will be prompted to input their answer again
      if convert_uppercase not in x:          #Decision making 1
          print ('\n Your guess must be either R, G, B, Y, V or I only ')
          input_guess2=input('Enter your guess for '+str(guess_strdth)+' [st/rd/th] colour in abbreviation again:')
          convert_uppercase =input_guess2.upper()
      guess_strdth+=1
      input_guess.append(convert_uppercase)
    input_guess_display=''.join(input_guess)
    print ('| Your guess is: '+input_guess_display+'  |')
    return input_guess

#Function 4 
#6.0a Function that displays some command for users to enter yes or no based on their decision of wanting to change their guess 
def display_confirm():
    print ('\n Confirm answer?')
    print ('.....If the colour sequence displayed above is your intended guess, input y')
    print ('.....If the colour sequence displayed above is not your intended guess (you have accidently make a wrong guess etc..), input n to change it ')

#Function 5 
#6.0b Function that asks wheter user want to change the guess input (for user to enter the data again, rather than class it as an incorrect guess)
def confirmation_answer (confirm_answer):
    #Iterative 4
    while confirm_answer=='Y' or confirm_answer=='Y':
      print ('checking answer........................................')
      break

    #Iterative 5
    while confirm_answer=='N' or confirm_answer=='n':
      print ('Guide to change the colour you have input: ')
      print ('Example: BBGY')
      print ('>>>> If you want to change your input of first  colour which is B in BBGY -------Enter 0')
      print ('>>>> If you want to change your input of second colour which is B in BBGY -------Enter 1')
      print ('>>>> If you want to change your input of third  colour which is G in BBGY -------Enter 2')
      print ('>>>> If you want to change your input of fourth colour which is Y in BBGY -------Enter 3')
      input_append=input('Enter which position of colour to append (0,1,2,3): ') #6.1 Allows users to choose which colour to change by its list index
      str(input_append)
      if input_append=='0':    #Decision making 2 
        print('----- Choice of colours in abbreviation: R, G, B, Y, V, I -----')
        print('>>>>Append answer for 1st position of colour') #6.2 Tells users the position of colour that is choosen to be changed 
        append_choice=input('Your new guess for 1st position of colour: ') #6.3 User input the colour to change 
        
        #6.4a Append colour is capitalized and then is placed in list index of 0 while .pop(1) removes the first list index of the list
        #6.4b By this way, the original colour in list index of 0 is replaced by a new answer. Same concept is applied for the following codes
        input_guess.insert(0,append_choice.upper()) 
        input_guess.pop(1) 
        append_choice_display=''.join(input_guess) #6.5 Convert the appended list into a string 
        print ('| Your guess is: '+append_choice_display+'  |') 
                            
      elif input_append=='1':  
        print('----- Choice of colours in abbreviation: R, G, B, Y, V, I -----')
        print('>>>>Append answer for 2nd position of colour')
        append_choice=input('Your new guess for 2nd position of colour: ')
        input_guess.insert(1,append_choice.upper())
        input_guess.pop(2)
        append_choice_display=''.join(input_guess)
        print ('| Your guess is: '+append_choice_display+'  |') 
                            
      elif input_append=='2':   
        print('----- Choice of colours in abbreviation: R, G, B, Y, V, I -----')
        print('>>>>Append answer for 3rd position of colour')
        append_choice=input('Your new guess for 3rd position of colour: ')
        input_guess.insert(2,append_choice.upper())
        input_guess.pop(3)
        append_choice_display=''.join(input_guess)
        print ('| Your guess is: '+append_choice_display+'  |') 
                            
      elif input_append=='3':
        print('----- Choice of colours in abbreviation: R, G, B, Y, V, I -----')
        print('>>>>Append answer for 4th position of colour')
        append_choice=input('Your new guess for 4th position of colour: ')
        input_guess.insert(3,append_choice.upper())
        input_guess.pop(4)
        append_choice_display=''.join(input_guess)
        print ('| Your guess is: '+append_choice_display+'  |') 
                            
      else:
        #6.6 Allows users to input the position of colour to append again given that their input is neither 0,1,2 or 3
        print ('input again') 
        input_append=input('Enter which position of colour to append (0,1,2,3): ')

      #6.7 Allows users to choose wheter to continue append their guess or to proceed by checking the answer 
      print('\n Continue game?')
      print('.....Enter y if you are certain that there is no change of your guess, '+str(input_guess_display))
      print('.....Enter n if you still want to continue changing your guess')
      confirm_answer=input('Your response (y/n): ')

#Function 6
#7.0 Function that helps to checks wheter there is a correct guess or correct guess but at wrong position 
def check_answer(input_guess, list_random, correct_colour_correct_position, correct_colour_wrong_position):
    #7.1 The global generated code, (list_random) and input answer which is the user guess (input_guess) is copied to use it locally in this function
    #7.1b This is to ensure that global generated codes remains the same when this function is reused in looping 
    input_guess_local=input_guess[:]
    list_random_local=list_random[:]

    #7.2a The correct colours in correct positions are replaced by '-' to ensure no repetition of indicators.
    #7.2b An accumulator returns the number of correct colours in correct positions at the end after looping 
    for i in range (4):                #Iterative 6
        if (input_guess_local[i]==list_random_local[i]):    #Decision making 3
            correct_colour_correct_position+=1
            input_guess_local[i]='-'
            list_random_local[i]='-'

    #7.3a The correct colours in wrong positions are replaced by '*' to ensure no repetition of indicators
    #7.3b An accumulator returns the number of correct colours in wrong positions at the end after looping 
    for i in range (4):                #Iterative 7
         if input_guess_local[i] in list_random_local and (input_guess_local[i] != list_random_local[i]):   #Decision making 4
            correct_colour_wrong_position+=1
            position_of_ccwp=list_random_local.index(input_guess_local[i]) #7.4 List index of ccwp in input_guess_local_is identified
            list_random_local[position_of_ccwp]='*'
            input_guess_local[i]='*'

    #7.5 Similiar to traditional mastermind game, text-based indicator is displayed to user for black peg and white peg
    print ('\nIndicator (based on your guess(es)): ') 
    print ('  (1) Number of correct colour in correct position (black peg): '+str(correct_colour_correct_position))
    print ('  (2) Number of correct colour but in wrong position (white peg): '+str(correct_colour_wrong_position)+ '\n')
    return correct_colour_correct_position
    return correct_colour_wrong_position


#1.0 All global values are defined in this section which will be used locally in functions or globally 
x=['R','B','G','Y','V','I'] #List 1: storing available colours in abbreviation 
list_random=[] #List 2: storing randomly choosen colours in abbreviation 
input_guess=[] #List 3: storing user input guess 
input_guess_display=''.join(input_guess) #1.1 Converts lists into a string for displaying user's input 
turns=10
count_display=1
count=0
correct_colour_correct_position=0
correct_colour_wrong_position=0

#2.0 Generate random colours in abbrevation 
generate_random()

#3.0 General welcome display 
print ('Welcome to Mastermind game')
print ('''In this game, you will be the codebreaker of mastermind game. You will need to guess the correct colours in the correct sequence (with 6
possible colour choice) for 4 colours in a sequence (Ex: BBIV) given 10 chances. Of each guess, there will be
indicator indicating the correct colour guess in correct position and correct colour guess but in wrong position \n''')
input_name=input('Hi, what is your name? (enter your name/ nickname): ') #3.1 User input their name/ nickname 
welcome_menu()

#4.0 When there is more than 0 turns, users will continue to input their guess. When turns reaches 0/ user guess is fully correct, the games ends
#Iterative 1 
while turns >0:
    #5.0 User enter their guess and their guess is validated
    input_check()
    count+=1
    count_display+=1
    turns-=1

    #6.0 User are required to confirm their answer before checking. They are allowed to append their answer if they want to change it 
    display_confirm()
    confirm_answer=str(input('Confirm answer- is your answer your intended guess? (y/n): '))        
    confirmation_answer(confirm_answer)

    #7.0 User's guess is checked and indicators are displayed 
    check_answer(input_guess, list_random, correct_colour_correct_position, correct_colour_wrong_position)
    
    #8.0 If user answer is correct, user wins the game and the loop breaks
    if input_guess==list_random:   #Decision making 5
         print ('Congratulations, '+str(input_name)+' .You have won the mastermind game with '+str(count)+' counts/ guesses')
         print ('Good game. Hope you have fun')
         print ('Hope you enjoyed this mastermind game!')
         break
        
    #9.0 User input guess is cleared so that when it is looped to the next turn, the guess will not be added into the previous guess 
    input_guess.clear()
    
    #10.0 If user have used up all their turns, user lost the game and the loop breaks 
    if turns ==0:        #Decision making 6 
         print ('Unfortunately, '+str(input_name)+' you lost!')
         print ('You have used up all 10 chances. Game over.')
         list_random_display=''.join(list_random) #10.1a Converts list into a string for displaying the mastermind code 
         print ('The answer is: '+ str(list_random_display)) #10.1b Answer is displayed to user if user lost the game 
         break
        

