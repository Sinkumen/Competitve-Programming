class Solution(object):
    def numberToWords(self, num: int) -> str:
        ones: dict = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        teens: dict = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
        }
        tens: dict = {
            #1: 'Ten',
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        prefix: dict ={
            6: 'Thousand',
            9: 'Million',
            12: 'Billion'
        }

        out1:str = str()
        first:bool = False
        pref_1: int = 3
        num_s: str = str(num)

        # Extracted digits translator
        def translate(num_s:str):   
            output: str = str()
            if len(num_s) == 3:
                if int(num_s[0]) in ones:
                    output = ones[int(num_s[0])] + ' Hundred '
                if num_s[1] == '0' and int(num_s[2]) in ones:
                    output += ones[int(num_s[2])]
                elif int(num_s[1]) in tens and num_s[2] == '0':
                    output += tens[int(num_s[1])]
                if int(num_s[1:]) in teens:
                    output += teens[int(num_s[1:])]
                elif int(num_s[1]) in tens and int(num_s[2]) in ones:
                    output += tens[int(num_s[1])] + ' ' + ones[int(num_s[2])]   
            elif len(num_s) == 2:
                if int(num_s) in teens:
                    output = teens[int(num_s)]
                elif int(num_s[0]) in tens and num_s[1]=='0':
                    output = tens[int(num_s[0])]
                elif int(num_s[0]) in tens and int(num_s[1]) in ones:
                    output = tens[int(num_s[0])] + ' ' + ones[int(num_s[1])]
            elif len(num_s) == 1:
                if num_s == '0':
                    output = 'Zero'
                elif int(num_s) in ones: 
                    output = ones[int(num_s)]
            return output.strip()

        for i in num_s:
            if bool(int(num_s)) == False:
                num_s = '0'
                break
            elif bool(num_s) == True:
                if i == '0':
                    num_s = num_s[((num_s.index('0'))+1):]
                else:
                    break

        while len(num_s) > 0:
            if first == False:
                if len(num_s) >= 3:
                    out1 = translate(num_s[-3:])
                    num_s = num_s[-(len(num_s)): -3] 
                elif len(num_s)<3:
                    out1 = translate(num_s)
                    break
                first = True
            elif len(num_s) >= 3:       
                if int(num_s[-3:]) == False:
                    num_s = num_s[-(len(num_s)): -3]
                    pref_1+=3
                    continue
                else:
                    out1 = f'{translate(num_s[-3:]) + " " + prefix[pref_1]} ' + out1
                    num_s = num_s[-(len(num_s)): -3]
            elif len(num_s) < 3:
                num_s = num_s[-(len(num_s)):]
                out1 = f'{translate(num_s) + " " + prefix[pref_1]} ' + out1
                break
            pref_1 += 3
        
        return out1.strip()
