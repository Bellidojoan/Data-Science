airquality <- read.csv("./datasets/airquality.csv", header=TRUE, sep=',')

aux <- cut(airquality$Ozone, breaks = 5, labels = c("bin1", "bin2", "bin3", "bin4", "bin5"))
print(aux)

aux <- addNA(aux)

levels(aux)[is.na(levels(aux))] <- "Unknown"