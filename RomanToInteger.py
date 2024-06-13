class Solution:
    '''
    Understand: Turn number into Roman numeral, exception that 4 and 9 are written differently,
    Match: Mapping with the roman numberal to numbers
    Implement:
    Review 
    Evaluate
    '''
    def romanToInt(self, s: str) -> int:
        romanToNum = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        value = 0
        for index in range(0, len(s)-1):
            num1 = s[index]
            num2 = s[index+1]

            if romanToNum[num1] < romanToNum[num2]:
                value = value - romanToNum[num1]
            else:
                value = value + romanToNum[num1]
        
        value += romanToNum[s[len(s)-1]]
        return value

        