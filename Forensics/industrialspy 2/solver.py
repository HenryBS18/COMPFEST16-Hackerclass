import re

keys = {
  "02": "SHIFT",
  "04": "aA",
  "05": "bB",
  "06": "cC",
  "07": "dD",
  "08": "eE",
  "09": "fF",
  "0a": "gG",
  "0b": "hH",
  "0c": "iI",
  "0d": "jJ",
  "0e": "kK",
  "0f": "lL",
  "10": "mM",
  "11": "nN",
  "12": "oO",
  "13": "pP",
  "14": "qQ",
  "15": "rR",
  "16": "sS",
  "17": "tT",
  "18": "uU",
  "19": "vV",
  "1a": "wW",
  "1b": "xX",
  "1c": "yY",
  "1d": "zZ",
  "1e": "1!",
  "1f": "2@",
  "20": "3#",
  "21": "4$",
  "22": "5%",
  "23": "6^",
  "24": "7&",
  "25": "8*",
  "26": "9(",
  "27":"0)",
  "2a":"DELETE",
  "2d": "-_",
  "2f": "[{",
  "30": "]}",
  "2c": " "
}

flag = ""

filename = 'res.txt' 

with open(filename, "r") as f:
  data = f.readline()
  while data:
    data = f.readline()
    res = re.findall("..", data)
    
    if len(res) > 2:
      if res[2] in keys:
        if res[2] == "2a": #delete - remove the last character
          flag = flag[:-1]
        else:
          if res[0] == "02": #shift - take upper case
            flag +=keys[res[2]][1]
          else: # take lower case
            flag += keys[res[2]][0]

print(flag)