import random
name = input("İsminiz Nedir? ")
print("Welcome ", name)
print("Türkiye'nin Şehirleri")
 
words_list = ['ankara', 'samsun', 'istanbul', 'adana', 
        'yozgat', 'manisa', 'bursa', 'edirne', 
         'kars', 'kırıkkale', 'elazığ', 'sinop',
         'ordu','trabzon','rize','izmir','burdur',
         'Afyon','artvin','denizli','muğla'] 
 
liste=[]
word = random.choice(words_list)
print('Bir harf giriniz:')
can = 6
garbage =[]
for i in word:
        garbage.append('-')
for i in word:
        print('-',end="")
print("")
while(can>0):
        tahmin=input()
        if(liste.count(tahmin)==0):
                liste.append(tahmin)
                search = word.count(tahmin)
                if(search==0):
                        can-=1
                        print("Kalan deneme hakkınız: ", can)
                else:
                        for i in range(0,len(word)):
                                if(tahmin== word[i]):
                                        garbage[i]=tahmin
                        if(garbage.count('-')==0):
                                print("Kazandınız \_0_/")
                                break
                        else:
                                for i in garbage:
                                        print(i,end="")
                                print("")
        else:
                print("Bu harfi daha önce denediniz :(")
        
if(can==0):
        print("Kaybettiniz :(")
        for i in word:
                print(i, end="")
