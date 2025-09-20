import os
import shutil

# Daftar tamu undangan dengan format tampilan yang diinginkan
guest_list = [
    "Mrs. Yuna Bella",
    "Mrs. Novinda",
    "Mrs. Galuh",
    "Mrs. Jesika",
    "Mrs. Alyta",
    "Mbak Ela Widya",
    "Nida Nur Azizah",
    "Mrs. Selvi",
    "Mrs. Afifah",
    "Mrs. Pamela",
    "Mrs. Azza Zein",
    "Mrs. Nikita",
    "Mrs. Evi",
    "Mbak Nova",
    "Mbak Whenes",
    "Mbak Tahta",
    "Mrs. Anggun",
    "Mrs. Indah",
    "Mbak Elok",
    "Mr. Aji",
    "Mr. Ricki",
    "Mrs. Syan",
    "Mrs. Mayang",
    "Mr. Hamzah",
    "Mr. Ali Muttaqin",
    "Mr. Irfan",
    "Mrs. Bella",
    "Mrs. Ina Indah",
    "Bu Nia",
    "Mrs. Nindi",
    "Mrs. Putri Maharani",
    "Eko",
    "Mas Fikri",
    "Mbak Miftah",
    "Mrs. Nikita"
]

def create_filename(name):
    # Membuat filename yang aman untuk URL
    # Menghapus spasi berlebih dan mengubah ke lowercase
    # Mengganti titik dengan tanda hubung
    filename = name.strip().lower()
    filename = filename.replace('.', '-')  # Mengganti titik dengan tanda hubung
    filename = filename.replace(' ', '-')  # Mengganti spasi dengan tanda hubung
    # Menghapus tanda hubung ganda jika ada
    while '--' in filename:
        filename = filename.replace('--', '-')
    return filename

def create_invitation(guest_name):
    # Baca template HTML
    with open('index.html', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Ganti data-guest
    content = content.replace('data-guest="Bhasri*"', f'data-guest="{guest_name}"')
    
    # Ganti id="guestNameSlot"
    content = content.replace('>Tamu Undangan<', f'>{guest_name}<')
    
    # Perbaiki semua href di lightbox
    base_url = "https://brahmasyahdan.github.io/undangan-pernikahan"
    filename = f'{guest_name.lower()}.html'
    full_url = f"{base_url}/{filename}"
    
    # Ganti href di lightbox dengan #
    content = content.replace('href="athia-aga%3Fto=Bhasri*.html#"', 'href="#"')
    
    # Ganti nama di modal QR (jika ada)
    content = content.replace('>Bhasri*<', f'>{guest_name}<')
    
    # Buat file baru untuk tamu dengan nama file yang aman
    output_filename = f'{create_filename(guest_name)}.html'
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f'Created invitation for {guest_name}: {output_filename}')
    print(f'Link: https://brahmasyahdan.github.io/undangan-pernikahan/{output_filename}')

def main():
    print("Generating invitations...")
    for guest in guest_list:
        create_invitation(guest)
    print("\nDone! All invitations have been created.")
    
    # Membuat pesan WhatsApp yang bisa dicopy
    print("\nFormat pesan untuk WhatsApp:")
    print("----------------------------")
    for guest in guest_list:
        filename = create_filename(guest)
        
        message = (
            f"Assalamu’alaikum warahmatullahi wabarakatuh {guest} 🙏😊\n"
            f"Bismillahirrahmanirrahim 🕌\n"
            f"Alhamdulillah, dengan izin Allah SWT kami akan menempuh jalan baru dalam hidup kami 💍✨\n"
            f"Dengan rendah hati kami mengundang {guest} untuk hadir dan memohon doa restu pada hari bahagia kami 🤲😊\n\n"
            f"Link undangan digitalnya ada di bawah ini ya ⬇️\n"
            f"https://brahmasyahdan.github.io/undangan-pernikahan/{filename}.html\n\n"
            f"Barakallahu laka wa baraka ‘alaika wa jama‘a bainakuma fii khair 🤲✨ "
            f"Semoga Allah memberkahi kami, {guest}, dan menyatukan kita dalam kebaikan 🌸\n\n"
            f"Wassalamu’alaikum warahmatullahi wabarakatuh 🙏😊"
        )
        
        print(f"\nUntuk {guest}:")
        print(message)
        print("----------------------------")


if __name__ == "__main__":
    main()