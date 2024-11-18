import csv

def write_data_to_csv(data):
    name = data.get("name")
    email = data.get("email")
    subject = data.get("subject", "")
    message_content = data.get("message","")

    database_file = "database/db.csv"
    with open(database_file, "a") as csv_writer:
        db_writer = csv.writer(csv_writer, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([name, email, subject, message_content])
