# import csv  # https://docs.python.org/3/library/csv.html

# # https://django-extensions.readthedocs.io/en/latest/runscript.html

# # python3 manage.py runscript many_load

# from unesco.models import Category, State, Site, Region, Iso


# def run():
#     fhand = open('unesco/load.csv')
#     reader = csv.reader(fhand)
#     next(reader)  # Advance past the header

#     Category.objects.all().delete()
#     State.objects.all().delete()
#     Site.objects.all().delete()
#     Region.objects.all().delete()
#     Iso.objects.all().delete()


#     # Format
#     # name,description,justification,year,longitude,latitude,
#     # area_hectares,category,states,region,iso
#     for row in reader:
#         try:
#             y = int(row[3])
#         except:
#             y = None
#         st, created = State.objects.get_or_create(state=row[8])
#         c, created = Category.objects.get_or_create(category=row[7])
#         r, created = Region.objects.get_or_create(region=row[9])
#         i, created = Iso.objects.get_or_create(iso=row[10])

#         si = Site(state=st, category=c, region=r, iso=i, year=y)
#         si.save()




import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, States, Region, Iso

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:

        c , created = Category.objects.get_or_create(name=row[7])
        st , created = States.objects.get_or_create(name=row[8])
        r , created = Region.objects.get_or_create(name=row[9])
        i , created = Iso.objects.get_or_create(name=row[10])


        try:
            y=int(row[3])
        except:
            y=None

        try:
            z=float(row[4])
        except:
            z=None

        try:
            x=float(row[5])
        except:
            x=None

        if row[6]=="":
            w=None
        else:
            w=float(row[6])

        #try:
           #w=float(row[6])
        #except:
          # w=None


        try:
            j=row[2]
        except:
            j=None

        site = Site(name=row[0], description=row[1], justification=j,  year=y, longitude=z, latitude=x, area_hectares= w, category=c, states=st, region=r, iso=i)

        site.save()