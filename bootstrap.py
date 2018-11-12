from models.house import House
from peewee import SqliteDatabase, IntegrityError

DATABASE = SqliteDatabase("nyumba.db")


def initialize():
  DATABASE.connect()
  DATABASE.create_tables([House], safe=True)
  try:
        House.create(
            plot_no="kawang_34",
            no_rooms=5,
            rent=20000,
            no_bathrooms=2,
            location="Kawangware, Nairobi",
            nearby_amenities="Kawangware Primary",
            rating=5
        )
        
        House.create(
            plot_no="kawang_35",
            no_rooms=4,
            rent=15000,
            no_bathrooms=1,
            location="Kawangware, Nairobi",
            nearby_amenities="Kawangware Group of schools",
            rating=5
        )

        House.create(
            plot_no="nyeri_1",
            no_rooms=4,
            rent=34000,
            no_bathrooms=1,
            location="nyeri, kenya",
            nearby_amenities="kenya group of schools",
            rating=4
        )

        House.create(
            plot_no="kiambu_1",
            no_rooms=4,
            rent=17000,
            no_bathrooms=7,
            location="kiambu, kenya",
            nearby_amenities="kiambu level 5 hospital",
            rating=4
        )

        House.create(
            plot_no="mombasa",
            no_rooms=4,
            rent=47000,
            no_bathrooms=5,
            location="mombasa, Kenya",
            nearby_amenities="shimo la tewa schools",
            rating=5
        )

        House.create(
            plot_no="nakuru",
            no_rooms=5,
            rent=48000,
            no_bathrooms=4,
            location="nakuru, Kenya",
            nearby_amenities="nkuru genral hospital",
            rating=5
        )

        House.create(
            plot_no="kitale",
            no_rooms=3,
            rent=37000,
            no_bathrooms=4,
            location="kitale, Kenya",
            nearby_amenities="nakuru highway",
            rating=5
        )


        House.create(
            plot_no="kitengela",
            no_rooms=5,
            rent=22000,
            no_bathrooms=3,
            location="Kitengela, Nairobi",
            nearby_amenities="Kitengela Primary",
            rating=5
        )
        
        House.create(
            plot_no="juja",
            no_rooms=6,
            rent=10000,
            no_bathrooms=1,
            location="juja, Nairobi",
            nearby_amenities="juja Group of schools",
            rating=5
        )

        House.create(
            plot_no="kirinyaga",
            no_rooms=3,
            rent=30000,
            no_bathrooms=4,
            location="kirinyaga, Kenya",
            nearby_amenities="kirinyaga group of schools",
            rating=5
        )


        House.create(
            plot_no="kisumu",
            no_rooms=6,
            rent=29000,
            no_bathrooms=4,
            location="Kisumu, kenya",
            nearby_amenities="Kisumu Primary",
            rating=5
        )
        
        House.create(
            plot_no="Rongai",
            no_rooms=7,
            rent=11000,
            no_bathrooms=3,
            location="Rongai, Nairobi",
            nearby_amenities="Nairobi Group of schools",
            rating=5
        )
        
        House.create(
            plot_no="kitui",
            no_rooms=4,
            rent=37000,
            no_bathrooms=6,
            location="kitui, Kenya",
            nearby_amenities="kitui hospital",
            rating=5
        )


        House.create(
            plot_no="kimilili",
            no_rooms=4,
            rent=21000,
            no_bathrooms=4,
            location="kimilili, Kenya",
            nearby_amenities="kimilili hospital",
            rating=5
        )
        
        House.create(
            plot_no="mwingi",
            no_rooms=4,
            rent=11000,
            no_bathrooms=3,
            location="mwingi, Nairobi",
            nearby_amenities="mwingi high school",
            rating=5
        )
        
        House.create(
            plot_no="Muranga",
            no_rooms=5,
            rent=22000,
            no_bathrooms=3,
            location="Muranga, Kenya",
            nearby_amenities="Muranga hospital",
            rating=5
        )
        
        House.create(
            plot_no="westlands",
            no_rooms=3,
            rent=10000,
            no_bathrooms=2,
            location="westlands, Nairobi",
            nearby_amenities="safaricom centre",
            rating=5
        )


  except IntegrityError:
        pass

  DATABASE.close()