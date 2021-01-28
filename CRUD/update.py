#!C:\Users\황지환\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html")
print()
import cgi, os
files = os.listdir('data')
listStr = '' 
for item in files:
   listStr = listStr + '<li><a href = "index.py?id={name}">{name}</a></li>'.format(name = item)
form = cgi.FieldStorage()
if 'id' in form:
  pageId = form["id"].value
  description = open('data/' + pageId, 'r').read()
else:
  pageId = 'Welcome' 
  description = 'Hello web' 

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {list}
  </ol>
  <a href="create.py">create</a>
  <h2>{title}</h2>
  <form action="process_update.py" method="post">
    <input type="hidden" name="pageId" value="{form_default_title}">
    <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
    <p><textarea rows="4" name="desc" placeholder="description">{form_default_description}</textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, list = listStr, desc = description, form_default_title = pageId, form_default_description = description))