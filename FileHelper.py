import csv
import random


def CutDownCsv():
    cutdown_line_csv_list = []
    with open(r'C:\Users\vi1290\Downloads\GCP Learning Data Pipeline project\flipkart_com-ecommerce_sample.csv',
              newline='', encoding='UTF8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in file_reader:
            try:
                cutdown_line_csv_list.append(row[1] + "," +
                                             row[3] + "," +
                                             random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]) + "," +
                                             row[6]
                                             )
            except IndexError as ie:
                pass

    cutdown_file = open(r'C:\Users\vi1290\Downloads\GCP Learning Data Pipeline project\flipkart_sales_list.csv', 'w+',
                        encoding='UTF8')
    cutdown_file.write("\n".join(cutdown_line_csv_list))

    csvfile.close()
    cutdown_file.close()


if __name__ == "__main__":
    CutDownCsv()
