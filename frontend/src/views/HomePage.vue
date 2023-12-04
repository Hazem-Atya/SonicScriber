<template>
   <img class="home-background-image" :src="wave" alt="background element" />
   <div class="banner">
     <div class="banner-description">
       <div class="description-text">
         Welcome to <span class="bold"> SonicScribe</span> <br />
         The hub of audio transcription. 
         <el-button class="start-button">Start Now</el-button>
       </div>
     </div>
     <el-image
       style="width: 700px; height: 450px; z-index: 0"
       :src="audi_to_text"
       :fit="fit"
     />
   </div>
 
   <div class="about">
     <span class="about-title bold"> About The Project </span>
     <span class="about-content">
       This project is offering users the possibility to transcribe different
       audio sequences with the goal of populating a data base that will be used
       to feed an AI audio transciptor so start now by subscribing with our
       platform and be among the trusted transcriptors.</span
     >
     <el-button class="join-button">Join Now</el-button>
   </div>
 </template>
 
 <script>
 import { ElButton, ElImage } from "element-plus";
 import audi_to_text from "../assets/images/att.png";
 import wave from "../assets/images/wave2.jpg";
 export default {
   components: { ElButton, ElImage },
   data: function () {
     return {
       audi_to_text,
       wave,
     };
   },
 };
 </script>
 
 <style>
 .home-background-image {
   position: absolute;
   width: 70%;
   z-index: -60;
   top: 20vh;
   left: 0vh;
   opacity: 0.2;
   -webkit-transform: rotate(45deg);
   -moz-transform: rotate(45deg);
   -ms-transform: rotate(45deg);
   -o-transform: rotate(45deg);
   transform: rotate(45deg);
 }
 .banner {
   display: flex;
   align-items: center;
   justify-content: flex-end;
 }
 
 .banner-description {
   position: absolute;
   z-index: 5;
   left: 40px;
 }
 
 .bold {
   font-weight: bolder;
 }
 
 .description-text {
   font-size: xx-large;
   width: 800px;
 }
 
 .start-button {
   width: 80%;
   background-color: #105979;
   color: white;
 }
 
 .about {
   margin-top: 25vh;
   display: flex;
   align-items: center;
   flex-direction: column;
   margin-bottom: 15vh;
 }
 .about-title {
   font-size: xx-large;
 }
 .about-content {
   font-size: x-large;
   text-align: center;
   margin-top: 5vh;
 }
 .join-button {
   width: 40%;
   background-color: #105979;
   color: white;
   margin-top: 5vh;
 }
 </style>
 