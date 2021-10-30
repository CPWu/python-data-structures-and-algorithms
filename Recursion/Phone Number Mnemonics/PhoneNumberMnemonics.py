# O(4^n * n) time | O(4^n * n) space - where n is the length of the phone number
def phoneNumberMnemonics(phoneNumber):
    currentMnemonic = [0] * len(phoneNumber)
    mnemonicsFound = []

    phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonic, mnemonicsFound)

    return mnemonicsFound

def phoneNumberMnemonicsHelper(index, phoneNumber, currentMnemonic, mnemonicsFound):
    if index == len(phoneNumber):
        mnemonic = "" .join(currentMnemonic)
        mnemonicsFound.append(mnemonic)
    else:
        digit = phoneNumber[index]
        letters = DIGIT_LETTERS[digit]
        for letter in letters:
            currentMnemonic[index] = letter
            phoneNumberMnemonicsHelper(index + 1, phoneNumber, currentMnemonic, mnemonicsFound)

DIGIT_LETTERS = {
    "0": ["0"], 
    "1": ["1"], 
    "2": ["a","b","c"],
    "3": ["d","e","f"],
    "4": ["g","h","i"],
    "5": ["j","k","l"],
    "6": ["m","n","o"],
    "7": ["p","q","r","s"],
    "8": ["t","u","v"], 
    "9": ["w","x","y","z"],  
}

phoneNumber = "1905"

print(phoneNumberMnemonics(phoneNumber))