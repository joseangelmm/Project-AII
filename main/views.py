#encoding:utf-8
from django.shortcuts import render
from main.models import Noticia, gustosUsuario
from bs4 import BeautifulSoup
from django.http.response import HttpResponse
import requests
import time
from django.contrib.auth.models import User
from datetime import datetime
fecha = datetime.now()
####DISTINTAS CATEGORÍAS####
def noticiasCultura(request):
    listaNoticias=Noticia.objects.filter(categoria="Cultura")
    fechaActual=str("{}-{}-{}".format(fecha.year, fecha.month, fecha.day))
    if (len(fechaActual.split("-")[1])==1):
        fechaDef= fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+fechaActual.split("-")[2]
        fechaDef1=fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+str(int(fechaActual.split("-")[2])-1)
    
    listaDefinitivaNoticias=[]
    for item in listaNoticias:
        if (str(item.fecha)==str(fechaDef) or str(item.fecha)==str(fechaDef1)):
            listaDefinitivaNoticias.append(item)
    
    return render(request,'lista_noticias_cultura.html', {'noticias':listaDefinitivaNoticias})

def noticiasInternacional(request):
    listaNoticias=Noticia.objects.filter(categoria="Internacional")
    fechaActual=str("{}-{}-{}".format(fecha.year, fecha.month, fecha.day))
    if (len(fechaActual.split("-")[1])==1):
        fechaDef= fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+fechaActual.split("-")[2]
        fechaDef1=fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+str(int(fechaActual.split("-")[2])-1)
    
    listaDefinitivaNoticias=[]
    for item in listaNoticias:
        if (str(item.fecha)==str(fechaDef) or str(item.fecha)==str(fechaDef1)):
            listaDefinitivaNoticias.append(item)
    return render(request,'lista_noticias_internacional.html', {'noticias':listaDefinitivaNoticias})

def noticiasCiencia(request):
    listaNoticias=Noticia.objects.filter(categoria="Ciencia")
    fechaActual=str("{}-{}-{}".format(fecha.year, fecha.month, fecha.day))
    if (len(fechaActual.split("-")[1])==1):
        fechaDef= fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+fechaActual.split("-")[2]
        fechaDef1=fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+str(int(fechaActual.split("-")[2])-1)
    
    listaDefinitivaNoticias=[]
    for item in listaNoticias:
        if (str(item.fecha)==str(fechaDef) or str(item.fecha)==str(fechaDef1)):
            listaDefinitivaNoticias.append(item)
    return render(request,'lista_noticias_ciencia.html', {'noticias':listaDefinitivaNoticias})

def noticiasPolitica(request):
    listaNoticias=Noticia.objects.filter(categoria="Politica")
    fechaActual=str("{}-{}-{}".format(fecha.year, fecha.month, fecha.day))
    if (len(fechaActual.split("-")[1])==1):
        fechaDef= fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+fechaActual.split("-")[2]
        fechaDef1=fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+str(int(fechaActual.split("-")[2])-1)
    
    listaDefinitivaNoticias=[]
    for item in listaNoticias:
        if (str(item.fecha)==str(fechaDef) or str(item.fecha)==str(fechaDef1)):
            listaDefinitivaNoticias.append(item)
    return render(request,'lista_noticias_politica.html', {'noticias':listaDefinitivaNoticias})
####TODAS LAS SECCIONES####
def noti(request):
    noticias=Noticia.objects.all()
    if request.user.is_authenticated:
        for item in gustosUsuario.objects.filter(username=request.user):
            print(item.numerosDeNoticiasBuscadasDeLaCategoriaTecnologiaYCiencia)
    return render(request,'lista_noticias.html', {'noticias':noticias})
############################################
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
    
    for i,x in enumerate(titulares): 
        if not(Noticia.objects.filter(titulo=titulares[i])):
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
       
        if (str(aut)=="None"):
            autores.append("Sin autor")
        else:
            autores.append(aut.text)
    print("Cargando Cultura elMundo...")
    print(len(listaLinks))
    print(len(listaLinksImagenes))
    print(len(titulares))
    print(len(fechas))
    print(len(autores))
    for i,x in enumerate(titulares):   
        if not(Noticia.objects.filter(titulo=titulares[i])):
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
   
    for i,x in enumerate(titulares):   
        if not(Noticia.objects.filter(titulo=titulares[i])):
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
            d=fechaa1.split("-")
            
            fechas.append(d[2]+"-"+d[1]+"-"+d[0])
        #autor
        for i in codigoHtml.find_all('div',class_="article-info"):
            for ii in i.find('p'):
                autores.append(str(i.text.strip()))
    #im
    
   
    for i in range(len(titulares)):
        if not(Noticia.objects.filter(titulo=titulares[i])):       
            Noticia(titulo=titulares[i], fecha=fechas[i],autor=autores[i],link=listaLinks[i],categoria="Ciencia", imagen=listaLinksImagenes[i]).save()
    
def noticiasPublicoInternacional():
    codigoHtml=extraerCodigo("https://www.publico.es/internacional")
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
            d=fechaa1.split("-")
            
            fechas.append(d[2]+"-"+d[1]+"-"+d[0])
        #autor
        for i in codigoHtml.find_all('div',class_="article-info"):
            for ii in i.find('p'):
                autores.append(str(i.text.strip()))
    #im
    
 
    for i in range(len(titulares)):   
        if not(Noticia.objects.filter(titulo=titulares[i])):    
            Noticia(titulo=titulares[i], fecha=fechas[i],autor=autores[i],link=listaLinks[i],categoria="Internacional", imagen=listaLinksImagenes[i]).save()
    
def noticiasPublicoPolitica():
    codigoHtml=extraerCodigo("https://www.publico.es/politica")
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
            d=fechaa1.split("-")
            
            fechas.append(d[2]+"-"+d[1]+"-"+d[0])
        #autor
        for i in codigoHtml.find_all('div',class_="article-info"):
            for ii in i.find('p'):
                autores.append(str(i.text.strip()))
    #im
    

    for i in range(len(titulares)): 
        if not(Noticia.objects.filter(titulo=titulares[i])):      
            Noticia(titulo=titulares[i], fecha=fechas[i],autor=autores[i],link=listaLinks[i],categoria="Politica", imagen=listaLinksImagenes[i]).save()
    
    

def noticiasPublicoCultura():
    codigoHtml=extraerCodigo("https://www.publico.es/culturas")
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
            d=fechaa1.split("-")
            
            fechas.append(d[2]+"-"+d[1]+"-"+d[0])
        #autor
        for i in codigoHtml.find_all('div',class_="article-info"):
            for ii in i.find('p'):
                autores.append(str(i.text.strip()))
    #im
    
    for i in range(len(titulares)):  
        if not(Noticia.objects.filter(titulo=titulares[i])):
            Noticia(titulo=titulares[i], fecha=fechas[i],autor=autores[i],link=listaLinks[i],categoria="Cultura", imagen=listaLinksImagenes[i]).save()
    


def deleteTables():  
    Noticia.objects.all().delete()
      
def iniciarElMundo(self):
    #deleteTables()
    
    noticiasPublicoCiencia()
    noticiasPublicoCultura()
    noticiasPublicoInternacional()
    noticiasPublicoPolitica()
    
    noticiasPoliticaELMUNDO()
    noticiasCulturaELMUNDO()
    noticiasCienciaELMUNDO()
    
    return HttpResponse("OK")
