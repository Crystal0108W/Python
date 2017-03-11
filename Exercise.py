# exercise 1
print ("Hellp World!")
print ("My name is Crystal!") 

print ("I will now count my chickens")

print ("Hens"), 25+30/6
print ("Roosters"), 100 - 25 *3 %4
print ("Now I will count the eggs:")
print (3+2+1-5+4%2 -1/4 + 6)

print ("Is it true that 3+2 < 5-7?")
print ("what is 3 + 2?"), 3+2
print ("What is 5-7?"), 5-7
print ("Oh, that's why it's FALSE")
print ("How about some more?")

print ("Is it greater?"), 5 > -2
print ("Is it greater or equal?"), 5>= -2
print ("Is it less or equal?"), 5 <+ -2

# exercise 2
my_name = "Crystal"
my_age = 24
my_height = 74
my_weight = 180
my_eyes = "brown"
my_teeth = "white"
my_hair = "black"

# exercise 3
print ("Let's talk about %s") % my_name
print ("She's %d inches tall") % my_height
print ("She's %d pounds heacy") % my_weight
print ("Actually that's not too heavy")
print ("She's got %s eyes and %s hair") %(my_eyes, my_hair)
print ("His teeth are usually %s depending on the coffee") %my_teeth
print ("If I add %d, %d and %d I get %d") %(my_age, my_height, my_weight, my_age+my_height+my_weight)

#exercise 4
x = "There are %d types of people" %100
binary = "binary"
do_not = "don't"

y = "Those who knows %s and those who %s." %(binary, do_not)
 
print (x)
print (y)

print ("I said: %r.") %x
print ("I also said: '%s'.") %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 

print (joke_evaluation % hilarious)

w = "This is  the left side of..." 
e = "a string with a right side"

print (w+e)


#exercise 5
print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % "snow")
print ("And everywhere taht Mary went.")
print ("." * 10) #shows 10 dots 

end1 = "C"
end2 = "r"
end3 = "y"
end4 = "s"
end5 = "t"
end6 = "a"
end7 = "l"

end8 = "W"
end9 = "a"
end10 = "n"
end11 = "g"


# put a comma in between two print commands will make the two words in the same line
print (end1 + end2 + end3 + end4 + end5 + end6 + end7) ,
print (end8 + end9 + end10 + end11) 



 
#exercise 6
formatter = "%r %r %r %r"

print (formatter % (1,2,3,4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter %(
		"I had this thing,",
		"That you could type up right",
		"But it didn't sing",
		"So I said goodnight!")) # IF you use the comma inside print command, they will show up as seperate strings 


 
#exercise 6
days = "Mon Tue Wed Thu Tue Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("Here are the days", days)
print ("Here are the months")
print (months)

 
#exercise 7
tabby_cat = "\tI'm tabbed in." 
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food 
\t* Fishies 
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

# \\ Backslash (\)
# \' Single-quote (')
# \" Double-quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only) \r ASCII carriage return (CR)
# \t ASCII horizontal tab (TAB)
# \uxxxx Character with 16-bit hex value xxxx (Unicode only) \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only) \v ASCII vertical tab (VT)
# \ooo Character with octal value oo
# \xhh Character with hex value hh
