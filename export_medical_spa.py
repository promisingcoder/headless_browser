import csv

# Data to be written to the CSV file
data = [
    {"Name": "Melisa Tennant- Willis", "Title": "RN, BSN. Med Spa owner, Master Microblading Artist", "Contact Info": "", "Profile Link": "", "Website": "", "Address": "", "Phone": "", "Email": ""},
    {"Name": "Melissa Pierzchajlo", "Title": "", "Contact Info": "Contact Info", "Profile Link": "linkedin.com/in/melissa-pierzchajlo", "Website": "solemedspa.com", "Address": "", "Phone": "", "Email": ""},
    {"Name": "Angineh Aghamalian", "Title": "Med Spa Owner / Founder / Executive", "Contact Info": "", "Profile Link": "linkedin.com/in/angieaghamalian", "Website": "skincodela.com", "Address": "4214 Beverly Blvd. Suite 202, Los Angeles, CA 90004", "Phone": "213-384-3800", "Email": ""},
    {"Name": "Phyllis Phillips", "Title": "Med spa owner with almost 40 years of experience in cosmetology and massage therapy", "Contact Info": "", "Profile Link": "", "Website": "", "Address": "1345 Kipling St, Eiber, Lakewood, CO, 80215, United States", "Phone": "303-279-6237", "Email": "info@angedelamer.com"},
    {"Name": "Ashley Spiller", "Title": "Medical Spa Owner at SlimRU Wellness & Aesthetics", "Contact Info": "", "Profile Link": "linkedin.com/in/ashley-spiller-b12753230", "Website": "", "Address": "", "Phone": "", "Email": ""},
    {"Name": "Tamara Hefner", "Title": "Owner of Reflection Medical Spa", "Contact Info": "", "Profile Link": "linkedin.com/in/tamara-hefner-39ba7765", "Website": "", "Address": "5311 S Harlem Ave, Suite 100, Chicago, IL 60638", "Phone": "(773) 380-9929", "Email": "info@reflectionsmedspa.com"},
    {"Name": "Romana Mehar", "Title": "Founder & Owner Of SKIN Med Spa & Laser", "Contact Info": "", "Profile Link": "linkedin.com/in/romana-mehar-49409a2b", "Website": "skinmedspas.com", "Address": "8951 Collin McKinney Pkwy Suite 1202, McKinney, TX 75070, United States; 4425 Plano Pkwy Suite 402, Carrollton, TX 75010, United States", "Phone": "(214) 935-9697; (214) 935-9554", "Email": "skinmedspastexas@gmail.com"},
    {"Name": "Audrey Bolema", "Title": "Owner at Raw Rituale Med Spa", "Contact Info": "", "Profile Link": "linkedin.com/in/audreybolema", "Website": "rawrituale.com", "Address": "335 Holly Street, Denver, CO 80220; 8775 E Orchard Rd Suite 814, Greenwood Village, CO 80111", "Phone": "303.229.8292", "Email": "audrey@rawrituale.com"},
    {"Name": "Ronda Hawara-Nofal", "Title": "Founder & Owner of Blue Medi Spa", "Contact Info": "Contact Info", "Profile Link": "linkedin.com/in/ronda-hawara-nofal-43380111", "Website": "BlueSpa.com; RondaNofal.com", "Address": "14622 VENTURA BLVD. #118, SHERMAN OAKS, CA 91403", "Phone": "+1 818-783-3600", "Email": ""},
    {"Name": "Myran Thomas", "Title": "Owner, LA Med Spa Esthetique", "Contact Info": "", "Profile Link": "linkedin.com/in/myran-thomas-85963413", "Website": "laspaesthetique.com; drmichaellin.com", "Address": "11950 San Vicente Boulevard, Suite 110 – Inside Courtyard, Brentwood, CA 90049; 5477 Ventura Blvd, Suite 100, Sherman Oaks, CA 91403; 462 N. Linden Ave, Suite 236, Beverly Hills, CA 90212", "Phone": "(310) 447-3838; (818) 906-6900; (310) 385-8425", "Email": ""}
]

# Writing to CSV file
csv_file = "med_spa_owners.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"CSV file '{csv_file}' created successfully.")
