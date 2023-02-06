from django.db import models

# Create your models here.
class Product:
    def __init__(self,id,brand,model,color,type,price,warranty,vat,net):
        self.id=id
        self.brand=brand
        self.model=model
        self.color=color
        self.type=type
        self.price=price
        self.warranty=warranty
        self.vat=vat
        self.net=net

    def __str__(self):
        return "id.{},brand.{},model.{},color.{},type.{},price.{},warranty.{},vat.{},net.{}"\
            .format(self.id,self.brand,self.model,self.color,self.type,self.price,
                    self.warranty,self.vat,self.net)