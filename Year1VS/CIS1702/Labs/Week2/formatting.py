name, course, lang, movie = "Rosie", "CompSci", "Python", "Megamind"
randNum = 14.98718972419412

# Concatonation
print("Hi, I'm " + name + " and I like the movie " + movie + ".")

# Format method
print("Hi, I'm {fname} and I'm studying {fcourse}.".format(fname = name, fcourse = course))

# F-String
print(f"Hi, I'm {name} and I like {lang}.")

# Precision Formatting
print(f"Here is a random number: {randNum:.5f}. Here it is again: {randNum:e}.")