const user = {
    template: `
    <div class="container">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Firm</th>
                </tr> 
            </thead>
            <tbody>
                <tr v-for="user in users">
                    <td>{{ user.id }}</td>
                    <td
                        data-bs-toggle="modal"
                        data-bs-target="#exampleModal"
                        @click="userInfo(user)"
                    >
                        {{ user.name }}
                    </td>
                    <td>{{ user.email }}</td>
                    <td
                        data-bs-toggle="modal"
                        data-bs-target="#exampleModal"
                        @click="firmInfo(user.Firm)"
                    >
                        {{ user.Firm.name }}
                    </td>
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
                        <div v-if="email" class="input-group mb-3">
                            <span class="input-group-text">
                                Email
                            </span>
                            <input type="text" class="form-control" v-model="email" disabled>
                        </div>
                        <div v-if="firm" class="input-group mb-3">
                            <span class="input-group-text">
                                Firm
                            </span>
                            <input type="text" class="form-control" v-model="firm" disabled>
                        </div>
                        <div v-if="email" class="input-group mb-3">
                            <span class="input-group-text">
                                Transactions
                            </span>
                            <ul class="list-group" style="width: 100%">
                                <li class="list-group-item" v-for="transaction in transactions">
                                    {{ transaction.Product.name }} - $ {{ transaction.Product.price }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>`,
    data() {
        return {
            users: [],
            modalTitle: "",
            id: 0,
            name: "",
            email: "",
            firm: "",
            transactions: [],
        }
    },
    methods: {
        refreshData() {
            axios.get(variables.API_URL + "user")
                .then((response) => this.users = response.data)
                .catch((error) => console.log(error.message));
        },
        userInfo(user) {
            axios.get(variables.API_URL + "transaction/user_transactions/" + user.id)
                .then((response) => {
                    this.modalTitle = "User Information";
                    this.id = user.id;
                    this.name = user.name;
                    this.email = user.email;
                    this.firm = user.Firm.name;
                    this.transactions = response.data;
                })
                .catch((error) => console.log(error.message));
        },
        firmInfo(firm) {
            this.modalTitle = "Firm Information";
            this.id = firm.id;
            this.name = firm.name;
            this.email = "";
            this.firm = "";
        }
    },
    mounted: function() {
        this.refreshData();
    }
}