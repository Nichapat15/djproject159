from django import  forms
class productfrom(forms.Form):
    BRAND_LIST = [('Sharp','Sharp'),
                  ('Mitsubishi','Mitsubishi'),
                  ('Hatari', 'Hatari'),
                  ('Tefal', 'Tefal'),
                  ]
    COLOR_LIST = [('White','White'),
                  ('Black','Black'),
                  ('Gray', 'Gray'),
                  ('Cream', 'Cream'),
                  ]
    TYPE_LIST = [('Desk fan','Desk fan'),
                  ('Floor fan','Floor fan'),
                  ('Wall fan', 'wall fan'),
                  ]
    id=forms.CharField(max_length=13, label="รหัสสินค้า",required=True,
                       widget=forms.TextInput(attrs={'size':'15'}))
    brand = forms.CharField(max_length=30, label="ชื่อแบรนด์", required=True,
                         widget=forms.Select(choices=BRAND_LIST))
    model = forms.CharField(max_length=30, label="ชื่อรุ่น", required=True,
                         widget=forms.TextInput(attrs={'size': '35'}))
    color = forms.CharField(max_length=30, label="สี", required=True,
                         widget=forms.RadioSelect(choices=COLOR_LIST))
    type = forms.CharField(max_length=30, label="ประเภท", required=True,
                         widget=forms.Select(choices=TYPE_LIST))
    price = forms.IntegerField(label="ราคา", required=True,
                         widget=forms.NumberInput(attrs={'size': '35','min':'500','max':'100000'}))
