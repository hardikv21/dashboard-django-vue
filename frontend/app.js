const routes = [
    {
        path: '/',
        component: user
    },
    {
        path: '/transaction',
        component: transaction
    }
];

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
});
  
const app = Vue.createApp({});
app.use(router);

app.mount('#app');