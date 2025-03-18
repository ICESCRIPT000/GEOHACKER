import requests
import time
import os
from pystyle import Write, Colors, System, Box

# Banner for the tool
def display_banner():
    banner = """
    ███████╗ █████╗ ██████╗ 
    ██╔════╝██╔══██╗██╔══██╗
    █████╗  ███████║██████╔╝
    ██╔══╝  ██╔══██║██╔══██╗
    ██║     ██║  ██║██║  ██║
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝
    ფეისბუკის ინფორმაცის ძებნა
    """
    Write.Print(Box.Lines(banner), Colors.purple_to_blue, interval=0.001)
    Write.Print("\nშექმნილია GEOHACKER\n", Colors.rainbow, interval=0.005)
    time.sleep(1)

# Function to search for Facebook profiles
def search_facebook_profile(name):
    url = f"https://www.facebook.com/{name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            Write.Print(f"\n[+] {url} - აქუნთი ნაპოვნია", Colors.green, interval=0.005)
            return url
        elif response.status_code == 404:
            Write.Print(f"\n[-] {url} - აქუნთი არა ნაპოვნი", Colors.red, interval=0.005)
        else:
            Write.Print(f"\n[!] {url} - ერორი {response.status_code}", Colors.yellow, interval=0.005)
    except Exception as e:
        Write.Print(f"\n[!] {url} - ერორი შემოწმების დროს: {e}", Colors.red, interval=0.005)
    return None

# Function to provide a tutorial on how to identify the correct account
def tutorial():
    Write.Print("\n\n[+] ტუტორიალი როგორ მოვიგცე თუ ვერ ვპოულობ აქაუნთს:\n", Colors.blue, interval=0.005)
    steps = [
        "1. თუ ბევრი ფეისბუკ აქუნთი იპოვა და არ იცი რომელია, შეადარე სახე თუ გაქ.",
        "2. თუ არ გაქვს სახე დადებული, გადადი მეგობრებთან და შეამოწმე თუ მეგობრებს აქვთ მონიშული 100% სახეც იქნება",
        "3. თუ 100% სახე გექნება შეგიძლია დედა იპოვო",
        "4. თუ დედა იპოვე და სახე ვერა დედას ექნწბა დაბადების დღის ფოტო ან რამე ეგეთი და იშოვი სახეს",
        "5. და ცადე პოვნა ტიკტოკის რო ჩაწერ სახელს და გვარს ფისბუკის ფოტოთი შეადარე"
    ]
    for step in steps:
        Write.Print(f"\n{step}", Colors.cyan, interval=0.005)
    time.sleep(2)
    input("\nდააჭირეთ Enter რო მენიუში გადახვიდეთ...")
    System.Clear()
    display_banner()

# Main function to run the tool
def main():
    System.Clear()
    display_banner()
    
    while True:
        Write.Print("\n[+] აირჩიეთ ფუნქცია:\n", Colors.purple, interval=0.005)
        options = [
            "1. ძებნა ფეისბუკით სახელით და გვარით",
            "2. ტუტორიალი როგორ მოვიგცე თუ ვერ ვიპოვე აქუნთი ფეისბუკით",
            "3. გამოსვლა"
        ]
        for option in options:
            Write.Print(f"\n{option}", Colors.blue, interval=0.005)
        
        choice = input("\nფუნქცია აირჩიეთ --> ")
        
        if choice == "1":
            name = input("\nშეიყვანეთ სახელი და გვარი (მაგ., გიორგი მელანაშვილი): ")
            Write.Print(f"\n[+] მოძებნა: {name}", Colors.green, interval=0.005)
            profile_url = search_facebook_profile(name.replace(" ", "."))  # Replace spaces with dots for URL
            if profile_url:
                Write.Print(f"\n[+] აქუნთი ნაპოვნია: {profile_url}", Colors.green, interval=0.005)
            input("\nდააჭირეთ Enter რო მენიუში გადახვიდეთ...")
            System.Clear()
            display_banner()
        elif choice == "2":
            tutorial()
        elif choice == "3":
            Write.Print("\n[-] გამოსვლა...", Colors.red, interval=0.005)
            break
        else:
            Write.Print("\n[!] არასწორი არჩევანი, გთხოვთ სცადოთ ხელახლა.", Colors.yellow, interval=0.005)

# Run the tool
if __name__ == "__main__":
    main()
