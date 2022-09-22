from DashboardApp.models import Firm, User, Product, Transaction


def testData(self):
    self.firm1 = Firm.objects.create(name="Firm1")
    self.firm2 = Firm.objects.create(name="Firm2")
    self.user1 = User.objects.create(name="User1", email="user1@dashboard.com", Firm=self.firm1)
    self.user2 = User.objects.create(name="User2", email="user2@dashboard.com", Firm=self.firm2)
    self.product1 = Product.objects.create(name="Product1", price=10)
    self.product2 = Product.objects.create(name="Product2", price=5)
    self.transaction1 = Transaction.objects.create(Product=self.product1, total=10, user=self.user1)
    self.transaction2 = Transaction.objects.create(Product=self.product2, total=5)