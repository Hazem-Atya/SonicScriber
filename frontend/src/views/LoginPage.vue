<template>
    <div class="signin-container">
        <el-form label-position="top" label-width="100px" :model="formLabelAlign" style="max-width: 460px" class="form">
            <h2>Login</h2>
            <br>
            <el-form-item label="Username">
                <el-input v-model="formLabelAlign.username" />
            </el-form-item>
            <el-form-item label="Password">
                <el-input type="password" v-model="formLabelAlign.password" />
            </el-form-item>
            <el-form-item>
                <el-button @click="login">Login</el-button>
            </el-form-item>
        </el-form>

    </div>
</template>
  
<script>
import { reactive } from "vue";
import { ElForm, ElFormItem, ElInput, ElButton } from "element-plus";
import { AuthService } from "../common/auth.service.js"

const formLabelAlign = reactive({
    username: "",
    password: "",
});

export default {
    name: "LoginPage",
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
        login() {
            AuthService.login(formLabelAlign);
            formLabelAlign.username=""
            formLabelAlign.password=""
        }
    }
};
</script>
  
<style>
.signin-container {
    height: 50vh;
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
    height: 50vh;
    background-color: #105979;
    border-radius: 40px;
}
</style>
  