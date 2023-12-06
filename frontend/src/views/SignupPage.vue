<template>
    <div class="signin-container">
        <el-form v-loading="loading" label-position="top" label-width="100px" :model="signupForm" style="max-width: 460px"
            class="form">
            <h2>Join us!</h2>

            <el-form-item label="First Name">
                <el-input v-model="signupForm.first_name" />
            </el-form-item>
            <el-form-item label="Last Name">
                <el-input v-model="signupForm.last_name" />
            </el-form-item>
            <el-form-item label="Username">
                <el-input v-model="signupForm.username" />
            </el-form-item>
            <el-form-item label="Email">
                <el-input v-model="signupForm.email" />
            </el-form-item>
            <el-form-item label="Password">
                <el-input type="password" v-model="signupForm.password" />
            </el-form-item>

            <el-form-item>
                <el-button @click="createAccount">Sign Up</el-button>
            </el-form-item>
        </el-form>

    </div>
</template>
  
<script>
import { reactive } from "vue";
import { AuthService } from "../common/auth.service.js"

const signupForm = reactive({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
});

export default {
    name: "SignupPage",

    mounted() {
        signupForm.first_name = "";
        signupForm.last_name = "";
        signupForm.username = "";
        signupForm.email = "";
        signupForm.password = "";
    },

    data: function () {
        return {
            signupForm,
            loading: false
        };
    },
    methods: {
        async createAccount() {
            this.loading = true;
            await AuthService.signup(this.signupForm)
            this.loading = false;
        }

    }

};
</script>
  
<style>
.signin-container {
    height: 70vh;
    display: flex;
    gap: 5%;
    justify-content: center;
    align-items: center;
}

.form {
    width: 60%;
}

.divider {
    width: 8px;
    height: 60vh;
    background-color: #105979;
    border-radius: 40px;
}
</style>
  