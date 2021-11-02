import csv

# list.csvの中にdev_t1.csvの中にないものをprint
def existenceJudge(keyword):
    design_t = 'list.csv'
    with open(design_t, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if(keyword in row[1]):
                resoult = 'Ok'
                break
            else:
                resoult = keyword+','
        return resoult

dev_t = 'dev_t1.csv'
with open(dev_t, encoding='utf8', newline='') as dev:
    csvreader_dev = csv.reader(dev)
    for row in csvreader_dev:
        resoult = existenceJudge(row[3])
        print(resoult)

