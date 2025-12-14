import ReadBarcodeBatch as a
from character import Character
from character_database import CharacterDatabase


def main():
    pBBar  = []
    # folder = input("Enter folder path containing barcode images: ").strip()
    folder = 'source'
    pBBar = a.read_barcodes_from_folder(folder)
    # print(pBBar)
    for row in pBBar:
        # print(f"Index:{row[0]}")
        # print(f"Barcode Type:{row[1]}")
        # print(f"Barcode Text:{row[2]}")
        # print(f"Barcode Hash:{row[3]}")
        db = CharacterDatabase()
        cDB = Character(row[2],row[3])
        cid = db.get_or_create(cDB)

# -------- MAIN --------
if __name__ == "__main__":
    main()
