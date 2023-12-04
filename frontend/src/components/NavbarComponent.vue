<template>
    <el-row>
        <el-col>
            <el-menu class="menu" mode="horizontal" :ellipsis="true">
                <el-menu-item index="0" class="logo-header">
                    <img style="width: 50px" :src="image" alt="Element logo" />
                    <el-text tag="b" size="large">SonicScribe</el-text>
                </el-menu-item>

                <router-link to="/">
                    <el-menu-item index="1">Home</el-menu-item>
                </router-link>
                <router-link to="/audios">
                    <el-menu-item v-if="AuthService.isLoggedIn()" index="2">All Audios</el-menu-item>
                </router-link>
       
    
                <div class="flex-grow"></div>

                <router-link to="/signup">
                    <el-menu-item index="5" v-if="!AuthService.isLoggedIn()">Sign up</el-menu-item>
                </router-link>
                <router-link to="/login">
                    <el-menu-item index="4" v-if="!AuthService.isLoggedIn()">Login</el-menu-item>
                </router-link>
                <el-menu-item  @click="logout" index="4" v-if="AuthService.isLoggedIn()">Logout</el-menu-item>
            </el-menu>
            
        </el-col>
    </el-row>
</template>
  
<script>

import image from "../assets/images/soniscrub_bg.png";
import { AuthService } from "../common/auth.service.js"



export default {
    data: function () {
        return {
            image,
            AuthService
        };
    },
    methods: {
        logout(){
            AuthService.logout();
            this.$router.push("/")
        }
    }
};
</script>
  
<style>
.container {
    margin-top: 10vh;
    margin-left: 10%;
    margin-right: 5%;
}

.logo-header {
    gap: 10px;
}

.flex-grow {
    flex-grow: 0.9;
}

a {
    text-decoration: none !important;
    ;
}
</style>
  