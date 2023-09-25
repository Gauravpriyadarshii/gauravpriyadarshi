# Define your skills
programming_languages = ["Python", "C++", "Java"]
web_development = ["HTML/CSS", "JavaScript", "Flask"]
database = ["MySQL", "SQLite"]

# Generate the HTML code for skills
skills_html = f"""
<h3>Programming Languages:</h3>
<ul>
    {"".join(f"<li>{lang}</li>" for lang in programming_languages)}
</ul>
<h3>Web Development:</h3>
<ul>
    {"".join(f"<li>{tech}</li>" for tech in web_development)}
</ul>
<h3>Database:</h3>
<ul>
    {"".join(f"<li>{db}</li>" for db in database)}
</ul>
"""

# Open the HTML file and insert the generated skills HTML
with open("index.html", "r") as html_file:
    html_content = html_file.read()

# Insert the skills HTML after the "Projects" section
html_content = html_content.replace("<!-- Insert Skills Here -->", skills_html)

# Write the updated content back to the HTML file
with open("index.html", "w") as html_file:
    html_file.write(html_content)
