# calendar-oswiecim
Kalendarz wydarzeń dla Oświęcimia [Koduj Dla Polski]

##### Uwaga! Pisane z myślą o Python 3.4 i na takim było testowane.

### Zależności

```
django==1.8.3
pillow==2.9.0
sorl-thumbnail==12.3
django-ckeditor==4.5.0
django-braces==1.8.1
```

###### import starych danych

```
python manage.py import_data SCIEZKA
```

###### Pillow
Do kompilacji wymagane są pliki nagłówkowe Pythona. W openSUSE te pliki znajdziemy w pakiecie `python3-devel`.
Obsługa poszczególnych formatów graficznych jest uzależniona od dodatkowych bibliotek. 
```
TKINTER 
JPEG wymaga libjpeg8-devel
OPENJPEG (JPEG2000) support not available
ZLIB (PNG/ZIP) wymaga libpng16-devel i zlib-devel
LIBTIFF wymaga libtiff-devel
FREETYPE2 wymaga freetype-devel
LITTLECMS2
WEBP wymaga libwebp-devel
WEBPMUX wymaga libwebp-devel
```

###### Instalacja

```
docker-compose build
docker-compose run webapp python manage.py migrate
docker-compose run webapp python manage.py createsuperuser
docker-compose run --service-ports webapp python manage.py runserver 0.0.0.0:8000
```
