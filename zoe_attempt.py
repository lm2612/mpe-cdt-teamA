# import csv

# with open('../Correct_loss_data/Region_1_DR.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('../Correct_loss_data/Region_1_DR.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         mydict = {rows[0]:rows[1] for rows in reader}

import pandas as pd

Region_1_DR=pd.read_csv('../AIR_data/Correct_loss_data/Region_1_DR.csv')


print(len(Region_1_DR.AIRSID.unique()))
print((Region_1_DR.AIRSID.unique()))

unique_arsid=Region_1_DR.AIRSID.unique()
for air_id in unique_arsid :
	print(air_id, Region_1_DR.loc[Region_1_DR['AIRSID']==air_id, 'LOB1' ].mean())
		

# print(len(Region_1_DR.AIRSID))
# means = []
# for air_id in Region_1_DR.AIRSID :
# 	if air_id not in means[:,0]:
# 		print(air_id, Region_1_DR.loc[Region_1_DR['AIRSID']==air_id, 'LOB1' ].mean())
# 		mean.append([air_id, Region_1_DR.loc[Region_1_DR['AIRSID']==air_id, 'LOB1' ].mean()])

print(Region_1_DR.loc[Region_1_DR['AIRSID']==10660, 'LOB1' ].sum())
print(Region_1_DR.loc[Region_1_DR['AIRSID']==10660, 'LOB1' ].mean())

# import csv
# with open('../AIR_data/Correct_loss_data/Region_1_DR.csv') as csvfile: #cauging python to automatically close and clean up the file outside the block
#      reader = csv.DictReader(csvfile)
#      for row in reader:
#      	Region_1_DR['AIRSID']=row['AIRSID']
#      	if row['AIRSID'] not in 
#          print(row['AIRSID'], row['EventID'])


#  with open('../AIR_data/Correct_loss_data/Region_1_DR.csv', 'w') as csvfile:
#     fieldnames = ['AIRSID', 'LOB1']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
