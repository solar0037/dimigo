x <- list(a=list(val = c(1, 2, 3)), b=list(val = c(1, 2, 3, 4)))
x
x[1]
x[[1]]

x <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3)
x <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8), nrow = 2)
x <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3, byrow = T)
x <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3,
            dimnames = list(c("item1", "item2", "item3"),
                            c("feature1", "feature2", "feature3")))
x

methods("plot")
install.packages("mlbench")
library(mlbench)

plot()
