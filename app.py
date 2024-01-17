from flask import Flask, render_template

app = Flask(__name__)

#quotes
quotes = [
    "You have to believe in yourself when no one else does.” - Serena Williams",
    "When you have a dream, you've got to grab it and never let go. - Carol Burnett",
    "The biggest adventure you can take is to live the life of your dreams.” - Oprah Winfrey",
    "It does not matter how slowly you go, as long as you do not stop.” -  Confucius",
]

#routes
@app.route('/')
def home():
    #Ranndom quote from the above quotes list
    import random
    random_quote = random.choice(quotes)
    
    return render_template('index.html', quote=random_quote)

