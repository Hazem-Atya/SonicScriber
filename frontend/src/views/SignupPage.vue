<template>
    <div class="signin-container">
        <el-form label-position="top" label-width="100px" :model="formLabelAlign" style="max-width: 460px" class="form">
            <h2>Join us!</h2>

            <el-form-item label="First Name">
                <el-input v-model="formLabelAlign.first_name" />
            </el-form-item>
            <el-form-item label="Last Name">
                <el-input v-model="formLabelAlign.last_name" />
            </el-form-item>
            <el-form-item label="Username">
                <el-input v-model="formLabelAlign.username" />
            </el-form-item>
            <el-form-item label="Email">
                <el-input  v-model="formLabelAlign.email" />
            </el-form-item>
            <el-form-item  label="Password">
                <el-input type="password" v-model="formLabelAlign.password" />
            </el-form-item>

            <el-form-item>
                <el-button @click="createAccount">Sign Up</el-button>
            </el-form-item>
        </el-form>

    </div>
</template>
  
<script>
import { reactive } from "vue";
import { ElForm, ElFormItem, ElInput, ElButton } from "element-plus";
import { AuthService } from "../common/auth.service.js"

const formLabelAlign = reactive({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
    confirm_password: "",
});

export default {
    name: "SignupPage",
    components: {
        ElForm,
        ElFormItem,
        ElInput,
        ElButton,
    },
    data: function () {
        return {
            formLabelAlign
        };
    },
    methods: {
        createAccount() {
            AuthService.signup(this.formLabelAlign)
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
  