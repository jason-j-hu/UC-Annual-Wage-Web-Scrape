
if __name__ == "__main__":
    for pgNum in range(-2, 15515+3):
        try:
            with open("pg" + str(pgNum) + ".json") as f:
                pass
        except IOError:
            print("File not accessible: " + str(pgNum))
