import sys
sys.path.append("/home/PJLAB/liangyiwen/Even/code/OpenBaseLab-Edu")
from BaseML import cls

model=cls('CART')

model.load_dataset('./Downloads/案例1处理.csv', type ='csv', x_column = [1,2,3,4],y_column=[5])
model.train(validate=True)
model.save('mymodel.pkl')

#y=model.inference([[1,  1,  1,  1,  1]])
# m=cls('KNN',n_neighbors =3 )
# m.load('mymodel.pkl')
# y=m.inference([[1,  1,  -1,  0]])
# print(y)