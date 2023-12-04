import { API_URL } from './config.js'
import TokenService from './token.service.js'
import { useToast } from 'vue-toast-notification';
import { router } from '../router'

const $toast = useToast();

export const AuthService = {

    signup(user) {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(user)
        };
        fetch(API_URL + '/users/signup/', requestOptions).then((response) => {
            response.json().then((data) => {
                if (!response.ok) {
                    $toast.error(JSON.stringify(data), {
                        position: "top-right",
                    });
                } else {
                    TokenService.saveToken(data.token)
                    $toast.success("Account created successfully!", {
                        position: "top-right",
                    });
                    router.push("/audios")
                }
            });
        })
            .catch((err) => {
                $toast.error(JSON.stringify(err), {
                    position: "top-right",
                });
            });
    }
    ,
    login(user) {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(user)
        };
        fetch(API_URL + '/users/login/', requestOptions).then((response) => {
            response.json().then((data) => {
                if (!response.ok) {
                    $toast.error(JSON.stringify(data), {
                        position: "top-right",
                    });
                } else {
                    TokenService.saveToken(data.token)
                    $toast.success("Welcome Back!", {
                        position: "top-right",
                    });
                    router.push("/audios")
                }
            });
        })
            .catch((err) => {
                $toast.error(JSON.stringify(err), {
                    position: "top-right",
                });
            });
    },
    logout() {
        TokenService.destroyToken()
        router.push('/login')
    },

    isLoggedIn() {
        return !!TokenService.getToken();
    }

}