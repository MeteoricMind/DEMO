import timeit
import tkinter as tk
import random
import pygame
import math

class TypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Test")
        self.master.geometry("500x300")

        self.words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
        random.shuffle(self.words)

        self.label = tk.Label(self.master, text=' '.join(self.words), font=('Arial', 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=('Arial', 12))
        self.entry.pack(pady=10)

        self.button = tk.Button(self.master, text='Submit', font=('Arial', 12), command=self.start_test)
        self.button.pack(pady=10)

        self.score_label = tk.Label(self.master, text='', font=('Arial', 12))
        self.score_label.pack(pady=10)

    def start_test(self):
        start_time = timeit.default_timer()
        user_input = self.entry.get()
        end_time = timeit.default_timer()
        elapsed_time = end_time - start_time
        user_words = user_input.split()
        correct_words = 0
        for i in range(len(user_words)):
            if user_words[i] == self.words[i]:
                correct_words += 1
        accuracy = correct_words / len(self.words) * 100
        speed = (len(user_input) / (elapsed_time*60))//1000
        # acc_speed = math.floor(speed)
        self.score_label.config(text=f'\nTyping speed: {speed} word per minute\nAccuracy: {accuracy:.2f}%')
    

if __name__ == '__main__':
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()

sns.countplot(x="Survived",hue="Sex",data=df)
sns.countplot(x="Survived",hue="Pclass",data=df)
df["Age"].plot.hist()
df["Fare"].plot.hist(bins=20,figsize=(10,5))
sns.countplot(x="Survived",hue="SibSp",data=df)
df.isnull().sum()
df.head(5)
df.drop("Cabin",axis=1,inplace=True)
df.head(5)
df.shape
df.dropna(inplace=True)
df.shape
df.isnull().sum()
sex=pd.get_dummies(df['Sex'],drop_first=True)
sex.head(5)
embark=pd.get_dummies(df['Embarked'],drop_first=True)
embark.head(5)
pcl=pd.get_dummies(df["Pclass"],drop_first=True)
pcl.head(5)
df=pd.concat([df,sex,embark,pcl],axis=1)
df.head(5)
df.drop(["Embarked","Pclass","PassengerId","Name","Ticket"],axis=1,inplace=True)
df.drop("Sex",axis=1,inplace=True)
df.head(5)
X=df.drop("Survived",axis=1)
Y=df["Survived"]