from django import forms

class CartAddProductForm(forms.Form):
    """
    Form for adding products to cart.
    Quantity is fixed at 1, but we include a hidden field with value 1
    to maintain compatibility with views expecting this field.
    """
    quantity = forms.IntegerField(
        initial=1,
        min_value=1,
        max_value=1,
        widget=forms.HiddenInput
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )


# from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(
#         choices=PRODUCT_QUANTITY_CHOICES,
#         coerce=int
#     )
#     override = forms.BooleanField(
#         required=False,
#         initial=False,
#         widget=forms.HiddenInput
#     )

