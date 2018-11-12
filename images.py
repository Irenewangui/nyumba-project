from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    IntegerField,
                    # VarCharField,
                    TextField,
                    OperationalError,
                    IntegrityError)
db = SqliteDatabase("nyumba.db")


class Images(Model):

    name = CharField(max_length=1000, unique=True)
    description = TextField(default="Good image")
    thumbnail_link = CharField(max_length=1000)
    fullimage_link = CharField(max_length=1000)
    
   
    class Meta:
        database = db


def initialize():
    try:
        Images.create_table(safe=True)
    except OperationalError:
        pass
    try:
        Images.create(
            name="house_1",
            description="Nakuru", 
            thumbnail_link="static/hou.jpg",
            fullimage_link="static/hbig.jpg"
            )
    except IntegrityError:
        pass
   
    try:       
        Images.create(
            name="house_kenya",
            description=" kisumu",
            thumbnail_link="static/spring-2955582_640.jpg",
            fullimage_link="static/spring-2955582_1920.jpg"
            )
    except IntegrityError:
        pass
    try:
        
        Images.create(
            name="today_nyumba",
            description=" ngong'",
            thumbnail_link="static/lincoln-mxz-3782473_640.jpg",
            fullimage_link="static/lincoln-mxz-3782473_1920.jpg"
            )
   
        
    except IntegrityError:
        pass
    try:
        
        Images.create(
            name="runda",
            description=" runda_kenya",
            thumbnail_link="static/spring-2955582_640.jpg",
            fullimage_link="static/spring-2955582_1920.jpg",
            
            )
    except IntegrityError:
        pass
    
    try:
        
        Images.create(
            name="nyumba",
            description=" yaya",
            thumbnail_link="static/house-3778518_640.jpg",
            fullimage_link="static/house-3778518_1920 (1).jpg"
            )
    except IntegrityError:
        pass
    
    try:
        
        Images.create(
            name="tod",
            description=" buruburu",
            thumbnail_link="static/house-3420617_640.jpg",
            fullimage_link="static/house-3420617_1920.jpg"
            )
    except IntegrityError:
        pass


    try:
        
        Images.create(
            name="aki",
            description=" kilimani",
            thumbnail_link="static/vintage-1149558_640.jpg",
            fullimage_link="static/vintage-1149558_1920.jpg"
            )
    except IntegrityError:
        pass

    # try:
        
    #     Images.create(
    #         name="ak",
    #         description=" kille",
    #         thumbnail_link="static/villa-3709804_640.jpg",
    #         fullimage_link="static/villa-3709804_1920.jpg"
    #         )
    # except IntegrityError:
    #     pass
    try:
        
        Images.create(
            name="aku",
            description=" upperhill",
            thumbnail_link="static/st-gallen-3775386_640.jpg",
            fullimage_link="static/st-gallen-3775386_1920.jpg"
            )
    except IntegrityError:
        pass

    # try:
        
    #     Images.create(
    #         name="akisimani",
    #         description=" mountain_view",
    #         thumbnail_link="static/large-home-389271_640.jpg",
    #         fullimage_link="static/large-home-389271.jpg"
    #         )
    # except IntegrityError:
    #     pass

    try:
        
        Images.create(
            name="akisimn",
            description=" eastlands",
            thumbnail_link="static/lithuania-3723357_640.jpg",
            fullimage_link="static/lithuania-3723357_1920.jpg"
            )
    except IntegrityError:
        pass
    
    try:
      
        Images.create(
            name="akisin",
            description=" muthaiga",
            thumbnail_link="static/imatra-3778397_640.jpg",
            fullimage_link="static/imatra-3778397_1920.jpg"
            )
    except IntegrityError:
        pass

    
    
    try:
        
        Images.create(
            name="akin",
            description=" parkls",
            thumbnail_link="static/hungary-3726915_640.jpg",
            fullimage_link="static/hungary-3726915_1920.jpg"
            )
    except IntegrityError:
        pass
    
    
    try:
        
        Images.create(
            name="akn",
            description=" parklands",
            thumbnail_link="static/architecture-3725016_640.jpg",
            fullimage_link="static/hungary-3726915_1920.jpg"
            )
    except IntegrityError:
        pass   