def find_n_last_pattern(n,text,pattern):
    '''
This function use to find the n th last occurance with pattern
n : n time last pattern WITH n = 1 is the last time
text : text to find
pattern: pattern need to be found in the text
'''
    if (n == 1):
        return text.rfind(pattern)
    else:
        i = 1
        temp_text = text
        while i < n:
            print (temp_text, ": before")
            temp_text = temp_text[:temp_text.rfind(pattern)]
            print (temp_text, ": after")
            i += 1
        return temp_text.rfind(pattern)