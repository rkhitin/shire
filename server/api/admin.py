from django.contrib import admin
from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import Customer, CustomerSettings, Category, Habbit, Obstacle, OvercomePlan


class CustomerSettingsInline(admin.TabularInline):
    model = CustomerSettings


class CustomersAdmin(admin.ModelAdmin):
    model = Customer
    inlines = [
        CustomerSettingsInline,
    ]


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm


admin.site.register(Habbit)
admin.site.register(OvercomePlan)
admin.site.register(Obstacle)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomersAdmin)
