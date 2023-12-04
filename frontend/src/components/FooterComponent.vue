<template>
    <div class="footer-container">
      <div class="footer-banner">
        <img style="width: 100px" :src="image" alt="Element logo" />
        <span class="title">SonicScribe</span>
      </div>
      <div class="footer-info">
        <div class="footer-bloc">
          <span class="title">Contact Us</span>
          <span>Kélibia, Nabeul, Tunisia</span>
          <span>contact@sonicscribe.io</span>
          <span>(+216) 11 222 333</span>
        </div>
        <div class="footer-bloc">
          <span class="title">Start now</span>
          <a href="#/audios" class="ref">Audios</a>
          <a href="#/myaudios" class="ref">Logout</a>
        </div>
        <div class="footer-bloc">
          <span class="title">Company</span>
          <span>About Us</span>
          <span>Vision</span>
          <span>Team</span>
        </div>
        <div class="footer-bloc">
          <span class="title">Social Media</span>
          <span>Facebook</span>
          <span>Instagram</span>
          <span>LinkedIn</span>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import image from "../assets/images/soniscrub_bg.png";
  
  import { ref } from "vue";
  
  const currentPath = ref(window.location.hash);
  
  window.addEventListener("hashchange", () => {
    currentPath.value = window.location.hash;
  });
  
  export default {
    data: function () {
      return {
        image,
      };
    },
  };
  </script>
  
  <style>
  .footer-banner {
    width: 15%;
  }
  .title {
    font-weight: bolder;
    margin-bottom: 1vh;
  }
  .logo-header {
    gap: 10px;
  }
  
  .footer-container {
    margin-top: 4vh;
    padding-left: 10%;
    background-color: #105979;
    color: white;
    height: 25vh;
    display: flex;
    align-items: center;
    gap: 10%;
  }
  
  .footer-info {
    width: 80%;
    display: flex;
    column-gap: 10%;
  }
  .footer-bloc {
    display: flex;
    gap: 10%;
    justify-content: center;
    flex-direction: column;
  }
  .footer-copyright {
    justify-content: center;
    display: flex;
  }
  .ref {
    text-decoration: none;
    color: white;
  }
  </style>
  