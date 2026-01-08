# OPTCG simulator alt tool
import os
import fnmatch
import cv2

INPUT_DIRECTORY = "Input Directory"
OUTPUT_MASTER_DIRECTORY = "Cards"

EXISTING_SETS = ["OP", "ST", "P", "EB", "PRB"]

SET_NAME_BREAKPOINT = '-'
CARD_NAME_BREAKPOINT = '('
CARD_NAME_POSTFIX = "_OVERRIDE"
OUTPUT_FORMAT = ".png"

OUTPUT_WIDTH = 720 #960
OUTPUT_HEIGHT = 1005 #1340


def main():
    print("Card Processing started.")
    try:
        card_set: str
        card_renamed: str

        for card in os.listdir(INPUT_DIRECTORY):
            print(f"Found {card}")
            card_as_np = cv2.imread((INPUT_DIRECTORY + '/' + card))
            card_resized = resize_image(card_as_np)

            card_set = card.split(SET_NAME_BREAKPOINT)[0]
            card_renamed = card.split(CARD_NAME_BREAKPOINT)[0] + CARD_NAME_POSTFIX + OUTPUT_FORMAT
            output_path = f"{OUTPUT_MASTER_DIRECTORY}/{card_set}/{card_renamed}"

            if not check_set_name(card_set):
                print(f"{card_set} os not a valid set.")
                exit(1)

            check_set_folder(card_set)

            cv2.imwrite(output_path, card_resized)
            print(f"{output_path} exported.")
    except Exception as e:
         print(e)
    print("Card Processing completed.")

def resize_image(image):
    return cv2.resize(image, (OUTPUT_WIDTH, OUTPUT_HEIGHT), interpolation=cv2.INTER_LANCZOS4)

def check_set_folder(card_set):
    existing_sets = os.listdir(OUTPUT_MASTER_DIRECTORY)
    if card_set not in existing_sets:
        os.mkdir(OUTPUT_MASTER_DIRECTORY + '/' + card_set)
        print(f"{card_set} folder created.")
    else: print(f"{card_set} folder already exists.")

def check_set_name(card_set):
    for set_name in EXISTING_SETS:
        if fnmatch.fnmatch(card_set, f"{set_name}*"):
            return True
    return False

if __name__ == '__main__':
    main()

