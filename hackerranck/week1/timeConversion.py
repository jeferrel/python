def timeConversion(s):
    # Write your code here
    letter = s[len(s) - 2]
    hour = int(s[:2])
    result = ""
    if letter == 'P':
        if hour < 12:
            hour += 12
            result = str(hour)
        else:
            result = str(hour)
    else:
        if hour == 12:
            result = "00"
        elif hour < 10:
            result = "0" + str(hour)
        else:
            result = str(hour)
    result += s[2:-2]
    return result

result = timeConversion("07:05:45PM")
print(result)
