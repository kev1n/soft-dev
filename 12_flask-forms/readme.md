# Discoveries
  * a route can only respond to GET or POST requests respectively if they're allowed methods in the @app.route
  * GET forms use query strings and request.args to parse user input
  * POST forms use the response in request.form to parse user input
  * GET forms direct to a different URL while POST forms can stay on the same URL (because of querystrings being appended)
  * method="POST" must be included in the form tag in the HTML to produce a POST request. If left empty, it is a GET request by default.
  * in a GET request, request.form is ImmutableMultiDict([]) and in a POST request, request.args is ImmutableMultiDict([])
  * when reloading the POST request page on Brave, I get the popup "The page that you're looking for used information that you entered. Returning to that page might cause any action you took to be repeated. Do you want to continue?" On safari, it is "To reopen this page Safari must resend a form. This might result in duplicate purchases, comments, or other actions."
  * this behavior isn't the case when using GET for the response ^