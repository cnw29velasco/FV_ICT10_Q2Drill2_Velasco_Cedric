from pyscript import document, display


def add_name(e):

    first = document.getElementById('first').value
    last = document.getElementById('last').value
    full = first + ' ' + last + '(The newest member), '

    document.getElementById("output1").innerHTML = ""

    g10 = {"Logan Anaque, ", "Jacob Minguillo, ", "Gavin Ruiz, "}
    g9 = {"Robert Junior, ", "Boberto Junior, ", "Robertido Junior, "}
    g8 = {"Rick Grayson, ", "Bruce Wayne, ", "Clark Kent, "}  
    g7 = {"Wally West, ", "Barry Allen, ", "Oliver Queen, "}
    all_members = g10.union(g9, g8, g7)

    

    all_members.add(full)

    message = full + ", you are officially a new member of ICT Club, joined by, "

    display(message + "".join(sorted(all_members)), target = 'output1')



