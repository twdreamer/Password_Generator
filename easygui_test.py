import easygui
msg = "Enter your personal information"
title = "Credit Card Application"
fieldNames = ["Name","Street Address","City","State","ZipCode"]
fieldValues = []  # we start with blanks for the values
fieldValues = easygui.multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues is None: break
    errmsg = ""
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "":
        break # no problems found
    fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)

print("Reply was: %s" % str(fieldValues))