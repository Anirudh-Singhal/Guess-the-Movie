# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:26:11 2020

@author: anirudh
"""
import random

movies=['anand','drishyam','nayak','golmaal','black friday','sooryavansham','avengers','khuda haafiz','gunjan saxena','kabir singh']

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if(letters[i]==' '):
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    n=len(movie)
    temp=[]
    for i in range(n):
        if(ref[i]==' ' or ref[i]==letter):
            temp.append(ref[i])
        else:
            if(qn_list[i]=='*'):
                temp.append('*')
            else:
                temp.append(ref[i])
    qn1=''.join(str(x) for x in temp)
    return qn1
        


def play():
    p1name=input("Player 1, Please enter your name:")
    p2name=input("Player 2, Please enter your name:")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if(turn%2==0):       #player1
            print(p1name,' your turn')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said=True
            while not_said:
                letter=input("Your guessed letter is: ")
                if(is_present(letter,picked_movie)):
                    modified_qn = unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess complete movie and 2 for guessing the letter: "))
                    if(d==1):
                        ans=input("Your answer: ")
                        if(ans==picked_movie):
                            print("Correct")
                            pp1+=1
                            not_said=False
                            print(p1name,' Your score is ',pp1)
                        else:
                            print('Wrong answer. Try Again.')
                else:
                    print(letter,' not found')
            c=int(input("Press 1 to continue the game and 0 to quit the game: "))
            if(c==0):
                print(p1name,' Your score is ',pp1)
                print(p2name,' Your score is ',pp2)
                print("Thank you for playing the game.")
                willing=False
                
        else:
            print(p2name,' your turn')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said=True
            while not_said:
                letter=input("Your guessed letter is: ")
                if(is_present(letter,picked_movie)):
                    modified_qn = unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess complete movie and 2 for guessing the letter: "))
                    if(d==1):
                        ans=input("Your answer: ")
                        if(ans==picked_movie):
                            print("Correct")
                            pp2+=1
                            not_said=False
                            print(p2name,' Your score is ',pp2)
                        else:
                            print('Wrong answer. Try Again.')
                else:
                    print(letter,' not found')
            c=int(input("Press 1 to continue the game and 0 to quit the game: "))
            if(c==0):
                print(p1name,' Your score is ',pp1)
                print(p2name,' Your score is ',pp2)
                print("Thank you for playing the game.")
                willing=False
        turn=turn+1
        
play()
            
            
                            
    