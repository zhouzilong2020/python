import pandas as pd 
import numpy as np 
from pandas import DataFrame



class Data_read():
	"""docstring for Data_read"""
	def __init__(self, data_name):
		self.data_name = data_name
	
	def Data_clean(self):
		data = pd.read_excel(self.data_name)
		df1 = data['精度'].values
		df3 = data['PCI'].values
		n = 0
		for i,j in zip(df1,df3):
			if i > 5 or j == 0 :
				data = data.drop(n)
			n += 1
		df2 = data['DBM'].values
		for i,n in zip(df2,data.index):
			if i < -110:
				data = data.drop(n)

		data = data.drop_duplicates(['PCI','精度','纬度'])

		df_location_list = []
		df_PCI_list = []
		df_ASU_list = []

		data1 = data.drop_duplicates(['经度','纬度'])
		column1 = data1['经度'].values
		column2 = data1['纬度'].values
		for a,b in zip(column1,column2):
			df_location_list.append([a,b])

		column1= data['经度'].values
		column2 = data['纬度'].values
		column3 = data['PCI'].values
		column4 = data['AsuLevel'].values
		list1 = [column3[0]]
		list2 = [column4[0]]
		x = 1
		while x < len(column1):
			if (column1[x] == column1[x-1]) & (column2[x] == column2[x-1]):
				list1.append(column3[x])
				list2.append(column4[x])
			else:
				df_PCI_list.append(list1)
				df_ASU_list.append(list2)
				list1=[column3[x]]
				list2=[column4[x]]
			x += 1
		df_PCI_list.append(list1)
		df_ASU_list.append(list2)
		self.df_location_list = df_location_list
		self.df_PCI_list = df_PCI_list
		self.df_ASU_list = df_ASU_list

		return (df_PCI_list,df_ASU_list,df_location_list)
	def Data_handle(self,PCI,ASU):
		ASU_dis = []
		for pci_points,asu_points in zip(self.df_PCI_list,self.df_ASU_list):
			asu_diss = 0
			for x,y in zip(pci_points,asu_points):
				if x not in PCI:
					asu_diss += abs(y)
			for pci_point_u,asu_point_u in zip(PCI,ASU):

				if pci_point_u in pci_points:
					for x,y in zip(pci_points,asu_points):
						if pci_point_u == x:
							dis = abs(y - asu_point_u)
							asu_diss += dis
							break
						else:
							continue
				else:
					dis = abs(asu_point_u)
					asu_diss += dis

			ASU_dis.append(asu_diss)
		self.ASU_dis = ASU_dis
#		print(ASU_dis)

	def Locat_asu(self):
		ASU_sorted=[]
		Locat_sorted=[]
		for a,b in zip(self.ASU_dis,self.df_location_list):
			if ASU_sorted:
				for x in range(len(ASU_sorted)):
					if a <= ASU_sorted[x]:
						ASU_sorted.insert(x,a)
						Locat_sorted.insert(x,b)
						break
					else:
						if x == len(ASU_sorted) - 1:
							ASU_sorted.append(a)
							Locat_sorted.append(b)

			else:
				ASU_sorted.append(a)
				Locat_sorted.append(b)

		self.ASU_sorted = ASU_sorted
		self.Locat_sorted = Locat_sorted

	def Knn(self):
		k = 5
		Locat_list = self.Locat_sorted[0:k]
		Locat_list = np.array(Locat_list)







sheet1 = Data_read(r'C:\网盘\基站数据表.xls')
pci = [478,477,479,113,105,378,166,0,280,34,416]
asu = [63,55,58,65,54,73,63,97,20,29,24]
a,b,c = sheet1.Data_clean()

sheet1.Data_handle(pci,asu)
sheet1.Locat_asu()
sheet1.Knn()

print([121.32557668,31.13295799])

