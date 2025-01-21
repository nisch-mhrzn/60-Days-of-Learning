import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
urls = ["https://github.com/nisch-mhrzn", "https://www.linkedin.com/in/nischalm1/"]
logos = ["git.png", "linked.png"]

for i, (url, logo_path) in enumerate(zip(urls, logos)):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="white")
    
    logo = Image.open(logo_path)
    # Ensure logo has an alpha channel
    logo = logo.convert("RGBA")
    # Calculate the size for the logo
    logo_width, logo_height = logo.size
    qr_width, qr_height = img.size
    factor = 4
    size_w = qr_width // factor
    size_h = qr_height // factor
    # Resize the logo
    logo = logo.resize((size_w, size_h), Image.LANCZOS)

    # Calculate the position for the logo
    pos_w = (qr_width - size_w) // 2
    pos_h = (qr_height - size_h) // 2
    # Create a mask for transparency
    mask = logo.split()[3]  # Use alpha channel as mask

    # Paste the logo onto the QR code
    img = img.convert("RGBA")  # Ensure the QR code image is in RGBA mode
    img.paste(logo, (pos_w, pos_h), mask)

    # Save the final image
    img.save(f"Nisch-Profile-{i}.png")
