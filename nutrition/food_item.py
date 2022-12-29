import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from .csv_reader import read_fact_file

bp = Blueprint('food', __name__, url_prefix='/food')

@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        error = None

        if not ingredient:
            error = 'Ingredient is required.'
        food_group = None
        if error is None:
            relevant_items = []
            for item in read_fact_file("C:\\Users\\VMARAM\\Downloads\\MyFoodData.csv"):
                if item['name'].lower().find(ingredient.lower()) != -1:
                    # title = item.pop('name')
                    food_group = item.pop('Food Group')
                    relevant_items.append(item.values())
                    print(f"appending {item['name']}")

            item.pop('Food Group')
            if len(relevant_items) == 0:
                error = f"No food with ingredient {ingredient} found"
                print("Error")
                flash(error)
            return render_template('food/details.html', food_group=food_group, labels=item.keys(), values=relevant_items)


    return render_template('food/search.html')