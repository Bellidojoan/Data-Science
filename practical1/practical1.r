# Exercice 1
x <- seq(1, 12)
print(x)

# Exercice 2
repeated_sequence <- rep(c(6, 2, 4), times = 4)
print(repeated_sequence)

# Exercice 3
sequence <- c(rep(9, 6), rep(2, 5), rep(5, 4))
matrix_sequence <- matrix(sequence, nrow = 5, ncol = 3, byrow = FALSE)
print(matrix_sequence)

# Exercice 4.1
set.seed(100)
random_vector <- rnorm(20)
print(random_vector)

# Exercice 4.2
mean_value <- mean(random_vector)
median_value <- median(random_vector)
variance_value <- var(random_vector)
sd_value <- sd(random_vector)

print(paste("Mean:", mean_value))
print(paste("Median:", median_value))
print(paste("Variance:", variance_value))
print(paste("Standard Deviation:", sd_value))

# Exercice 5

# (a) Read the data into an R object named students
students <- read.table("data1.txt", header = FALSE, sep = "")

# (b) Add column titles: height, shoesize, gender, population
colnames(students) <- c("height", "shoesize", "gender", "population")

# (c) Check that R reads the file correctly
print(students)

# (d) Print the header names only
print(colnames(students))

# (e) Print the height column
print(students$height)


# (f) Gender and population distribution
gender_distribution <- table(students$gender)
population_distribution <- table(students$population)
print(gender_distribution)
print(population_distribution)

# (g) Contingency table
contingency_table <- table(students$gender, students$population)
print(contingency_table)

# (h) Subsets by gender using data frame operations
male_students <- students[students$gender == "Male", ]
female_students <- students[students$gender == "Female", ]

# Subsets by gender using subset
male_students_subset <- subset(students, gender == "Male")
female_students_subset <- subset(students, gender == "Female")

# (i) Subsets by height using data frame operations
median_height <- median(students$height)
below_median <- students[students$height < median_height, ]
above_median <- students[students$height >= median_height, ]

# Subsets by height using subset
below_median_subset <- subset(students, height < median_height)
above_median_subset <- subset(students, height >= median_height)

# (j) Convert height to metres
students$height <- students$height / 100
for (i in 1:nrow(students)) {
  students$height[i] <- students$height[i] / 100
}
students$height <- apply(students["height"], 1, function(x) x / 100)

# (k) Plot height against shoesize with blue circles for males and magenta crosses for females
plot(students$height, students$shoesize,
     col = ifelse(students$gender == "Male", "blue", "magenta"),
     pch = ifelse(students$gender == "Male", 16, 4),
     xlab = "Height (m)", ylab = "Shoe Size")
legend("topright", legend = c("Male", "Female"),
       col = c("blue", "magenta"),
       pch = c(16, 4))
