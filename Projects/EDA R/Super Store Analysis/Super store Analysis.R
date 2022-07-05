library(dplyr)
library(tidyverse)
getwd()
df = read.csv('Superstore.csv')
df
View(df)
head(df)
head(df,10)
tail(df)
tail(df,10)
str(df)
summary(df)
glimpse(df)
sample_n(df,5)
sample_frac(df,0.2)
distinct(df)
x = distinct(df)
x
dim(df)
is.null(df)
View(df)
data_category = select(df,Category,Product.Name,Sales)
View(data_category)
data_state=select(df,State,Poduct.Name,Sales)
view(data_state)
dim(data_category)

data_category$Category
cat1=df[df$Category=='Technology',]
view(cat1)

data_category$Furniture
cat2=df[df$Category=='Furniture',]
view(cat2)
str(df)
df %>%
  count(Profit)
quant=df[df$Quantity>5,]
view(quant)

quant1=df[df$Quantity>5,c(14:21),]
view(quant)
view(head(quant,10))

quant2=df[df$Quantity>5,c(17:19)]
view(quant2)

view(df) 

quant3=df[df$Sales>5,c(1:3)]
view(quant3)

quant4=df[df$Category=='Technology'&df$Sub.Category=='Phones',]
view(quant4)

quant5=df[df$Category=='Technology'&df$Sub.Category=='Phones',c(11,12,15)]
view(quant5)

subset_data=subset(df,Segment=='Consumer'& Region=='East')
view(subset_data)

slt=select(df,Product.Name,Profit)
view(slt)
arr=arrange(slt,Profit)
view(arr)

fin=select(df,Quantity,Sales)
view(fin)

arr1=arrange(fin,Sales)
view(arr1)

arr2=arrange(fin,-Sales)
view(arr2)

arr3=arrange(slt,-Profit)
view(arr3)

df1=select(df,-Row.ID,-Order.ID,-Order.Date)
view(df1)
df1=select(df1,-Postal.Code,-Customer.ID)
view(df1)

df2=select(df,-Product.ID)
view(df2)

st=select(df,starts_with('C'))
view(st)


st1=select(df,contains('Name'))
view(st1)
st2=select(df,matches('Name'))
view(st2)

df=rename(df,Product=Product.Name)
view(df)
df=rename(df,Offer=Discount)
view(df)

dv=filter(df,Region=='South')
view(dv)
dim(dv)

ds=summarise(df,sum_sales=sum(Sales))
view(ds)

statewise=df %>% group_by(State) %>% summarize(total_sales=sum(Sales))
view(statewise)

productwise=df %>% group_by(Product) %>% summarise(total_sales=sum(Sales))
view(productwise)

de=df %>% group_by(Product) %>% summarize(total_profit=sum(Profit)) %>% arrange(desc(total_profit))
view(de)

gsplot=df %>% group_by(State) %>% summarise(total_sales=sum(Sales)) %>% arrange(desc(total_sales))
view(gsplot)


colnames(gsplot)=c('region','value')
view(gsplot)

gsplot$region=tolower(gsplot$region)

install.packages('choroplethr')
install.packages('choroplethrMaps')

library(choroplethr)
library(choroplethrMaps)
gs_sales=state_choropleth(gsplot,title='Graphical Analysis',legend='Sales in us')
print(gs_sales)
First=df[df$Ship.Mode=='First Class',]
view(First)

quant4=df[df$Category=='Technology'&df$Segment=='Consumer',c(8,15,17,18,19)]
view(quant4)

ggplot(data=df,aes(x=Quantity,y=Sales,fill=Ship.Mode))+geom_bar(stat='identity')

ggplot(data=df,aes(x=Quantity,y=Sales,fill=Region))+geom_bar(stat='identity')

ggplot(data=df,aes(x=Sales,y=Profit,col=Ship.Mode))+geom_point()

