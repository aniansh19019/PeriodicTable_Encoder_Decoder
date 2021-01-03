# PeriodicTable_Encoder_Decoder
This is a set of two programs that use the mendeleev python library (https://github.com/lmmentel/mendeleev/) to do the following:

1. **string_to_num.py** asks the user for a string and encodes it(if possible) to a sequence of numbers. The numbers are atomic numbers of the chemical element symbols extracted from the input string.

**For example:** if the user enters "SUPER", the program outputs ["16 92 15 68"] where each number corresponds to an element from the periodic table ( [S U P Er] in this case).

2. **num_to_string.py** does the opposite of the first program and encodes a number to a string by converting the atomic numbers extracted from the number to the chemical symbols.

**For example:** if the user enters "1234", the program outputs ['HHeLiBe', 'HHeSe', 'HVBe', 'MgLiBe', 'MgSe']. These are all the possible combinations of elements possible whose atmoic numbers taken in order will give back the original number.

This was just a fun exercise to write a program for something we used to do by pen and paper in our chemistry class in high school.

## Installation

```

git clone https://github.com/aniansh19019/PeriodicTable_Encoder_Decoder
cd PeriodicTable_Encoder_Decoder
virtualenv -p python3 .env
source .env/bin/activate
pip install -r requirements.txt

```
use `python num_to_string.py` and `python string_to_num.py` to run the programs.
