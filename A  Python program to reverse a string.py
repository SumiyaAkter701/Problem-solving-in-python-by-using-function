# Write a Python program to reverse a string.
string = input("Enter a string value: ")

def reverseing_string(srt_05):
    reverse_str = " "
    srt_05_len = len(srt_05)
    while srt_05_len > 0:
        reverse_str +=srt_05[srt_05_len-1] 
        srt_05_len -=1
    return reverse_str
print (reverseing_string(string))
