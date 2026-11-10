html_content = """
<html>
         <head>
                  <title>my frist web page</title>
                  <style>
                  <body { background-color: #f0f8ff; font-family: Arial, sans-serif;  text-align: center; padding-top: 40px;}
                  <h1 {color: #333;}
                  p { font-size: 18px; color: #555;}
                  </style>
                  </head>
                  <body>
                  <h1>hello world!</h1>
                  <p>I JUST BUILT MY FIRST WEB PAGE FILE USING PYTHON!</p>
                  </body>
                  </html>
                  """
                  
with open("index.html", "w") as file:
    file.write(html_content)
    
print("success! your index.html web file has been created") 