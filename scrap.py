from requests_html import HTMLSession
import io

session = HTMLSession()
r = session.get("https://7esl.com/english-idioms/")
idiom = r.html.xpath("//tbody//tr//td//text()")
csv = io.open("idiom.csv","a", encoding="utf8")

for i in range(len(idiom)):
    print(idiom[i])
    csv.write(idiom[i]+'\n')

#for i in range (0,len(idiom),2) :
#    tab = [idiom[i],idiom[i+1]]
#    csv.write("'"+ tab[0]+ "','" + tab[1] +"'"+ '\n')