import csv

# Data for each person
data = [
    {
        "Name": "Susan L Ward",
        "Company": "Law Offices of Susan L Ward",
        "LinkedIn Profile": "linkedin.com/in/susanlward",
        "Website": "stlfamilylaw.com",
        "Phone": "(314) 783-9400",
        "Address": "2652 Melvin Avenue, Brentwood, MO 63144",
        "Email": "sward@stlfamilylaw.com",
    },
    {
        "Name": "Jan A. Meyer, Esq.",
        "Company": "Experienced in the areas of trusts and estates, trust administration and probates",
        "LinkedIn Profile": "linkedin.com/in/meyeresqfamilyprotection",
        "Website": "danapointwills.com",
        "Phone": "(949) 607-9412",
        "Fax": "(949) 340-2033",
        "Address": "32776 Sail Way Dana Point, CA 92629",
        "Email": "jan@danapointwills.com",
    },
    {
        "Name": "Edward Kelleher",
        "Company": "Business Owner at Law Off. Edward J Kelleher",
        "LinkedIn Profile": "linkedin.com/in/edward-kelleher-0207b63a",
        "Website": "kelleherlegalteam.com",
        "Address": "57 North Street Suite 405, Danbury, CT 06810",
        "Email": "EKelleher@KelleherLegalTeam.com",
        "Phone": "203-270-6801",
        "Fax": "203-486-8042",
    },
    {
        "Name": "Yaacov Brisman",
        "Company": "Owner at Brisman Law Firm P.C.",
        "LinkedIn Profile": "linkedin.com/in/yaacov-brisman-8a66245",
        "Website": "brismanlaw.com",
    },
    {
        "Name": "Gerard Marino",
        "Company": "Owner/Attorney, Marino & Marino, P.C.",
        "LinkedIn Profile": "linkedin.com/in/gerard-marino-5242327",
        "Website": "marinolawyers.com",
        "Address": "23 Shore Road, Winchester, MA 01890",
        "Phone": "781-721-9500",
        "Fax": "781-721-9501",
    },
    {
        "Name": "Thomas Young",
        "Company": "Owner at Law Office of Thomas Young, PC",
        "LinkedIn Profile": "linkedin.com/in/thomas-young-83a53197",
        "Website": "thomasyounglaw.com",
        "Address": "1776 S. Jackson Street, Suite 402, Denver, CO 80210",
        "Email": "thomasyounglawoffice@gmail.com",
        "Phone": "(303) 756-9419",
        "Fax": "(303) 692-9049",
    },
    {
        "Name": "Kenneth L. Sheppard, Jr.",
        "Company": "Sheppard Law Offices, Co., L.P.A.",
        "LinkedIn Profile": "linkedin.com/in/ohio-attorney-ken-sheppard-jr",
        "Website": "sheppardlawoffices.com",
        "Address": "8351 N. High Street, Ste. 101, Columbus, OH 43235",
        "Phone": "866-770-2190",
    },
    {
        "Name": "Hope R. Jay, MSW, JD",
        "Company": "Business Owner at The Law Office of Hope R. Jay",
        "LinkedIn Profile": "linkedin.com/in/hope-r-jay-msw-jd-4392958",
        "Website": "hopejaylaw.com",
        "Address": "415 Franklin Street, Buffalo, NY 14202",
        "Email": "hope@hopejaylaw.com",
        "Phone": "716.856.6300",
        "Fax": "716.853.6506",
    },
    {
        "Name": "Charles Shaw",
        "Company": "Owner at Law Offices of Charles Regan Shaw PLC",
        "LinkedIn Profile": "linkedin.com/in/charles-shaw-73b22a10",
    },
    {
        "Name": "Douglas Funkhouser",
        "Company": "Owner, Douglas A. Funkhouser Co., L.P.A.",
        "LinkedIn Profile": "linkedin.com/in/douglasfunkhouser",
        "Website": "funkhouserlaw.com",
        "Phone": "(614) 756-2154",
        "Address": "765 S. High Street, Columbus, OH 43206",
    },
    {
        "Name": "Gary Massey",
        "Company": "Chattanooga Personal Injury Attorney",
        "LinkedIn Profile": "linkedin.com/in/garymasseyjr",
        "Website": "masseyattorneys.com",
        "Address": "6400 Lee Highway, Suite 101, Chattanooga, TN 37421",
        "Phone": "(423) 697-4529",
        "Fax": "(423) 634-8886",
    }
]

# CSV file name
csv_file = "lawyers_info.csv"

# Field names for the CSV
fieldnames = ["Name", "Company", "LinkedIn Profile", "Website", "Address", "Phone", "Fax", "Email"]

# Write the data to a CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for person in data:
        writer.writerow(person)

print(f"Data has been written to {csv_file}")
