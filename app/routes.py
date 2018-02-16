from flask import render_template, flash, redirect, url_for
from flask import request
from app.model import Product
from app import app

@app.route('/')
@app.route('/index')
def index():
    items = []
    products = Product.query.all()
    for product in products:
        items.append(product)
    return render_template("index.html", items=items)


@app.route("/product/<productid>")
def product(productid):
    currentproduct = Product.query.filter_by(id=productid).first_or_404()
    return render_template("product.html", product=currentproduct, imgpath =currentproduct.imgpath)



