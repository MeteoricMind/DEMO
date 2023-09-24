import random
import string
import re


def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password_length = int(input("Enter len of the password: "))

random_password = generate_random_password(password_length)
print("Random Password:", random_password)


def stemming(content):
    stemmed_content = re.sub('[a-zA-Z]',' ' , content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmes_content if not word in stopwords.word('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content 