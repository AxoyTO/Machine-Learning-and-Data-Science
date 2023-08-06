library(datasets)
data(iris)
install.packages("GGally")
library(GGally)
ggpairs(iris, mapping=ggplot2::aes(colour = Species))

