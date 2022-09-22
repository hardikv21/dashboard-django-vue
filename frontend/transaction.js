const transaction = {
    template: `
    <div class="container">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Product</th>
                    <th>Total</th>
                    <th>User</th>
                </tr> 
            </thead>
            <tbody>
                <tr v-for="transaction in transactions">
                    <td>{{ transaction.id }}</td>
                    <td
                        data-bs-toggle="modal"
                        data-bs-target="#exampleModal"
                        @click="productInfo(transaction.Product)"
                    >
                        {{ transaction.Product.name }}
                    </td>
                    <td>$ {{ transaction.total }}</td>
                    <td>{{ transaction.user ? transaction.user.name : '-' }}</td>
                </tr>
            </tbody>
        </table>

        <div
            class="modal fade"
            id="exampleModal"
            tabindex="-1"
            aria-labelledby="exampleModalLabel"
            aria-hidden="true"
        >
            <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">
                            {{ modalTitle }}
                        </h5>
                        <button
                            type="button"
                            class="btn-close"
                            data-bs-dismiss="modal"
                            aria-label="Close"
                        ></button>
                    </div>
                    <div class="modal-body">
                        <div class="input-group mb-3">
                            <span class="input-group-text">
                                ID
                            </span>
                            <input type="text" class="form-control" v-model="id" disabled>
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text">
                                Name
                            </span>
                            <input type="text" class="form-control" v-model="name" disabled>
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text">
                                Price
                            </span>
                            <input type="text" class="form-control" v-model="price" disabled>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>`,
    data() {
        return {
            transactions: [],
            modalTitle: "",
            id: 0,
            name: "",
            price: 0,
        }
    },
    methods: {
        refreshData() {
            axios.get(variables.API_URL + "transaction")
                .then((response) => this.transactions = response.data)
                .catch((error) => console.log(error.message));
        },
        productInfo(product) {
            this.modalTitle = "Product Information";
            this.id = product.id;
            this.name = product.name;
            this.price = product.price;
        }
    },
    mounted: function() {
        this.refreshData();
    }
}