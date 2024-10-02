airquality <- read.csv("./datasets/airquality.csv", header=TRUE, sep=',') # Load the dataset

print(airquality[1:2, ])

nrow(airquality)


print(airquality[40,])

airquality <- na.omit(airquality)
mean(airquality$Ozone)

print(subset(airquality, Ozone > 31 & Temp > 90))