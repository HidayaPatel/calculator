# Importing Libraries 
import matplotlib.pyplot as plt
from sklearn import datasets

# loaing the iris dataset (built - in)
iris = datasets.load_iris()

# Displaying the iris dataset

# 1. print(iris)
# 2. print(iris.data) 
# 3. print(iris.data.shape)
# 4. print(len(iris.data)) #-see number of rows-
# 5. print(iris.feature_names)      
# 6. print(iris.target_names) 

# To understand the mapping:

# 0 corresponds to 'setosa'
# 1 corresponds to 'versicolor'
# 2 corresponds to 'virginica'

# Extracting the features and labels
# sepal length - slicing-  : means select all rows 0 means select first column
x = iris['data'][:, 0] 
y = iris['data'][:, 2]  # petal length

# Plotting the data points
plt.scatter(x, y)

# Adding labels and title
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

# Displaying the plot
plt.title('Iris Dataset Scatter Plot')

# Showing the plot
plt.show()


