
from .utils import get_files_from_folder, check_all_template, convert_symbols

def main():
    print("####################################")
    print("########## KOODU CHECKERS ##########")
    print("####################################")
    templates = get_files_from_folder()
    valids = check_all_template(templates)
    symbols = convert_symbols(valids)
    
    for (path, status) in zip(templates, symbols):
        print(path, status)

if __name__ == "__main__":
    main()