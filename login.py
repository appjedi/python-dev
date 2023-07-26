{% extends "layout.html" %}
{% block title %}Login{% endblock %}
{% block content %}
    <section class="hero">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="column is-4 is-offset-4">
            <h3 class="title has-text-grey">Login</h3>
            <div class="box">
              <form action="" method="post" name="login">
                {{ form.csrf_token }}

                <div class="field">
                  <div class="control">
                    {{ form.username(required=True, autofocus=True,
                                     class='input is-large',
                                     placeholder='your username') }}
                  </div>
                  {% for error in form.username.errors %}
                    <p class="help has-background-warning">
                        {{ error }}
                    </p>
                  {% endfor %}
                </div>

                <div class="field">
                  <div class="control">
                    {{ form.password(required=True, class='input is-large',
                                     placeholder='your password') }}
                  </div>
                  {% for error in form.password.errors %}
                    <p class="help has-background-warning">
                        {{ error }}
                    </p>
                  {% endfor %}
                </div>

                <button class="button is-block is-info is-large is-fullwidth">
                  Login
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
{% endblock %}