setwd("c:\\R_temp")

# 패키지 설치
# install.packages("multilinguer")
library(multilinguer)
# install_jdk( ) 
# install.packages(c("hash", "tau", "Sejong", "RSQLite", "devtools", "bit", "rex", "lazyeval", "htmlwidgets", "crosstalk", "promises", "later", "sessioninfo", "xopen", "bit64", "blob", "DBI", "memoise", "plogr", "covr", "DT", "rcmdcheck", "rversions"), type = "binary")
# install.packages("remotes")
# remotes::install_github('haven-jeon/KoNLP', upgrade = "never", INSTALL_opts=c("--no-multiarch"))


#install.packages("KoNLP")
# install.packages("wordcloud")
# install.packages("stringr")


library("KoNLP")
library("wordcloud")
library("stringr")


#install.packages("waldo")
#install.packages("knitr")



useSejongDic()
# extractNoun("아버지가 방에 들어가신다")

#mergeUserDic(data.frame(readLines("mergefile.txt"), "ncn"))

# 데이터 분석 및 시각화
for (filename in c("big_data", "artificial_intelligence")) {
  txt <- readLines(paste(filename, ".txt", sep=""), encoding="UTF-8")
  txt
  place <- sapply(txt,extractNoun,USE.NAMES = F)
  
  class(place)
  head(place, 2)
  c <- unlist(place)
  c
  place <- Filter(function(x){nchar(x) >=2}, c)
  place
  res <- str_replace_all(place,"[^[:alpha:]]","")
  res <- res[res != ""]
  
  # res <-gsub("제주","",res)
  
  
  write(res, paste(filename, "2.txt", sep=""))
  res2 <-read.table(paste(filename, "2.txt", sep=""))
  class(res2)
  head(res2)
  wordcount <- table(res2)
  head(sort(wordcount, decreasing=T),30)
  
  library(RColorBrewer)
  palete <- brewer.pal(9,"Set1")
  
  wordcloud(names(wordcount),freq = wordcount,scale = c(5,1),rot.per=0.25,
            min.freq=2,random.order = F,random.color = T, colors = palete)
}
