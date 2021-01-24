from flask import Flask, jsonify
from flask_cors import CORS


# stub data for testing

game_cards = [
    {
        'title': 'Eclipse Phase',
        'website': 'https://eclipsephase.com/',
        'logo_img_src': 'https://eclipsephase.com/sites/all/themes/eclipse/logo.png',
        'logo_img_alt': 'eclipse phase logo',
        'tagline': 'a game of transhuman horror',
        'logo_img_style': {
            'background-color': 'black',
        }
    },
    {
        'title': 'Genesys',
        'website': 'https://www.fantasyflightgames.com/en/products/genesys/',
        'logo_img_src': 'https://images-cdn.fantasyflightgames.com/filer_public/70/67/7067c9e1-60bb-49ae-9b11-7d6e7926961d/gns01_anc_slider.jpg',
        'logo_img_alt': 'genesys logo',
        'tagline': 'a universal RPG based around winning narrative control',
    },
]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/games', methods=['GET'])
def all_games():
    return jsonify({
        'status': 'success',
        'cards': game_cards,
    })


if __name__ == '__main__':
    app.run()
