# EXERCICE 2

cars <- read.csv("./datasets/cars.csv", header=TRUE, sep=',') # Load the dataset

# Make a plot of the distance field in terms of the speed field (use the $ syntax).
plot(cars$speed, cars$dist, xlab="Speed", ylab="Distance", main="Distance vs. Speed")

# Make a histogram of the distance variable.
hist(cars$dist, xlab="Distance", main="Histogram of Distance")

# Make a histogram of the speed variable.
hist(cars$speed, xlab="Speed", main="Histogram of Speed")

# Modify the previous plots to show the name of the variables (“speed” or “distance”) as the title of the axis. Change the title of the three graphics, and also use colours for the histograms and titles. Save the new graphics as pdf files.

# Save the plots as PDF
pdf("./documents/exercice2/ex2_distance_vs_speed_plot.pdf")
# Plot of Distance vs Speed with modified axis labels and title
plot(cars$speed, cars$dist, 
     xlab="Speed", 
     ylab="Distance", 
     main="Distance vs Speed", 
     col="blue",
     col.main="red")
dev.off()

pdf("./documents/exercice2/ex2_histogram_distance.pdf")
# Histogram of Distance with modified title, axis labels, and color
hist(cars$dist, 
     xlab="Distance", 
     main="Histogram of Distance", 
     col="green",
     col.main="red")
dev.off()

pdf("./documents/exercice2/ex2_histogram_speed.pdf")
# Histogram of Speed with modified title, axis labels, and color
hist(cars$speed, 
     xlab="Speed", 
     main="Histogram of Speed", 
     col="orange",
     col.main="blue")
dev.off()