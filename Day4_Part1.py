def passport():
    f = open("data.txt","r")
    count =0
    password =""
    checker =0
    for line in f.readlines():
        password+=line
        if(line=="\n"):
            if("byr:"in password and "iyr:" in password and "eyr:" in password and "hgt:" in password and "hcl:" in password and "ecl:" in password and "pid:" in password):
                count+=1
    print(count)
            
passport()