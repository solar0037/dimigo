setwd("c:\\R_temp")
data <- read.csv("baseball.csv", header = T)
head(data,10)

class(data)
a<-1
a<-"Hello"
class(a)

x <- c(1,2,3,4,5)
x
class(x)
x <- c("1", "2", "3")
x <- c(1,"2",3)

x <- 1:100
x <- 5:10
seq(1, 10, 2)

x <- c(1, 2, 4)

class(x)
names(x) <- c("kim", "seo", "park")
x

x <- c("a", "b", "c")
x[1]
x[-1]
x[c(1, 2)]
x[c(1, 3)]
x["seo"]

rep(1:10)
rep(1:2, each=5)

data$H
bp <- barplot(data$H, main=paste("2021 KBO"), col=rainbow(12),
              cex.names=1.3, las=3,  names.arg=data$name, ylim=c(0,200))

x<-median(data$H)
x
x<-sd(data$H)
x
x<-max(data$H)
x

summary(data)

x<-mean(data$H)
x
abline(h=x, lty=1, col="red")

plot(data$AVG, data$HR)
