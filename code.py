import pandas as pd # for data manipulation and analysis

from sklearn.feature_extraction.text import CountVectorizer # Scikit-learn library
# The CountVectorizer provides a simple way to both tokenize a collection of text documents and build a vocabulary of known words

from sklearn.metrics.pairwise import cosine_similarity #metric used to measure how similar the documents are irrespective of 
                                                       #their size
    
from tkinter import *

pw1=Tk()

df=pd.read_csv("movie_dataset.csv") # to read dataset
title_col=df["title"]

pw1.title("Enter Movie Name")  # title of prompt window 1
pw1.geometry("300x200")        # dimension of prompt window 1

def func1():    
    pic=e1.get()
    def get_title_from_index(index):
        return df[df.index == index]["title"].values[0]
    def get_index_from_title(title):
        return df[df.title == title]["index"].values[0]
    
    attributes=['keywords','cast','genres','director']

    for feature in attributes:
        df[feature]=df[feature].fillna('')

    def combine_attributes(row):
        try:
            return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
        except:
            print("Error",row)

    df["combined_attributes"]=df.apply(combine_attributes,axis=1)

    cv=CountVectorizer()
    matrix=cv.fit_transform(df["combined_attributes"])
    
    cosine_sim=cosine_similarity(matrix)
    movie_user_likes = pic     
    
    index=get_index_from_title(movie_user_likes)
    
    similar_movies=list(enumerate(cosine_sim[index])) #Enumerate() method adds a counter to an iterable and returns it in a form 
    #of enumerate object.This enumerate object can then be used directly in for loops or be converted into a list of tuples 
    #using list() method.
    
    sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)
    
    i=0
    list1=[]
    for movie in sorted_similar_movies:
        list1.append(get_title_from_index(movie[0]))
        i=i+1
        if i>10:
            break
    
    pw2=Tk()
    pw2.title("Recommendations")  # title of prompt window 2
    pw2.geometry("400x400")       # dimensions of prompt window 2

# for GUI and displaying information in prompt window 2
    lb1=Label(pw2, text = " ",pady=10) 
    lb1.grid(row = 0, column = 0, sticky = W)#sticky is used to indicate the sides and corners of the cell to which widget sticks
    lb2=Label(pw2, text = "Recommended Movies are : ",pady=10) 
    lb2.grid(row = 1, column = 0, sticky = W)
    lb3=Label(pw2, text = list1[1],padx=5,pady=7) 
    lb3.grid(row = 2, column = 0, sticky = W)
    lb4=Label(pw2, text = list1[2],pady=5,padx=5) 
    lb4.grid(row = 3, column = 0, sticky = W)
    lb5=Label(pw2, text = list1[3],padx=5,pady=7) 
    lb5.grid(row = 4, column = 0, sticky = W)
    lb6=Label(pw2, text = list1[4],pady=5,padx=5) 
    lb6.grid(row = 5, column = 0, sticky = W)
    lb7=Label(pw2, text = list1[5],padx=5,pady=7) 
    lb7.grid(row = 6, column = 0, sticky = W)
    lb8=Label(pw2, text = list1[6],pady=5,padx=5) 
    lb8.grid(row = 7, column = 0, sticky = W)
    
    pw2.mainloop() # infinite loop used to run the application, wait for an event to occur and process 
                   # the event as long as the window is not closed.

# for GUI and displaying information in prompt window 1
l1=Label(pw1, text = " ",pady=5) 
l1.grid(row = 0, column = 0, sticky = W) 
l2=Label(pw1, text = " Enter the movie name : ",pady=5) 
l2.grid(row = 1, column = 0, sticky = W)

e1=Entry(pw1, bd =5)
e1.grid(row = 2, column = 0, sticky = W,padx=4)

b1=Button(pw1,text="Submit",width=17,height=1,bg='cyan',command=lambda:func1())  
b1.grid(row = 3, column = 0, sticky = W, padx = 4,pady=5) 

l3=Label(pw1, text = " For your reference some movies are: Pan, Frozen... ",pady=10) 
l3.grid(row = 4, column = 0, sticky = W)
l4=Label(pw1, text = " Avatar, Tangled, King Kong... ",pady=1) 
l4.grid(row = 5, column = 0, sticky = W)

pw1.mainloop()  # infinite loop used to run the application, wait for an event to occur and process
                # the event as long as the window is not closed.