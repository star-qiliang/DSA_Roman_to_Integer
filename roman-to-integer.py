class Solution:
    def romanToInt(self, s: str) -> int:
        power_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900,
        }

        combine_set = set(["IV","IX","XL","XC","CD","CM"])
        stack = ""
        base = 0
        for x in s:

            # print("stack:", stack)
            # print("x:", x)
            # print("base:", base)
            # print("\n")

            if (not stack) and (not x in ("I","X","C")):
                base+=power_dict[x]
            elif stack:
                combine = stack+x

                if combine in combine_set:
                    base+=power_dict[combine]
                    stack = ""

                elif x in ("I","X","C"):
                    base+=power_dict[stack]
                    stack = x
                else:
                    base+=power_dict[stack]
                    base+=power_dict[x]
                    stack = ""

            elif not stack:
                if x in ("I","X","C"):
                    stack+=x
                else:
                    base+=power_dict[x]
            
        if stack:
            base+=power_dict[stack]
    
        return base

            