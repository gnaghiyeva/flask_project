# from flask import Blueprint, Flask, render_template
# from create_dataframe import create_dataframe
#
# app = Flask(__name__)
#
# bp = Blueprint("pages", __name__)
#
# @app.route('/')
# def home():
#     # DataFrame oluşturma
#     url = "https://smartjob.az/vacancies"
#     dataframe = create_dataframe(url)
#
#     # HTML şablonunu render etme
#     return render_template('/pages/home.html', dataframe=dataframe)
#
# @app.route("/about")
# def about():
#     return render_template("pages/about.html")
#
# if __name__ == '__main__':
#     app.register_blueprint(bp)
#     app.run(debug=True)


from flask import Blueprint, render_template

from board.scrape import scrape_page

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    url = "https://smartjob.az/vacancies"
    jobs = scrape_page(url)
    return render_template('pages/home.html', jobs=jobs)

@bp.route("/about")
def about():
    return render_template("pages/about.html")