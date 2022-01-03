class CheckoutPageMixin:
  
  def get_checkout_data(self, 
  firstName='test_name', 
  lastName="test_last_name",
  postalCode = "1234",
  ):
    return {
      "first-name": firstName, 
      "last-name": lastName,
      'postal-code': postalCode
    }

