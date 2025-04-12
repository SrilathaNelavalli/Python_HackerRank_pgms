def imagecopy():
    try:
        with open("C:\\Users\\srinu\\OneDrive\\Documents\\AWS\\images\\a2.jpg","rb") as sp:
            with open("pt1.jpg","wb") as dp:
                srcimage=sp.read()
                dp.write(srcimage)
        print("the image copied successfully")
    except FileNotFoundError:
        print("file doesn't exist")
imagecopy()