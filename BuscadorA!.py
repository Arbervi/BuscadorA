import webbrowser
from datetime import datetime

reloj = datetime.now()
link = None
terminar=False


#periodicos=["elmundo","elpais"]
#enlaces=["http://www.elmundo.es","http://elpais.com"]
#palabra=input("¿Qué periódico quieres ver?: ")
#posicion=periodicos.index(palabra)
#webbrowser.open(enlaces[posicion], new=2)
print ('Equipo A 2020-2021')
print('64K RAM SYSTEM 38911 PYTHON BYTES FREE READY')
print ('BuscadorA!')
while terminar==False:
    busqueda=input('Busqueda:\n')
    busqueda=busqueda.lower().replace(" ","")
    if busqueda == ('youtube'): link = 'https://www.youtube.com/'
    if busqueda == ('hobbyconsolas'):link=('https://www.hobbyconsolas.com/')
    if busqueda == ('hangouts'):link=('https://hangouts.google.com/')
    if busqueda == ('scratch'):link=('https://scratch.mit.edu/')
    if busqueda == ('facebook'):link='https://es-es.facebook.com/'
    if busqueda == ('twitter'):link='https://twitter.com/'
    if busqueda == ('sanpchat'):link='https://www.snapchat.com/'
    if busqueda == ('sescam'):link='https://sanidad.castillalamancha.es/'
    if busqueda== ('rae'):link='https://www.rae.es/'
    if busqueda== ('nintendo'):link='www.nintendo.es'
    if busqueda==('uclm'):link='https://www.uclm.es/'
    if busqueda==('boe'):link='https://boe.es/'
    if busqueda==('playstation5'):link='https://www.playstation.com/es-es/explore/ps5/'
    if busqueda==('playstation'):link='https://www.playstation.com/'
    if busqueda==('gmail'):link='www.Gmail.com'
    if busqueda==('hotmail'):link='https://outlook.live.com/mail/inbox'
    if busqueda==('tiktok'):link='https://www.tiktok.com/'
    if busqueda==('microsoft'):link='https://www.microsoft.com/'
    if busqueda==('apple'):link='www.Apple.com'
    if busqueda==('raspberrypi'):link='https://www.raspberrypi.org/'
    if busqueda==('lobosunited'):link='https://www.youtube.com/channel/UCuZhu4mMnfuBVWOCH2KQO2w'
    if busqueda==('python'):link='https://www.python.org/'
    if busqueda==('duckduckgo'):link='https://duckduckgo.com/about'
    if busqueda==('fifa'):link='https://www.ea.com/es-es/games/fifa'
    if busqueda==('fornite'):link='https://www.epicgames.com/fortnite/es-ES/home'
    if busqueda==('onedrive'):link='https://onedrive.live.com/'
    if busqueda==('roblox'):link='www.Roblox.com'
    if busqueda==('google'):link='www.Google.com'
    if busqueda==('google!'):link='https://www.google.com/search?sxsrf=ALeKk03HPhuodABC_LcbgECr_0JIGgQuLw%3A1585927094527&source=hp&ei=tlOHXtDjHc2flwTrobeoAQ&q=google+in+1998&oq=go&gs_lcp=CgZwc3ktYWIQARgBMgQIIxAnMgQIIxAnMgQIIxAnMgUIABCRAjIHCAAQFBCHAjICCAAyAggAMgIIADICCAAyAggAOgcIIxDqAhAnULoMWLoYYJFMaAJwAHgAgAFViAH0AZIBATOYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab'
    if busqueda==('netscape'):link='https://isp.netscape.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAAVpxwsYqtn5VE_Ki6QC03lRuHrp3Xpc4HSx4q0uoh9-MPPYflq-XOJgMNyE5s_7yc9N6EPbDERB3_UaLXzdt-Da-inppKaY6_XhixEk1_r0E6MA5F2JZaQs7o1xnFoFGIsK3I4g3-iPOmTGXHKepQEeAk9SkMXIm8BhvHSJDXiJ'
    if busqueda==('emuladorsupernintendo'):link='https://supernintendoemulator.com/'
    if busqueda==('hora'): print(reloj.hour,":",reloj.minute)
    if busqueda==('aol'):link='https://search.aol.com/'
    if busqueda==('yahoo'):link='https://es.yahoo.com/'
    if busqueda==('descargarroblox') :link='https://www.roblox.com/account/signupredir'
    if busqueda==('yandex'):link='www.yandex.com'
    if busqueda==('amazon'):link='www.amazon.es'
    if busqueda==('close'): terminar=True
    if busqueda==('trunks2009'): link='https://www.youtube.com/channel/UC39oWmQNe_GkLMM49tkoyyw'
    if busqueda == ('steam'): link = 'https://store.steampowered.com/'
    if busqueda == ('epicgames'): link = 'https://www.epicgames.com/store/en-US/'
    if not(link is None):
        webbrowser.open(link, new=2)
    link=None

