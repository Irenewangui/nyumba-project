from flask import (Flask, render_template, request, jsonify)
from peewee import IntegrityError
import bootstrap
from models.house import House
import images
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)

bootstrap.initialize()

images.initialize()


@app.route('/')
def index():
    # avail_houses = House.select()
    # return render_template('list_houses.html', houses=avail_houses)
    list_image = images.Images.select()
    results = []
    for image in list_image:
        image_item = {
            'description': image.description,
            # 'plot_no': image.plot_no,
            # 'no_rooms':image.no_rooms,
            # 'rent':image.rent,
            # 'no_bathrooms':image.no_bathrooms,
            # 'location':image.location,
            # 'nearby_amenities':image.nearby_amenities,
            # 'rating':image.rating,

            'thumbnail_link': image.thumbnail_link,
            'fullimage_link': image.fullimage_link
        }
        results.append(image_item)
    return render_template("list_houses.html", images=results)


@app.route('/houses/add', methods=['POST'])
def add_house():
    data = dict(request.form.items())
    try:
        House.create(
            plot_no=data.get('plot_no'),
            no_rooms=data.get('no_rooms'),
            rent=data.get('rent'),
            no_bathrooms=data.get('no_bathrooms'),
            location=data.get('location'),
            nearby_amenities=data.get('nearby_amenities'),
            rating=data.get('rating')
        )
        result = {'status': 'success'}
    except IntegrityError:
        result = {'status': 'failed', 'message': 'Plot number not unique'}
    finally:
        return jsonify(result)







if __name__ == '__main__':
    app.run(**app_start_config)