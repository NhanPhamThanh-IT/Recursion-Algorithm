# Python3 program using to convert the given decimal number into an equivalent binary number. 

# Recursive function
def convertDecToBin(dec : int) -> int:
    if dec == 0:
        return 0
    return (dec % 2 + 10 * convertDecToBin(int(dec // 2)))

# Main
if __name__ == "__main__":
    dec = 10
    print(f'Convert {dec} to binary: {convertDecToBin(dec)}')