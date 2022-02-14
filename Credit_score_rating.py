def credit_score(score):
    s = ""

    if(score > 850):
        s = "Outside of range"
# Your code starts after this line

    elif(score >= 300 and score <= 579):
        s = "Poor"
    elif(score >= 580 and score <= 669):
        s = "Fair"
    elif(score >= 670 and score <= 739):
        s = "Good"
    elif(score >= 740 and score <= 799):
        s = "Very Good"
    elif(score >= 800 and score <= 850):
        s = "Exceptional"




# Your code ends before this line
    else:
        s = "Outside of range"

    return s  