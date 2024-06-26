{% extends "layout.html" %}
{% block title %}Edit movie{% endblock %}
{% block content %}
    <h1 class="title">Edit movie</h1>

    <form action="" method="post" name="movie_edit">
      {{ form.csrf_token }}

      <div class="field">
        <label for="title" class="label">Title</label>
        <div class="control">
          {{ form.title(required=True, autofocus=True, class='input') }}
        </div>
        {% for error in form.title.errors %}
        <p class="help has-background-warning">
            {{ error }}
        </p>
        {% endfor %}
      </div>

      <div class="field">
        <label for="year" class="label">Year</label>
        <div class="control">
          {{ form.year(class='input') }}
        </div>
        {% for error in form.year.errors %}
        <p class="help has-background-warning">
            {{ error }}
        </p>
        {% endfor %}
      </div>

      <div class="field is-grouped">
        <div class="control">
          <button class="button is-primary is-small">Save</button>
        </div>
      </div>
    </form>
{% endblock %}