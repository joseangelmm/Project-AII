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
    if request.user.is_authenticated:
        for item in gustosUsuario.objects.filter(username=request.user):
            obj = gustosUsuario.objects.get(username=(item.username))
            obj.numerosDeNoticiasBuscadasDeLaCategoriaCultura = item.numerosDeNoticiasBuscadasDeLaCategoriaCultura+1
            obj.save()
            
    listaNoticias=Noticia.objects.filter(categoria="Cultura")
    fechaActual=str("{}-{}-{}".format(fecha.year, fecha.month, fecha.day))
    if (len(fechaActual.split("-")[1])==1):
        fechaDef= fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+fechaActual.split("-")[2]
        fechaDef1=fechaActual.split("-")[0]+"-"+"0"+fechaActual.split("-")[1]+"-"+str(int(fechaActual.split("-")[2])-1)
    
    listaDefinitivaNoticias=[]
    for item in listaNoticias:
        if (str(item.fecha)==str(fechaDef) or str(item.fecha)==str(fechaDef1)):
            listaDefinitivaNoticias.append(item)
    print(requests.get)
    return render(request,'lista_noticias_cultura.html', {'noticias':listaDefinitivaNoticias})

def noticiasInternacional(request):
    if request.user.is_authenticated:
        for item in gustosUsuario.objects.filter(username=request.user):
            obj = gustosUsuario.objects.get(username=(item.username))
            obj.numerosDeNoticiasBuscadasDeLaCategoriaInternacional = item.numerosDeNoticiasBuscadasDeLaCategoriaInternacional+1
            obj.save()
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
    if request.user.is_authenticated:
        for item in gustosUsuario.objects.filter(username=request.user):
            obj = gustosUsuario.objects.get(username=(item.username))
            obj.numerosDeNoticiasBuscadasDeLaCategoriaTecnologiaYCiencia= item.numerosDeNoticiasBuscadasDeLaCategoriaTecnologiaYCiencia+1
            obj.save()
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
    if request.user.is_authenticated:
        for item in gustosUsuario.objects.filter(username=request.user):
            obj = gustosUsuario.objects.get(username=(item.username))
            obj.numerosDeNoticiasBuscadasDeLaCategoriaPolitica= item.numerosDeNoticiasBuscadasDeLaCategoriaPolitica+1
            obj.save()
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
    noticias1=[]
    noticias=[]
    if request.user.is_authenticated:
        for item in gustosUsuario.objects.filter(username=request.user):
 
            totalGustos=item.numerosDeNoticiasBuscadasDeLaCategoriaTecnologiaYCiencia+item.numerosDeNoticiasBuscadasDeLaCategoriaInternacional+item.numerosDeNoticiasBuscadasDeLaCategoriaPolitica+item.numerosDeNoticiasBuscadasDeLaCategoriaCultura
            gustosCiencia=int((item.numerosDeNoticiasBuscadasDeLaCategoriaTecnologiaYCiencia*10)/totalGustos)+1
            gustosCultura=int((item.numerosDeNoticiasBuscadasDeLaCategoriaCultura*10)/totalGustos)+1
            gustosPolitica=int((item.numerosDeNoticiasBuscadasDeLaCategoriaPolitica*10)/totalGustos)+1
            gustosInternacional=int((item.numerosDeNoticiasBuscadasDeLaCategoriaInternacional*10)/totalGustos)+1

            print(totalGustos)
            print(gustosCultura)
            print(gustosCiencia)
            print(gustosInternacional)
            print(gustosPolitica)
        
        noticiasDef=[]
        noticias=Noticia.objects.filter(categoria="Ciencia").order_by('fecha')
        noticias1=noticias.reverse()
        for item in noticias1[0:gustosCiencia]:
            noticiasDef.append(item)
        noticias=Noticia.objects.filter(categoria="Cultura").order_by('fecha')
        noticias1=noticias.reverse()
        for item in noticias1[0:gustosCultura]:
            noticiasDef.append(item)
        noticias=Noticia.objects.filter(categoria="Internacional").order_by('fecha')
        noticias1=noticias.reverse()
        for item in noticias1[0:gustosInternacional]:
            noticiasDef.append(item)
        noticias=Noticia.objects.filter(categoria="Politica").order_by('fecha')
        noticias1=noticias.reverse()
        for item in noticias1[0:gustosPolitica]:
            noticiasDef.append(item)    
        
        
        
                    
    else:
        noticiasDef=[]
        noticias=Noticia.objects.filter(categoria="Ciencia").order_by('fecha')
        noticias1=noticias.reverse()
        for item in noticias1[0:3]:
            noticiasDef.append(item)
        noticias=Noticia.objects.filter(categoria="Cultura").order_by('fecha')
        noticias1=noticias.reverse()
        for item in noticias1[0:3]:
            noticiasDef.append(item)
        noticias=Noticia.objects.filter(categoria="Internacional").order_by('fecha')
        noticias1=noticias.reverse()
        for item in noticias1[0:2]:
            noticiasDef.append(item)
        noticias=Noticia.objects.filter(categoria="Politica").order_by('fecha')
        noticias1=noticias.reverse()
        for item in noticias1[0:2]:
            noticiasDef.append(item)
             
    return render(request,'lista_noticias.html', {'noticias':noticiasDef})
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
