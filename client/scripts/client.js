const Foo = { template: '<div>foo</div>' }

const routes = [
  { path: '/foo', component: Foo }
]

const router = new VueRouter({
  routes // short for `routes: routes`
})

const vue = new Vue({
            el: '#vue',
            data: { article : article },
            router
}).$mount('#app')