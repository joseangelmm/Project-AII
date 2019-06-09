#encoding:utf-8
from django.shortcuts import render
from main.models import Usuario, Noticia
from bs4 import BeautifulSoup
from django.http.response import HttpResponse
import requests



def noti(request):
    noticias=Noticia.objects.all()
    print(noticias)
    return render(request,'lista_noticias.html', {'noticias':noticias})

def extraerCodigo(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    return soup

def noticiasCienciaELMUNDO():
    codigoHtml=extraerCodigo("https://www.elmundo.es/ciencia-y-salud/ciencia.html")
    listaLinks=[]
    listaLinksImagenes=[]
    for i in codigoHtml.find_all('a',class_='ue-c-cover-content__link'):
        if i.get('href').startswith("https://www.elmundo.es/"):
            listaLinks.append(i.get('href'))
    
    titulares=[]
    fechas=[]
    autores=[]   
    for i in listaLinks:
        codigoHtml=extraerCodigo(i)  
        a=codigoHtml.find("meta",  property="og:image")
        if a:
            listaLinksImagenes.append(a['content']) 
        else:
            b=codigoHtml.find("meta",  attrs={'name':'og:image'})
            listaLinksImagenes.append(b['content'])     
        for i in codigoHtml.find('title'):
            titulares.append(i.split("|")[0])   
        x=codigoHtml.find("meta",  property="article:modified_time")
        fechas.append(x['content'][0:10])
        aut=codigoHtml.find('div',class_="ue-c-article__byline-name")
        if aut is not None:
            autores.append(aut.text)
        else:
            autores.append("Desconocido")
          
    print("Cargando Ciencia elMundo...")
    print(len(listaLinks))
    print(len(listaLinksImagenes))
    print(len(titulares))
    print(len(fechas))
    print(len(autores))
    for i,x in enumerate(titulares): 
        Noticia(titulo=titulares[i], fecha=fechas[i],autor=autores[i],imagen=listaLinksImagenes[i],link=listaLinks[i],categoria="Ciencia").save()



def noticiasCulturaELMUNDO():
    codigoHtml=extraerCodigo("https://www.elmundo.es/cultura.html")
    listaLinks=[]
    listaLinksImagenes=[]
    for i in codigoHtml.find_all('a',class_='ue-c-cover-content__link'):
        if i.get('href').startswith("https://www.elmundo.es/cultura/"):
            listaLinks.append(i.get('href'))
     
    titulares=[]
    fechas=[]
    autores=[]
    
    for i in listaLinks:
        codigoHtml=extraerCodigo(i) 
        a=codigoHtml.find("meta",  property="og:image")
        if a:
            listaLinksImagenes.append(a['content']) 
        else:
            b=codigoHtml.find("meta",  attrs={'name':'og:image'})
            listaLinksImagenes.append(b['content'])      
        for i in codigoHtml.find('title'):
            titulares.append(i.split("|")[0])    
        x=codigoHtml.find("meta",  property="article:modified_time")
        fechas.append(x['content'][0:10])
        aut=codigoHtml.find('div',class_="ue-c-article__byline-name")
        autores.append(aut.text)
    print("Cargando Cultura elMundo...")
    print(len(listaLinks))
    print(len(listaLinksImagenes))
    print(len(titulares))
    print(len(fechas))
    print(len(autores))
    for i,x in enumerate(titulares):   
        Noticia(titulo=titulares[i], fecha=fechas[i], imagen=listaLinksImagenes[i],autor=autores[i],link=listaLinks[i],categoria="Cultura").save()
        
           
def noticiasPoliticaELMUNDO():
    codigoHtml=extraerCodigo("https://www.elmundo.es/t/po/politica.html")
    listaLinks=[]
    listaLinksImagenes=[]   
    for i in codigoHtml.find_all('a',class_='ue-c-cover-content__link'):
        if i.get('href').startswith("https://www.elmundo.es/espana") or i.get('href').startswith("https://www.elmundo.es/cataluna"):
            listaLinks.append(i.get('href'))
    titulares=[]
    fechas=[]
    autores=[]
    for i in listaLinks:
        codigoHtml=extraerCodigo(i)  
        a=codigoHtml.find("meta",  property="og:image")
        if a:
            listaLinksImagenes.append(a['content']) 
        else:
            b=codigoHtml.find("meta",  attrs={'name':'og:image'})
            listaLinksImagenes.append(b['content']) 
        for i in codigoHtml.find('title'):
            titulares.append(i.split("|")[0])  
        x=codigoHtml.find("meta",  property="article:modified_time")
        fechas.append(x['content'][0:10])
        aut=codigoHtml.find('div',class_="ue-c-article__byline-name")
        autores.append(aut.text)
    print("Cargando Politica elMundo...")
    print(len(listaLinks))
    print(len(listaLinksImagenes))
    print(len(titulares))
    print(len(fechas))
    print(len(autores))

    for i,x in enumerate(titulares):   
        Noticia(titulo=titulares[i], fecha=fechas[i], imagen=listaLinksImagenes[i],autor=autores[i],categoria="Politica",link=listaLinks[i]).save()
        
  
def noticiasPublicoCiencia():
    codigoHtml=extraerCodigo("https://www.publico.es/ciencias")
    listaLinks=[]
    listaLinksImagenes=[]
    
    #HREF
    for i in codigoHtml.find_all('div',class_='listing-item'):
        for p in i.find_all('a',class_='page-link'):
            listaLinks.append(str("https://www.publico.es"+p["href"]))
            break
        if (not(len(list(str(i.find_all('img')))) == 2)):       
            for p in i.find_all('img'):
                listaLinksImagenes.append(str("https://www.publico.es"+p["src"]))
                break
        else:
            listaLinksImagenes.append(str("http://www.sanisidrolonas.com.ar/wp-content/uploads/2011/05/sin-imagen12.jpg"))
        
    
    #titulares
    titulares=[]
    fechas=[]
    autores=[]
    for item in listaLinks:
        codigoHtml=extraerCodigo(str(item))
        #titulares
        for i in codigoHtml.find_all('div',class_="article-header-title"):
            for ii in i.find_all('h1'):
                titulares.append(str(ii.text.strip()))
        #fechas
        for i in codigoHtml.find('span',class_="published"):
            fechaa=str(i.strip()).split(" ")
            fechaa1=fechaa[0].replace("/","-")
            print(fechaa1)
            d=fechaa1.split("-")
            print(d)
            
            fechas.append(d[2]+"-"+d[1]+"-"+d[0])
        #autor
        for i in codigoHtml.find_all('div',class_="article-info"):
            for ii in i.find('p'):
                autores.append(str(i.text.strip()))
    #im
    
    print(len(titulares))
    for i in range(len(titulares)):       
        Noticia(titulo=titulares[i], fecha=fechas[i],autor=autores[i],link=listaLinks[i],categoria="Ciencia", imagen=listaLinksImagenes[i]).save()
    
    
def deleteTables():  
    Noticia.objects.all().delete()
      
def iniciarElMundo(self):
    #deleteTables()
    noticiasPublicoCiencia()
    """
    noticiasPoliticaELMUNDO()
    noticiasCulturaELMUNDO()
    noticiasCienciaELMUNDO()
    """
    return HttpResponse("OK")
