from datetime import datetime

from flask import current_app, render_template


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("index.html", day=day_name)


def movie_add_page():
    if not current_user.is_admin:
        abort(401)
    form = MovieEditForm()
    if form.validate_on_submit():
        title = form.data["title"]
        year = form.data["year"]
        movie = Movie(title, year=year)
        db = current_app.config["db"]
        movie_key = db.add_movie(movie)
        flash("Movie added.")
        return redirect(url_for("movie_page", movie_key=movie_key))
    return render_template("movie_edit.html", form=form)


def movie_page(movie_key):
    db = current_app.config["db"]
    movie = db.get_movie(movie_key)
    return render_template("movie.html", movie=movie)


def movies_page():
    db = current_app.config["db"]
    if request.method == "GET":
        movies = db.get_movies()
        return render_template("movies.html", movies=sorted(movies))
    else:
        if not current_user.is_admin:
            abort(401)
        form_movie_keys = request.form.getlist("movie_keys")
        for form_movie_key in form_movie_keys:
            db.delete_movie(int(form_movie_key))
        flash("%(num)d movies deleted." % {"num": len(form_movie_keys)})
        return redirect(url_for("movies_page"))


def validate_movie_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("title", "").strip()
    if len(form_title) == 0:
        form.errors["title"] = "Title can not be blank."
    else:
        form.data["title"] = form_title

    form_year = form.get("year")
    if not form_year:
        form.data["year"] = None
    elif not form_year.isdigit():
        form.errors["year"] = "Year must consist of digits only."
    else:
        year = int(form_year)
        if (year < 1887) or (year > datetime.now().year):
            form.errors["year"] = "Year not in valid range."
        else:
            form.data["year"] = year

    return len(form.errors) == 0


def movie_add_page():
    if request.method == "GET":
        values = {"title": "", "year": ""}
        return render_template(
            "movie_edit.html",
            min_year=1887,
            max_year=datetime.now().year,
            values=values,
        )
    else:
        valid = validate_movie_form(request.form)
        if not valid:
            return render_template(
                "movie_edit.html",
                min_year=1887,
                max_year=datetime.now().year,
                values=request.form,
            )
        title = request.form.data["title"]
        year = request.form.data["year"]
        movie = Movie(title, year=year)
        db = current_app.config["db"]
        movie_key = db.add_movie(movie)
        return redirect(url_for("movie_page", movie_key=movie_key))


# @login_required
def movie_add_page():
    if not current_user.is_admin:
        abort(401)
    form = MovieEditForm()
    if form.validate_on_submit():
        title = form.data["title"]
        year = form.data["year"]
        movie = Movie(title, year=year)
        db = current_app.config["db"]
        movie_key = db.add_movie(movie)
        flash("Movie added.")
        return redirect(url_for("movie_page", movie_key=movie_key))
    return render_template("movie_edit.html", form=form)


def movie_edit_page(movie_key):
    if request.method == "GET":
        db = current_app.config["db"]
        movie = db.get_movie(movie_key)
        if movie is None:
            abort(404)
        values = {"title": movie.title, "year": movie.year}
        return render_template(
            "movie_edit.html",
            min_year=1887,
            max_year=datetime.now().year,
            values=values,
        )
    else:
        valid = validate_movie_form(request.form)
        if not valid:
            return render_template(
                "movie_edit.html",
                min_year=1887,
                max_year=datetime.now().year,
                values=request.form,
            )
        title = request.form.data["title"]
        year = request.form.data["year"]
        movie = Movie(title, year=year)
        db = current_app.config["db"]
        db.update_movie(movie_key, movie)
        return redirect(url_for("movie_page", movie_key=movie_key))


def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        user = get_user(username)
        if user is not None:
            password = form.data["password"]
            if hasher.verify(password, user.password):
                login_user(user)
                flash("You have logged in.")
                next_page = request.args.get("next", url_for("home_page"))
                return redirect(next_page)
        flash("Invalid credentials.")
    return render_template("login.html", form=form)


def logout_page():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("home_page"))
