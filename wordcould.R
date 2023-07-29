#install.packages("wordcloud")
library(wordcloud)
#install.packages("RColorBrewer")
library(RColorBrewer)
#install.packages("wordcloud2")
library(wordcloud2)

reviews_wordcount <- read.csv("/Users/michellesoo/Downloads/wordcount_output.csv", stringsAsFactors = FALSE)
set.seed(1234) # for reproducibility 
wordcloud(words = reviews_wordcount$Word, freq = reviews_wordcount$Count, min.freq = 8000,
          max.words=400, random.order=FALSE, rot.per=0.35,
