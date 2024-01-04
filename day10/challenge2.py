 
def format_name ():
    """Takes a first and last name and format it
    to return the title case version of the name."""
    f_name = input("What is your first name? ").title()
    l_name = input("What is your last name? ").title()
    if f_name =="" or l_name =="":
        return "You didn't provide valid inputs."
    return  f"{f_name} {l_name}"

print(format_name())