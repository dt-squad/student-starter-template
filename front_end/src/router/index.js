import {createRouter, createWebHistory} from "vue-router"
import manage_jobs_view from "../views/manage_jobs_view.vue"
import home from "../views/home.vue"

const router = createRouter({history:createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {"path" : "/", "name" : "home", "component":home},
        {"path" : "/manage_jobs", "name" : "manage_jobs", "component":manage_jobs_view},
    ]
})

export default router