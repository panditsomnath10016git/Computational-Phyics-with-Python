
import numpy as np

def lagrange_interpolate(x_data,f_data,x):
    n_data_points=len(x_data)
    c=np.zeros(n_data_points)
    for i in range(n_data_points):
        x_excluded= np.delete(x_data,i)
        c[i]=np.prod((x-x_excluded)/(x_data[i]-x_excluded))
    
    y=sum(np.multiply(c,f_data))
    return y
    
def lagrange_interpolate_xy(x_data,y_data,f_data,x,y):
    if len(x_data)!=len(y_data):
        raise Exception("x_data and y_data dimensions must match")
        
    n_data_points=len(x_data)
    c=np.zeros((n_data_points,n_data_points))
    for i in range(n_data_points):
        for j in range(n_data_points):
            x_excluded= np.delete(x_data,i)
            y_excluded= np.delete(y_data,j)
            c[i,j]=np.prod((x-x_excluded)/(x_data[i]-x_excluded))*np.prod((y-y_excluded)/(y_data[j]-y_excluded))
        
    y=np.sum(np.multiply(c,f_data))
    return y

