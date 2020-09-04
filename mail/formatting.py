
msg_template = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com """
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""


def format_msg(my_name="venky", my_website="venky"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg
