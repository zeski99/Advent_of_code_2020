print((lambda h: (int(h.real), int(h.imag)))(sum([1 + 1j * (1920<=int(p["byr"])<=2002 and 2010<=int(p["iyr"])<=2020 and 2020<=int(p["eyr"])<=2030 and p["ecl"]in["amb","blu","brn","gry","grn","hzl","oth"] and ((p["hgt"].endswith("cm") and 150<=int(p["hgt"][:-2])<=193) or (p["hgt"].endswith("in")and 59<=int(p["hgt"][:-2])<=76)) and len(p["hcl"]) == 7 and p["hcl"][0] == "#" and all(c in "0123456789abcdef" for c in p["hcl"][1:])and len(p["pid"]) == 9 and all(map(str.isdigit, p["pid"]))) for p in [{k:v for k,v in (x.split(":") for x in d) if k != "cid"} for d in [v.split() for v in open("4").read().split("\n\n")]] if len(p) == 7])))