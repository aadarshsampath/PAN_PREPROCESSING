import csv
import os
import shutil

def loadCsv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    return dataset

def xml_getdata():
    from BeautifulSoup import BeautifulSoup
    import re
    import bs4
    import os
    from stripogram import html2text, html2safehtml
    from os.path import basename
    my_path="C:\\Users\\AadarshSam\\Desktop\\PAN_NEW\\PAN_2016_TWITTER\\Dutch_twitter_texts\\"
    path= "C:\\Users\\AadarshSam\\Desktop\\PAN_NEW\\PAN_2016_TWITTER\\Dutch_twitter_2016\\"

    for filename in os.listdir(path):
        my_list=[]
        s=''
        if not filename.endswith(".xml"):
            continue
        fullname=os.path.join(path,filename)
        doc_el = bs4.BeautifulSoup(open(fullname),'xml')
        my_list.append([ el.text for el in doc_el.findAll('document') ])
        with open(my_path+basename(filename).strip(".xml") +".txt",'wb') as f:
            for item in my_list:
                s= s + str(item)
                soup = BeautifulSoup(s)
                text_parts = soup.findAll(text=True)
                text = ''.join(text_parts)
                f.write("%s\n" % text)


def folderseg(dataset,f):
    count=0
    src="C:\\Users\\AadarshSam\\Desktop\\PAN_NEW\\PAN_2016_TWITTER\\Dutch_twitter_texts\\"
    data_list=list(dataset)
    age1 = []
    age2=[]
    age3=[]
    age4=[]
    age5=[]
    filenames = []
    male=[]
    #for copying female records
    #for copying 18-24
    for i in range(1,len(data_list)):
            if ((data_list[i][2])=='18-24'):
                    path = "C:\Users\AadarshSam\\Desktop\\PAN_AGE_GROUPS\\English\\18-24\\"
                    filename = str(data_list[i][0]) + '.txt'
                    age1.append(filename)


    for filename in age1:
        full_file_name = os.path.join(src, filename)
        shutil.copy(full_file_name, path)

# for copying 25-34

    for i in range(1,len(data_list)):
            if ((data_list[i][2])=='25-34'):
                    path = "C:\Users\AadarshSam\\Desktop\\PAN_AGE_GROUPS\\English\\25-34\\"
                    filename_2 = str(data_list[i][0]) + '.txt'
                    age2.append(filename_2)

    for filename_2 in age2:
        full_file_name_age2 = os.path.join(src, filename_2)
        shutil.copy(full_file_name_age2, path)

# for copying 35-49
    for i in range(1,len(data_list)):
            if ((data_list[i][2])=='35-49'):
                    path = "C:\Users\AadarshSam\\Desktop\\PAN_AGE_GROUPS\\English\\35-49\\"
                    filename_3 = str(data_list[i][0]) + '.txt'
                    age3.append(filename_3)

    for filename_3 in age3:
        full_file_name_age3 = os.path.join(src, filename_3)
        shutil.copy(full_file_name_age3, path)

#for copying 50-XX

    for i in range(1,len(data_list)):
            if ((data_list[i][2])=='50-64'):
                    path = "C:\Users\AadarshSam\\Desktop\\PAN_AGE_GROUPS\\English\\50-64\\"
                    filename_4 = str(data_list[i][0]) + '.txt'
                    age4.append(filename_4)

    for filename_4 in age4:
        full_file_name_age4 = os.path.join(src, filename_4)
        shutil.copy(full_file_name_age4, path)
#for copying 65-xx
    for i in range(1,len(data_list)):
            if ((data_list[i][2])=='65-xx'):
                    path = "C:\Users\AadarshSam\\Desktop\\PAN_AGE_GROUPS\\English\\65-xx\\"
                    filename_5 = str(data_list[i][0]) + '.txt'
                    age5.append(filename_5)

    for filename_5 in age5:
        full_file_name_age5 = os.path.join(src, filename_5)
        shutil.copy(full_file_name_age5, path)




    for i in range(1,len(data_list)):

            if ((data_list[i][1])=='FEMALE'):
                    path = "C:\\Users\\AadarshSam\\Desktop\\PAN_NEW\\PAN_2016_TWITTER\\Dutch_Female_twitter_2016\\"
                    filename = str(data_list[i][0]) + '.txt'
                    filenames.append(filename)


    for filename in filenames:
        full_file_name = os.path.join(src, filename)
        shutil.copy(full_file_name, path)

# for copying male records

    for i in range(1,len(data_list)):
            if ((data_list[i][1])=='MALE'):
                    path = "C:\\Users\\AadarshSam\\Desktop\\PAN_NEW\\PAN_2016_TWITTER\\Dutch_Male_twitter_2016\\"
                    filename_male = str(data_list[i][0]) + '.txt'
                    male.append(filename_male)

    for filename_male in male:
        full_file_name_male = os.path.join(src, filename_male)
        shutil.copy(full_file_name_male, path)


def main():
    f = []
    filename='C:\\Users\\AadarshSam\\Desktop\\PAN_NEW\\PAN_2016_TWITTER\\dutch_twitter_truth_2016.csv'
    xml_getdata()
    print "xml is done"
    dataset = loadCsv(filename)
    print "dataset is done"
    folderseg(dataset,f)
    print "process is done"
main()