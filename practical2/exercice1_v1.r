# EXERCICE 1

titanic <- read.csv("./datasets/titanic.csv", header=TRUE, sep=',') # Load the dataset
titanic<-subset(titanic,select=-X) # Remove the row index column

head(titanic) # Display the first few rows of the dataset
summary(titanic) # Display the summary statistics of the dataset
plot(titanic) # Create a scatterplot matrix of the dataset


# Which variables are quantitative and which variables are categorical? How can we know it?
str(titanic) # Using str() function we can see the structure of the dataset. We can see the data type of each variable. If the data type is integer or numeric, then it is quantitative. If the data type is factor, then it is categorical.

# Quantitative (Numerical) Variables:
# - Freq: Represents the frequency (number of people)

# Categorical Variables:
# - X: Row index (treated as categorical, despite being an integer)
# - Class: Passenger class (e.g., "1st", "2nd", "3rd", "Crew")
# - Sex: Gender (e.g., "Male", "Female")
# - Age: Age group (e.g., "Child", "Adult")
# - Survived: Survival status (e.g., "Yes", "No")