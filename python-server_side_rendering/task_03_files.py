#!/usr/bin/python3
"""Creating a Basic HTML Template in Flask"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    """home"""
    return render_template('index.html')


@app.route('/about')
def about():
    """about"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """contact"""
    return render_template('contact.html')


@app.route('/items')
def items():
    """items"""
    with open('items.json') as f:
        content = json.load(f)
    return render_template('items.html', items=content.get('items', []))


def read_json(filename):
    """read from JSON file"""
    with open(filename) as f:
        return json.load(f)


def read_csv(filename):
    """read from CSV file"""
    products = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
        return products


@app.route('/products')
def products():
    """products"""
    source = request.args.get('source')
    product_id = request.args.get('id')
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:
        return render_template('product_display.html',
                               error='Wrong source')
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error='Product not found')
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found')
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
