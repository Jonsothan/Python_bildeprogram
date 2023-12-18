from PIL import Image, ImageOps, ImageFont, ImageDraw # Importer image fra pillow
import pilgram 

valg = input("Hva vil du? (filter/roter/resize/tekst/polaroid) ")

with Image.open("./skog.jpg") as img:
    if valg == "filter":
        pilgram.willow(img).show()
    elif valg == "roter":
        img.rotate(180).show()
    elif valg == "resize":
        # Endre størrelse på bilde slik at den har minimum bredde på 1080
        img = ImageOps.contain(img, (1080, 1080))
        img.show()
    elif valg == "tekst":
        tekst = input("Hva vil du skrive?: ")
        font = ImageFont.truetype("Lato-Regular.ttf", 30)
        ImageDraw.Draw(
            img
        ).text(
            (img.width/2, img.height/2),
            tekst,
            (255,255,255),
            font=font,
        )
        img.show()
    elif valg == "polaroid":
        # Endre størrelse på bildet
        img.resize((1080, 1080), Image.LANCZOS)

        # Åpne ramma som bilde
        ramme = Image.open("polaroid-frame-PNG-5.png")

        # Manuel skalering av bilde 
        cropped = img.resize((img.width + 203, img.height + 447))
        # Lim inn bildet i rammen, og putt på filter på bildet
        ramme.paste(pilgram._1977(cropped), (61, 61))

        # Lagre bilde som "bilde.jpg_polaroid.jpg"
        ramme.save(img.filename + "_polaroid." + ramme.format.lower())
    else:
        print("Feil")