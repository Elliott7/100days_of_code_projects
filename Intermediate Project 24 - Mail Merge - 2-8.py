"""
Project Twenty Four - Mail Merge
Project to automate the creation of files and text invites. Easy but really cool
"""

invitation = "You are invited to my birthday this Saturday \n \nHope you can make it! \n \nMe"
with open("names.txt") as file:
    contents = file.read().split()
    print(contents)
    for name in contents:
        string = f"Dear {name}, \n \n" + invitation
        with open(f"letter_for_{name}.txt", 'w') as filee:
            filee.write(string)

