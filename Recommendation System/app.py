from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for recommendations
recommendations = {
    'technology': ['Tech News', 'Gadget Reviews', 'Programming Tutorials'],
    'sports': ['Football News', 'Basketball Highlights', 'Sports Analysis'],
    'food': ['Recipe Ideas', 'Restaurant Reviews', 'Food Videos'],
}

@app.route('/', methods=['GET', 'POST'])
def home():
    recommended_items = []
    if request.method == 'POST':
        category = request.form.get('category')
        if category in recommendations:
            recommended_items = recommendations[category]
    return render_template('home.html', recommended_items=recommended_items)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001)
