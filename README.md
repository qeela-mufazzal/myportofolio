Name : Qeela Mufazzal Rafif

NPM : 2506637104

Class : PBP KKI

MAMAH HINA!!! 😭😭😭

### Assignment 1
1. Some semantic elements were used to divide the page into several parts, which improved accessibility and code maintainability without relying on generic <div> elements.
2. I faced space constraints where the side-by-side grid columns and two-column info boxes would become squished on narrower screens. I prioritized keeping the primary identity and visual focus, such as name and photo, at the top, stacking elements vertically, shrinking the avatar width, and converting horizontal flex groups into vertical stacks to fit single-column mobile viewports.
3. To update some informations, we have to do it manually via code editing, making it tedious. I would find a way to actually make it able to update those datas automatically.

### Assignment 2
1. The project's urls.py intercepts the incoming HTTP request first, matches the /skills/ prefix, and routes it to the main application's URL configuration. Then, application's urls.py matches the relative path 'skills/' to the show_skills view function inside main/views.py. After that, views.py receives the request object, queries the Model (Skill.objects.all()), places the resulting queryset into a context dictionary ({'skills_list': skills_list}), and calls render(), while models.py executes an SQL query against the database (e.g., db.sqlite3) to retrieve all skill records and returns them as Python objects to the view, and template (skills.html) receives the context data and uses Django Template Language ({% for skill in skills_list %}) to dynamically generate HTML string structures. Finally, Django sends the rendered HTML back to the user's browser, which parses and displays the final styled web page.
2. Because storing data in a Model separates data management from application presentation. Updating or adding new portfolio items can be done via the Django Admin interface or shell without touching or re-deploying HTML code. Model data can be easily filtered, sorted, paginated, or reused across different pages without duplicating template code. Models enforce schema constraints, preventing invalid data entries.
3. makemigrations inspects changes made to models.py file and generates a new Python migration script. However, it does not touch or modify the database itself. While migrate reads unapplied migration files and executes SQL commands directly on database to update its structure and tables. For example, when you want to add a new field on Skill model, run python manage.py makemigrations after editing the model, then python manage.py migrate