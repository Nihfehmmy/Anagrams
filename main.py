# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
        str1 = "Race"
        str2 = "Care"

        # convert both the strings into lowercase
        str1 = str1.lower()
        str2 = str2.lower()
        # check if length is same
        if(len(str1) == len(str2)):

            # sort the strings
            sorted_str1 = sorted(str1)
            sorted_str2 = sorted(str2)

        # if sorted char arrays are same
            if(sorted_str1 == sorted_str2):
                print(str1 + " and " + str2 + " are anagram.")
            else:
                print(str1 + " and " + str2 + " are not anagram.")
        return True
        
find_anagram('race','care')
