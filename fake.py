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