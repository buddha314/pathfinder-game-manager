from app import views

app = views.create_app()

app.run(debug=app.debug)
