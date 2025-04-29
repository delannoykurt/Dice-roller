from flask import Flask, render_template, request, url_for
import random

PORT = 5606

app = Flask(__name__)


@app.route('/')
def home():
    num_dice = int(request.args.get('dice', 2))  # Récupère le nombre demandé (2 par défaut)
    dice_results = [random.randint(1, 6) for _ in range(num_dice)]
    dice_images = [url_for('static', filename=f'images/dice{n}.png') for n in dice_results]
    total_score = sum(dice_results)

    dice_data = list(zip(dice_results, dice_images))  # Associe chaque résultat à son image

    return render_template('index.html', dice_data=dice_data, dice_results=dice_results, dice_images=dice_images, num_dice=num_dice, total_score=total_score)


#--------------------------/
if __name__ == "__main__":
    app.run(port=PORT, debug=True)
