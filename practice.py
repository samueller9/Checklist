# Make a dictionary with information about yourself called “personal_info”
def personal_info = {
    'name' : "Stefan Mueller",
    'age'  :  20,
    'school' : "Dominican University of California",
# Add a “pets” node and list an array of your pets. (or parents or siblings)
    'siblings' : ["Andy", "Niklas"],
}


# Given an array of dictionaries of names and ages, output an array of people over 18 years old.

student_info = {
'Maddie'   : 14,
'Dylan'    : 13,
'Gabe'     : 14,
'Cameron'  : 17,
'Kate'     : 18,
'Kevin'    : 16,
'Phil'     : 20,
'Lola'     : 22,
'Juan'     : 19,

}

print(all(x > 18 for x in student_info))
