# EXERCICE 3

cars <- read.csv("./datasets/cars.csv", header=TRUE, sep=',') # Load the dataset

# Remove the first column of the cars data frame.
cars <- cars[, -1]

# Construct a new data frame with the new data.
new_cars <- data.frame(speed = c(21, 34), dist = c(47, 87))

# Add the constructed data frame to the cars data frame.
cars <- rbind(cars, new_cars)

# Sort the data in the resulting dataset by column speed (ascending). There is two ways to do it: using the order() command or combining the with and the order() commands.
cars <- cars[order(cars$speed), ]

# Save the resulting dataset as a CSV file.
write.csv(cars, file = "./datasets/cars_sorted.csv", row.names = FALSE)