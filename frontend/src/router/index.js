import { createRouter, createWebHistory } from "vue-router";
import HomePage from './../views/HomePage.vue'
import AudiosList from './../views/AudiosList.vue'
import Audio from './../views/AudioPage.vue'
import Login from './../views/LoginPage.vue'
import Signup from './../views/SignupPage.vue'
import NotFound from './../views/NotFound.vue'
import { AuthService } from "../common/auth.service.js"

const redirectIfNotLoggedIn = (to, from, next) => {
  if (!AuthService.isLoggedIn()) {
    next('/login');
  } else {
    next();
  }
}

const redirectIfLoggedIn = (to, from, next) => {
  if (AuthService.isLoggedIn()) {
    next('/');
  } else {
    next();
  }
}


export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage,
    },
    {
      path: "/audios",
      name: "audios",
      component: AudiosList,
      beforeEnter: redirectIfNotLoggedIn
    },
    {
      path: "/audio/:id",
      name: "audio",
      component: Audio,
    },
    {
      path: "/login",
      name: "login",
      component: Login,
      beforeEnter: redirectIfLoggedIn
    },
    {
      path: "/signup",
      name: "signup",
      component: Signup,
      beforeEnter: redirectIfLoggedIn
    },
    {
      path: "/:notfound",
      name: "notFound",
      component: NotFound
    }
  ]
})
export default router;
